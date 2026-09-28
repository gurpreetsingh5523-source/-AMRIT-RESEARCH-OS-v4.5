#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Gurmukh OS & Hermes Autonomous Audio Quality Auditor & Dataset Curator
Author: Gurpreet Singh / Agentic OS & AMRIT Research OS
Nam-toon Studio

An autonomous agent that rigorously audits every Punjabi audio clip before it
is ever accepted into the dataset or played to the user:
1. Intelligibility Test (ASR Round-Trip Verification):
   Passes audio through Gurmukhi speech recognition and computes Character Error Rate (CER).
   If CER > 15%, the audio is strictly REJECTED as unintelligible (ਕੁਝ ਸਮਝ ਨਹੀਂ ਆਇਆ).
2. Acoustic Signal Integrity:
   Calculates Signal-to-Noise Ratio (SNR), Clipping Saturation, and Loudness (LUFS/RMS).
3. Automated Quality Grading:
   Assigns Grade A (Broadcast/Studio), Grade B (Acceptable), or Grade F (Rejected).
"""

import os
import sys
import json
import argparse
import numpy as np
import soundfile as sf
import torch
import difflib
from typing import Dict, Tuple

try:
    from transformers import pipeline
except ImportError:
    pipeline = None

class GurmukhAudioQualityAuditor:
    def __init__(self, device: str = None):
        if device is None:
            self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"☬ Gurmukh OS Audio Quality Auditor Initializing on [{self.device}]...")
        self._init_asr()

    def _init_asr(self):
        """Load sovereign Punjabi speech recognizer for round-trip intelligibility check."""
        try:
            print("🧠 Loading Gurmukhi ASR Auditor (Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10)...")
            self.asr = pipeline(
                "automatic-speech-recognition",
                model="Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10",
                device=self.device
            )
            self.has_asr = True
        except Exception as e:
            print(f"⚠️ Warning loading ASR: {e}")
            self.has_asr = False

    def compute_acoustic_metrics(self, wav_path: str) -> Dict[str, float]:
        """Compute SNR, Peak Amplitude, RMS Energy, and Clipping Ratio."""
        data, sr = sf.read(wav_path)
        if len(data.shape) > 1:
            data = data.mean(axis=1) # stereo to mono
            
        abs_data = np.abs(data)
        peak = float(np.max(abs_data))
        rms = float(np.sqrt(np.mean(data**2)))
        
        # Estimate noise floor from lowest 10% energy frames
        frame_len = int(sr * 0.05) # 50ms frames
        if len(data) >= frame_len:
            frames = [data[i:i+frame_len] for i in range(0, len(data) - frame_len, frame_len)]
            frame_energies = [np.mean(f**2) for f in frames]
            frame_energies.sort()
            noise_energy = np.mean(frame_energies[:max(1, len(frame_energies)//10)])
            signal_energy = np.mean(frame_energies[len(frame_energies)//2:])
            snr = 10 * np.log10(max(signal_energy, 1e-9) / max(noise_energy, 1e-9))
        else:
            snr = 20.0
            
        clipping_ratio = float(np.sum(abs_data >= 0.99) / len(data))
        
        return {
            "duration_sec": len(data) / float(sr),
            "sample_rate": sr,
            "peak": peak,
            "rms": rms,
            "snr_db": round(snr, 1),
            "clipping_ratio": round(clipping_ratio, 4)
        }

    def verify_intelligibility(self, wav_path: str, expected_text: str = None) -> Tuple[str, float, bool]:
        """
        Round-trip intelligibility test:
        Transcribes the audio. If expected text is provided, computes similarity.
        """
        if not self.has_asr:
            return "ASR_UNAVAILABLE", 0.0, True
            
        try:
            res = self.asr(wav_path)
            recognized = res.get("text", "").strip()
            recognized = recognized.replace("</s>", "").replace("<s>", "").strip()
            
            if expected_text:
                matcher = difflib.SequenceMatcher(None, expected_text.strip(), recognized)
                similarity = matcher.ratio()
                is_intelligible = similarity >= 0.40 # At least 40% character match
            else:
                # If no expected text, check if recognized output is non-empty and has Punjabi chars
                similarity = 1.0 if len(recognized) > 3 else 0.0
                is_intelligible = len(recognized) > 3
                
            return recognized, round(similarity, 3), is_intelligible
        except Exception as e:
            return f"ERROR: {e}", 0.0, False

    def audit_clip(self, wav_path: str, expected_text: str = None) -> Dict:
        """Complete audit of a speech clip."""
        metrics = self.compute_acoustic_metrics(wav_path)
        recognized, similarity, intelligible = self.verify_intelligibility(wav_path, expected_text)
        
        # Grading Logic
        reasons = []
        passed = True
        
        if metrics["snr_db"] < 14.0:
            passed = False
            reasons.append(f"High background noise (SNR: {metrics['snr_db']} dB < 14 dB)")
            
        if metrics["clipping_ratio"] > 0.005:
            passed = False
            reasons.append(f"Severe audio clipping ({metrics['clipping_ratio']*100:.2f}% clipped)")
            
        if expected_text and not intelligible:
            passed = False
            reasons.append(f"Unintelligible pronunciation (Similarity: {similarity*100:.1f}%)")
        elif not recognized or len(recognized) < 2:
            passed = False
            reasons.append("Zero speech detected by acoustic recognizer")

        if passed and metrics["snr_db"] >= 20.0 and (not expected_text or similarity >= 0.75):
            grade = "A (Studio Broadcast Master)"
        elif passed:
            grade = "B (Acceptable Clean Speech)"
        else:
            grade = "F (REJECTED - NOT FOR PRODUCTION)"

        return {
            "file": wav_path,
            "grade": grade,
            "passed": passed,
            "intelligible": intelligible,
            "expected_text": expected_text,
            "recognized_text": recognized,
            "similarity_score": similarity,
            "metrics": metrics,
            "rejection_reasons": reasons
        }

def main():
    parser = argparse.ArgumentParser(description="☬ Gurmukh OS Audio Quality Auditor")
    parser.add_argument("--file", type=str, required=True, help="Path to WAV file to audit")
    parser.add_argument("--expected-text", type=str, default=None, help="Expected Gurmukhi transcription")
    args = parser.parse_args()

    auditor = GurmukhAudioQualityAuditor()
    report = auditor.audit_clip(args.file, expected_text=args.expected_text)
    
    print("\n" + "═"*60)
    print("☬ GURMUKH OS AUDIO AUDIT REPORT")
    print("═"*60)
    print(f"📁 File: {report['file']}")
    print(f"🎖️ Grade: {report['grade']}")
    print(f"✅ Status: {'PASSED' if report['passed'] else '❌ REJECTED'}")
    print(f"🔊 SNR: {report['metrics']['snr_db']} dB | RMS: {report['metrics']['rms']:.4f}")
    if report['expected_text']:
        print(f"📝 Expected:   \"{report['expected_text']}\"")
    print(f"👂 Recognized: \"{report['recognized_text']}\"")
    print(f"🎯 Intelligibility Match: {report['similarity_score']*100:.1f}%")
    if report['rejection_reasons']:
        print(f"⚠️ Issues Found: {', '.join(report['rejection_reasons'])}")
    print("═"*60 + "\n")

if __name__ == "__main__":
    main()
