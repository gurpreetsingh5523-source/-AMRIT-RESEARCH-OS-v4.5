#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Multi-Speaker Punjabi Studio TTS Corpus Builder
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio

Builds a high-precision multi-speaker Punjabi Speech Dataset optimized for TTS:
1. Resamples to 22,050 Hz 16-bit Mono WAV.
2. Trims leading/trailing silence (<50ms).
3. Normalizes volume to -20 dBFS.
4. Produces normalized text (numbers -> Gurmukhi words) for Piper / VITS training.
5. Formats as multi-speaker LJSpeech / AudioFolder standard.
"""

import os
import re
import unicodedata
import yt_dlp
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pandas as pd
from transformers import pipeline
import torch

NUM_TO_PUNJABI = {
    "0": "ਸਿਫ਼ਰ", "1": "ਇੱਕ", "2": "ਦੋ", "3": "ਤਿੰਨ", "4": "ਚਾਰ", "5": "ਪੰਜ",
    "6": "ਛੇ", "7": "ਸੱਤ", "8": "ਅੱਠ", "9": "ਨੌਂ", "10": "ਦਸ",
    "15": "ਪੰਦਰਾਂ", "20": "ਵੀਹ", "25": "ਪੰਝੀ", "50": "ਪੰਜਾਹ",
    "60": "ਸੱਠ", "65": "ਪੈਂਹਠ", "70": "ਸੱਤਰ", "80": "ਅੱਸੀ",
    "85": "ਪਚਾਸੀ", "90": "ਨੱਬੇ", "100": "ਸੌ"
}

def normalize_tts_text(text: str) -> str:
    """Normalize text specifically for TTS training (expand numbers and symbols)."""
    if not text:
        return ""
    norm = unicodedata.normalize("NFC", text.strip())
    
    # Replace numbers with Punjabi words
    for num, word in NUM_TO_PUNJABI.items():
        norm = re.sub(rf"\b{num}\b", word, norm)
        
    # Replace percent and symbols
    norm = norm.replace("%", " ਪ੍ਰਤੀਸ਼ਤ")
    norm = norm.replace("&", " ਅਤੇ ")
    norm = norm.replace("-", " ")
    
    # Clean whitespace
    norm = re.sub(r"\s+", " ", norm).strip()
    return norm

def trim_silence(sound: AudioSegment, silence_thresh: int = -40, chunk_size: int = 10) -> AudioSegment:
    """Trim leading and trailing silence to ensure tight phoneme boundaries for TTS."""
    trim_start = 0
    while trim_start < len(sound) and sound[trim_start:trim_start+chunk_size].dBFS < silence_thresh:
        trim_start += chunk_size
        
    trim_end = len(sound)
    while trim_end > trim_start and sound[trim_end-chunk_size:trim_end].dBFS < silence_thresh:
        trim_end -= chunk_size
        
    # Keep 30ms padding
    start_pos = max(0, trim_start - 30)
    end_pos = min(len(sound), trim_end + 30)
    return sound[start_pos:end_pos]

def download_audio_stream(url: str, output_path: str, duration_sec: int = 360) -> str:
    """Download audio stream from YouTube, resample to 22050Hz mono WAV."""
    print(f"📥 Downloading audio from: {url}")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path.replace('.wav', '.%(ext)s'),
        'extractor_args': {'youtube': {'player_client': ['android', 'ios']}},
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
        'postprocessor_args': ['-ar', '22050', '-ac', '1'],
        'download_ranges': yt_dlp.utils.download_range_func(None, [(30, 30 + duration_sec)])
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    final_wav = output_path if output_path.endswith('.wav') else output_path + '.wav'
    print(f"✅ Audio ready at: {final_wav}")
    return final_wav

def process_speaker(
    speaker_id: str,
    speaker_name: str,
    gender: str,
    url: str,
    output_wav_dir: str,
    asr_pipeline,
    duration_sec: int = 300,
    start_sec: int = 30
) -> list:
    """Download, slice, transcribe, and normalize audio for a specific speaker."""
    print(f"\n🎙️ Processing Speaker: {speaker_name} ({gender}, ID: {speaker_id})")
    cache_wav = os.path.join("audio_pipeline", "raw_cache", f"{speaker_id}_raw.wav")
    
    # 1. Download
    try:
        download_audio_stream(url, cache_wav, duration_sec=duration_sec)
    except Exception as e:
        print(f"⚠️ Error downloading {url}: {e}")
        return []
        
    # 2. Slice into 3s - 10s speech chunks
    sound = AudioSegment.from_wav(cache_wav)
    print(f"   Downloaded audio duration: {len(sound)/1000.0:.1f}s")
    
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
    
    # 3. Export normalized 22,050Hz WAV with tight silence trimming
    speaker_records = []
    for idx, clip in enumerate(merged_clips):
        trimmed = trim_silence(clip, silence_thresh=-38)
        change_in_dBFS = -20.0 - trimmed.dBFS
        normalized = trimmed.apply_gain(change_in_dBFS)
        normalized = normalized.set_frame_rate(22050).set_channels(1)
        
        file_name = f"{speaker_id}_{idx+1:04d}.wav"
        full_path = os.path.join(output_wav_dir, file_name)
        normalized.export(full_path, format="wav")
        
        # ASR transcription
        try:
            res = asr_pipeline(full_path)
            raw_text = res.get("text", "")
            clean_text = re.sub(r'</?s>', '', raw_text).strip()
            clean_text = re.sub(r'\s+', ' ', clean_text)
        except Exception as e:
            clean_text = ""
            
        tts_text = normalize_tts_text(clean_text)
        dur = round(len(normalized) / 1000.0, 2)
        
        speaker_records.append({
            "file_name": f"wavs/{file_name}",
            "speaker_id": speaker_id,
            "speaker_name": speaker_name,
            "gender": gender,
            "transcription": clean_text,
            "normalized_text": tts_text,
            "duration_seconds": dur,
            "source": url
        })
        print(f"   [{speaker_id}_{idx+1:04d}] ({dur}s): {clean_text[:50]}...")
        
    return speaker_records

def build_multispeaker_corpus():
    base_dir = os.path.join("audio_pipeline", "Punjabi-MultiSpeaker-Studio-TTS-Corpus")
    wavs_dir = os.path.join(base_dir, "wavs")
    os.makedirs(wavs_dir, exist_ok=True)
    os.makedirs(os.path.join("audio_pipeline", "raw_cache"), exist_ok=True)
    
    # 1. Load ASR
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"🧠 Loading Vakyansh Punjabi ASR on {device}...")
    asr = pipeline("automatic-speech-recognition", model="Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10", device=device)
    
    all_records = []
    
    # --- SPEAKER 1: Bhai Ranjit Singh (Dhadrianwale) from existing verified corpus ---
    print("\n🎙️ Converting Speaker 1 (Bhai Ranjit Singh) to 22,050Hz TTS format...")
    existing_meta_path = "audio_pipeline/Punjabi-Conversational-Speech-Corpus/metadata.csv"
    if os.path.exists(existing_meta_path):
        df_spk1 = pd.read_csv(existing_meta_path)
        for _, row in df_spk1.iterrows():
            src_wav = os.path.join("audio_pipeline/Punjabi-Conversational-Speech-Corpus", row["file_name"])
            if os.path.exists(src_wav):
                sound = AudioSegment.from_wav(src_wav)
                trimmed = trim_silence(sound, silence_thresh=-38)
                change_in_dBFS = -20.0 - trimmed.dBFS
                normalized = trimmed.apply_gain(change_in_dBFS).set_frame_rate(22050).set_channels(1)
                
                fname = os.path.basename(row["file_name"]).replace("clip_", "spk1_male_")
                dst_path = os.path.join(wavs_dir, fname)
                normalized.export(dst_path, format="wav")
                
                clean_text = row["transcription"]
                tts_text = normalize_tts_text(clean_text)
                dur = round(len(normalized) / 1000.0, 2)
                
                all_records.append({
                    "file_name": f"wavs/{fname}",
                    "speaker_id": "spk1_male_orator",
                    "speaker_name": "Bhai Ranjit Singh",
                    "gender": "male",
                    "transcription": clean_text,
                    "normalized_text": tts_text,
                    "duration_seconds": dur,
                    "source": row["source"]
                })
        print(f"   Converted {len(df_spk1)} clips for Speaker 1.")
        
    # --- SPEAKER 2: Dr. Surjit Patar (Male Literary / Poet) ---
    spk2_records = process_speaker(
        speaker_id="spk2_male_literary",
        speaker_name="Dr. Surjit Patar",
        gender="male",
        url="https://www.youtube.com/watch?v=aIWAq9kfj-U",
        output_wav_dir=wavs_dir,
        asr_pipeline=asr,
        duration_sec=300
    )
    all_records.extend(spk2_records)
    
    # --- SPEAKER 3: BBC Punjabi Female Broadcaster ---
    spk3_records = process_speaker(
        speaker_id="spk3_female_broadcaster",
        speaker_name="BBC Punjabi Broadcaster",
        gender="female",
        url="https://www.youtube.com/watch?v=yj8OHgeM_3k",
        output_wav_dir=wavs_dir,
        asr_pipeline=asr,
        duration_sec=300
    )
    all_records.extend(spk3_records)
    
    # Save unified metadata
    df = pd.DataFrame(all_records)
    csv_path = os.path.join(base_dir, "metadata.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8")
    
    parquet_path = os.path.join(base_dir, "train.parquet")
    df.to_parquet(parquet_path, index=False)
    
    total_dur = df["duration_seconds"].sum()
    print(f"\n🎉 MULTI-SPEAKER DATASET COMPLETE!")
    print(f"   Total Clips   : {len(df)}")
    print(f"   Total Duration: {round(total_dur/60.0, 1)} minutes")
    print(f"   Speakers      : {df['speaker_name'].unique().tolist()}")
    
    # Generate README
    readme_content = f"""---
