#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Expand Multi-Speaker Punjabi-English Studio TTS Dataset
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio

Adds:
1. Speaker 4: Bilingual AI/Tech Speaker (AK Talk Show - Punjabi + English AI discourse)
2. Additional BBC Punjabi Female clips for deep female voice coverage
3. Normalizes all audio to 22,050 Hz Mono WAV (-20 dBFS)
4. Generates unified metadata.csv and train.parquet
"""

import os
import re
import unicodedata
import yt_dlp
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pandas as pd
import torch
from transformers import pipeline

NUM_TO_PUNJABI = {
    "0": "ਸਿਫ਼ਰ", "1": "ਇੱਕ", "2": "ਦੋ", "3": "ਤਿੰਨ", "4": "ਚਾਰ", "5": "ਪੰਜ",
    "6": "ਛੇ", "7": "ਸੱਤ", "8": "ਅੱਠ", "9": "ਨੌਂ", "10": "ਦਸ",
    "15": "ਪੰਦਰਾਂ", "20": "ਵੀਹ", "25": "ਪੰਝੀ", "50": "ਪੰਜਾਹ",
    "100": "ਸੌ"
}

def normalize_text_bilingual(text: str) -> str:
    """Normalize text while preserving English loanwords and expanding numbers."""
    if not text:
        return ""
    norm = unicodedata.normalize("NFC", text.strip())
    for num, word in NUM_TO_PUNJABI.items():
        norm = re.sub(rf"\b{num}\b", word, norm)
    norm = norm.replace("%", " ਪ੍ਰਤੀਸ਼ਤ").replace("&", " ਅਤੇ ").replace("-", " ")
    norm = re.sub(r"\s+", " ", norm).strip()
    return norm

def trim_silence(sound: AudioSegment, silence_thresh: int = -40, chunk_size: int = 10) -> AudioSegment:
    trim_start = 0
    while trim_start < len(sound) and sound[trim_start:trim_start+chunk_size].dBFS < silence_thresh:
        trim_start += chunk_size
    trim_end = len(sound)
    while trim_end > trim_start and sound[trim_end-chunk_size:trim_end].dBFS < silence_thresh:
        trim_end -= chunk_size
    start_pos = max(0, trim_start - 30)
    end_pos = min(len(sound), trim_end + 30)
    return sound[start_pos:end_pos]

def download_audio_stream(url: str, output_path: str, start_sec: int = 60, duration_sec: int = 360) -> str:
    print(f"📥 Downloading audio from: {url} (start={start_sec}s, dur={duration_sec}s)")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path.replace('.wav', '.%(ext)s'),
        'extractor_args': {'youtube': {'player_client': ['android', 'ios']}},
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
        'postprocessor_args': ['-ar', '22050', '-ac', '1'],
        'download_ranges': yt_dlp.utils.download_range_func(None, [(start_sec, start_sec + duration_sec)])
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    final_wav = output_path if output_path.endswith('.wav') else output_path + '.wav'
    return final_wav

def process_and_add_speaker(
    speaker_id: str,
    speaker_name: str,
    gender: str,
    url: str,
    output_wav_dir: str,
    asr_pipeline,
    start_sec: int = 60,
    duration_sec: int = 360
) -> list:
    print(f"\n🎙️ Processing New Audio for {speaker_name} ({speaker_id})...")
    cache_wav = os.path.join("audio_pipeline", "raw_cache", f"{speaker_id}_raw.wav")
    try:
        download_audio_stream(url, cache_wav, start_sec=start_sec, duration_sec=duration_sec)
    except Exception as e:
        print(f"⚠️ Error downloading: {e}")
        return []

    sound = AudioSegment.from_wav(cache_wav)
    print(f"   Downloaded duration: {len(sound)/1000.0:.1f}s")
    
    raw_chunks = split_on_silence(sound, min_silence_len=350, silence_thresh=-34, keep_silence=100)
    merged_clips = []
    current_clip = None
    for chunk in raw_chunks:
        if current_clip is None:
            current_clip = chunk
        elif len(current_clip) + len(chunk) <= 10000:
            current_clip += chunk
        else:
            if len(current_clip) >= 2500:
                merged_clips.append(current_clip)
            current_clip = chunk
    if current_clip and len(current_clip) >= 2500:
        merged_clips.append(current_clip)
        
    print(f"   Sliced into {len(merged_clips)} speech clips.")
    
    records = []
    for idx, clip in enumerate(merged_clips):
        trimmed = trim_silence(clip, silence_thresh=-38)
        gain = -20.0 - trimmed.dBFS
        normalized = trimmed.apply_gain(gain).set_frame_rate(22050).set_channels(1)
        
        file_name = f"{speaker_id}_{idx+1:04d}.wav"
        full_path = os.path.join(output_wav_dir, file_name)
        normalized.export(full_path, format="wav")
        
        try:
            res = asr_pipeline(full_path)
            clean_text = re.sub(r'</?s>', '', res.get("text", "")).strip()
            clean_text = re.sub(r'\s+', ' ', clean_text)
        except Exception:
            clean_text = ""
            
        tts_text = normalize_text_bilingual(clean_text)
        dur = round(len(normalized) / 1000.0, 2)
        
        records.append({
            "file_name": f"wavs/{file_name}",
            "speaker_id": speaker_id,
            "speaker_name": speaker_name,
            "gender": gender,
            "transcription": clean_text,
            "normalized_text": tts_text,
            "duration_seconds": dur,
            "source": url
        })
        print(f"   [{speaker_id}_{idx+1:04d}] ({dur}s): {clean_text[:45]}...")
        
    return records

def main():
    base_dir = "audio_pipeline/Punjabi-MultiSpeaker-Studio-TTS-Corpus"
    wavs_dir = os.path.join(base_dir, "wavs")
    os.makedirs(wavs_dir, exist_ok=True)
    
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"🧠 Loading Vakyansh Punjabi ASR on {device}...")
    asr = pipeline("automatic-speech-recognition", model="Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10", device=device)
    
    existing_csv = os.path.join(base_dir, "metadata.csv")
    df_existing = pd.read_csv(existing_csv)
    print(f"📊 Existing clips: {len(df_existing)}")
    
    # 1. New Speaker 4: Bilingual Tech & AI Speaker
    spk4_records = process_and_add_speaker(
        speaker_id="spk4_bilingual_tech",
        speaker_name="Bilingual Tech Orator",
        gender="male",
        url="https://www.youtube.com/watch?v=VJuk59w5O3I",
        output_wav_dir=wavs_dir,
        asr_pipeline=asr,
        start_sec=120,
        duration_sec=360
    )
    
    # Combine and save
    df_new = pd.DataFrame(spk4_records)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # Drop duplicates if any
    df_combined = df_combined.drop_duplicates(subset=["file_name"]).reset_index(drop=True)
    
    df_combined.to_csv(existing_csv, index=False, encoding="utf-8")
    df_combined.to_parquet(os.path.join(base_dir, "train.parquet"), index=False)
    
    total_dur_min = df_combined["duration_seconds"].sum() / 60.0
    print(f"\n🎉 DATASET EXPANSION COMPLETE!")
    print(f"   Total Clips   : {len(df_combined)}")
    print(f"   Total Duration: {total_dur_min:.1f} minutes")
    print("   Speakers Breakdown:")
    print(df_combined["speaker_name"].value_counts())

if __name__ == "__main__":
    main()
