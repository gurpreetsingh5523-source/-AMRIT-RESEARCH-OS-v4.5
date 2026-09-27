#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Punjabi Neural Text-to-Speech (PTTS) Synthesizer & Audio Player
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio

Synthesizes Punjabi text directly using the high-fidelity VITS ONNX model
and plays the generated speech aloud through macOS speakers via `afplay`.
"""

import os
import sys
import argparse
import subprocess
import soundfile as sf
import onnxruntime as ort
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download

DEFAULT_MODEL_REPO = "Nam-toon-studio/punjabi-tts-voices"
DEFAULT_ONNX_LOCAL = os.path.join(os.path.dirname(__file__), "punjabi_mms.onnx")

def get_model_path(download_from_hf: bool = False) -> str:
    """Resolve model path: either local ONNX file or download from Hugging Face Hub."""
    if not download_from_hf and os.path.exists(DEFAULT_ONNX_LOCAL):
        print(f"📁 Local ONNX model mil gaya: {DEFAULT_ONNX_LOCAL}")
        return DEFAULT_ONNX_LOCAL
    
    print(f"🌐 Hugging Face ਤੋਂ ਮਾਡਲ ਡਾਊਨਲੋਡ ਹੋ ਰਿਹਾ ਹੈ: {DEFAULT_MODEL_REPO} (pa-guru-female.onnx)...")
    downloaded_path = hf_hub_download(
        repo_id=DEFAULT_MODEL_REPO,
        filename="pa-guru-female.onnx"
    )
    print(f"✅ ਮਾਡਲ ਡਾਊਨਲੋਡ ਹੋ ਗਿਆ: {downloaded_path}")
    return downloaded_path

def synthesize_punjabi(
    text: str,
    model_path: str,
    output_wav: str = "audio_pipeline/punjabi_output.wav",
    play_audio: bool = True
) -> str:
    """Convert Punjabi text to audio and play via system speakers."""
    print(f"\n🗣️ ਬੋਲਣ ਵਾਲਾ ਵਾਕ (Input Text): \"{text}\"")
    
    # 1. Initialize tokenizer
    tokenizer_source = "facebook/mms-tts-pan"
    tok_dir = os.path.join(os.path.dirname(__file__), "tokenizer_files")
    if os.path.exists(os.path.join(tok_dir, "vocab.json")):
        tokenizer = AutoTokenizer.from_pretrained(tok_dir)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_source)
        
    # 2. Tokenize Gurmukhi text
    inputs = tokenizer(text, return_tensors="np")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    print(f"🔤 ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਮੁਕੰਮਲ ({input_ids.shape[1]} ਟੋਕਨ)")

    # 3. Load ONNX session and run inference
    print("🧠 ਆਵਾਜ਼ ਮਾਡਲ (Neural TTS) ਅਵਾਜ਼ ਤਿਆਰ ਕਰ ਰਿਹਾ ਹੈ...")
    session = ort.InferenceSession(model_path)
    ort_inputs = {
        "input_ids": input_ids,
        "attention_mask": attention_mask
    }
    outputs = session.run(None, ort_inputs)
    waveform = outputs[0].flatten()
    
    sample_rate = 16000
    duration_sec = len(waveform) / sample_rate
    print(f"🎵 ਆਡੀਓ ਤਿਆਰ ਹੋ ਗਈ: {duration_sec:.2f} ਸਕਿੰਟ (ਸੈਂਪਲ ਰੇਟ: {sample_rate}Hz)")

    # 4. Save to WAV
    os.makedirs(os.path.dirname(os.path.abspath(output_wav)), exist_ok=True)
    sf.write(output_wav, waveform, sample_rate)
    print(f"💾 ਆਡੀਓ ਫਾਈਲ ਸੇਵ ਕੀਤੀ ਗਈ: {output_wav}")

    # 5. Play aloud on macOS
    if play_audio:
        print("\n🔊 ਆਡੀਓ ਸਪੀਕਰਾਂ 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ (afplay)... ਸੁਣੋ ਜੀ:")
        subprocess.run(["/usr/bin/afplay", output_wav], check=True)
        print("✅ ਆਵਾਜ਼ ਸਫਲਤਾਪੂਰਵਕ ਚੱਲ ਚੁੱਕੀ ਹੈ।")

    return output_wav

def main():
    parser = argparse.ArgumentParser(description="ੴ Punjabi Neural TTS Synthesizer & Player")
    parser.add_argument(
        "--text",
        type=str,
        default="ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ ਜੀ, ਅੰਮ੍ਰਿਤ ਰਿਸਰਚ ਓ.ਐਸ. ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ। ਇਹ ਪੰਜਾਬੀ ਮਾਡਲ ਹੁਣ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।",
        help="Punjabi Gurmukhi text to speak"
    )
    parser.add_argument(
        "--download-hf",
        action="store_true",
        help="Download model file directly from Hugging Face hub"
    )
    parser.add_argument(
        "--no-play",
        action="store_true",
        help="Do not play audio through speakers"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="audio_pipeline/punjabi_output.wav",
        help="Output WAV file path"
    )
    args = parser.parse_args()

    model_path = get_model_path(download_from_hf=args.download_hf)
    synthesize_punjabi(
        text=args.text,
        model_path=model_path,
        output_wav=args.output,
        play_audio=not args.no_play
    )

if __name__ == "__main__":
    main()