license: apache-2.0
task_categories:
- text-to-speech
- automatic-speech-recognition
language:
- pa
tags:
- audio
- tts
- speech
- punjabi
- gurmukhi
- indic
- multi-speaker
- sovereign-ai
- amrit-research-os
- nam-toon-studio
size_categories:
- n<{max(1000, len(df))}
configs:
- config_name: default
  data_files:
  - split: train
    path: train.parquet
---

# ੴ Punjabi-MultiSpeaker-Studio-TTS-Corpus
## ☬ Multi-Speaker Punjabi Neural TTS Audio Corpus (ਪੰਜਾਬੀ ਮਲਟੀ-ਸਪੀਕਰ ਸਟੂਡੀਓ TTS ਡਾਟਾਸੈੱਟ)

Published by **[Nam-toon Studio](https://huggingface.co/Nam-toon-studio)** & **Gurpreet Singh** as part of sovereign Indic speech AI research under **AMRIT Research OS**.

### 📊 Dataset Summary
- **Total Audio Clips:** {len(df)} clips
- **Total Audio Duration:** ~{round(total_dur/60.0, 1)} minutes of high-resolution studio speech
- **Audio Specification:** 22,050 Hz, 16-bit Mono WAV, Normalized (-20 dBFS), Tight Silence Trimmed (<50ms)
- **Primary Language:** Punjabi (`pa`)
- **Primary Script:** Gurmukhi (ਗੁਰਮੁਖੀ)
- **Speakers:**
  1. `spk1_male_orator`: Bhai Ranjit Singh (Male, Conversational/Orator)
  2. `spk2_male_literary`: Dr. Surjit Patar (Male, Classical Literary/Poetic)
  3. `spk3_female_broadcaster`: BBC Punjabi Broadcaster (Female, Professional Studio Voice)

### 🗂️ Dataset Fields
- `file_name` (`string`): Relative path to audio clip in `wavs/`
- `speaker_id` (`string`): Unique speaker ID for multi-speaker conditioning
- `speaker_name` (`string`): Speaker identity
- `gender` (`string`): `male` / `female`
- `transcription` (`string`): Gurmukhi transcription
- `normalized_text` (`string`): Phonetically expanded text (numbers converted to Punjabi words for TTS)
- `duration_seconds` (`float`): Duration in seconds
- `source` (`string`): Audio reference URL

### 🚀 Usage for Piper & VITS Training
```python
from datasets import load_dataset

dataset = load_dataset("Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus")
print(dataset["train"][0])
```
"""
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✅ README.md created at {os.path.join(base_dir, 'README.md')}")

if __name__ == "__main__":
    build_multispeaker_corpus()

