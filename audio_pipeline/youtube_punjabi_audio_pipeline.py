#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Punjabi Speech & Audio Dataset Builder (YouTube to Hugging Face)
Architected for Nam-toon Studio & AMRIT Research OS
by Gurpreet Singh

Pipeline:
1. Download audio from YouTube via yt-dlp (16kHz Mono WAV)
2. Segment speech into clean 3-12 second clips via VAD (Silence Detection)
3. Normalize loudness to standard -20 dBFS
4. Auto-transcribe using Whisper
5. Build standard Hugging Face AudioFolder + metadata.csv + train.parquet
6. Push directly to Nam-toon-studio on Hugging Face
"""

import os
import sys
import argparse
import yt_dlp
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pandas as pd
import whisper
from huggingface_hub import HfApi, create_repo

def download_youtube_audio(url: str, output_path: str, max_duration_sec: int = 600) -> str:
    """Download audio stream from YouTube, resample to 16kHz mono WAV."""
    print(f"📥 Downloading audio from YouTube: {url}")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path.replace('.wav', '.%(ext)s'),
        'extractor_args': {'youtube': {'player_client': ['android', 'ios']}},
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'postprocessor_args': ['-ar', '16000', '-ac', '1'],
        'quiet': False
    }
    
    if max_duration_sec > 0:
        ydl_opts['download_ranges'] = yt_dlp.utils.download_range_func(None, [(0, max_duration_sec)])
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    final_wav = output_path if output_path.endswith('.wav') else output_path + '.wav'
    if not os.path.exists(final_wav):
        # find the converted wav file
        base = os.path.splitext(output_path)[0]
        if os.path.exists(base + '.wav'):
            final_wav = base + '.wav'
    print(f"✅ Audio downloaded and extracted to: {final_wav}")
    return final_wav


def slice_into_speech_clips(
    wav_path: str,
    output_dir: str,
    min_clip_len_ms: int = 3000,
    max_clip_len_ms: int = 12000,
    silence_thresh: int = -34,
    min_silence_len: int = 350
) -> list:
    """Slice continuous audio into clean speech chunks between 3s and 12s."""
    print(f"✂️ Slicing speech into clean chunks (VAD silence threshold: {silence_thresh} dBFS)...")
    os.makedirs(output_dir, exist_ok=True)
    sound = AudioSegment.from_wav(wav_path)
    total_dur_sec = len(sound) / 1000.0
    print(f"   Audio Duration: {total_dur_sec:.1f}s")
    
    raw_chunks = split_on_silence(
        sound,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
        keep_silence=200
    )
    print(f"   Detected {len(raw_chunks)} raw speech segments")
    
    merged_clips = []
    current_clip = None
    for chunk in raw_chunks:
        if current_clip is None:
            current_clip = chunk
        elif len(current_clip) + len(chunk) <= max_clip_len_ms:
            current_clip += chunk
        else:
            if len(current_clip) >= min_clip_len_ms:
                merged_clips.append(current_clip)
            current_clip = chunk
    if current_clip and len(current_clip) >= min_clip_len_ms:
        merged_clips.append(current_clip)
        
    saved_clips = []
    print(f"   Saving {len(merged_clips)} normalized clips...")
    for idx, clip in enumerate(merged_clips):
        # Normalize volume to -20 dBFS
        change_in_dBFS = -20.0 - clip.dBFS
        normalized_clip = clip.apply_gain(change_in_dBFS)
        
        file_name = f"clip_{idx+1:04d}.wav"
        rel_path = os.path.join("data", file_name)
        full_path = os.path.join(output_dir, file_name)
        normalized_clip.export(full_path, format="wav")
        saved_clips.append({
            "file_name": rel_path,
            "full_path": full_path,
            "duration": round(len(clip) / 1000.0, 2)
        })
        
    print(f"✅ Created {len(saved_clips)} clean audio clips in: {output_dir}")
    return saved_clips


def transcribe_clips(clips: list, engine: str = "vakyansh") -> list:
    """Transcribe audio clips using high-accuracy Gurmukhi Punjabi ASR."""
    print(f"🧠 Transcribing {len(clips)} audio clips using engine: {engine}...")
    
    if engine == "vakyansh":
        import re
        from transformers import pipeline
        import torch
        device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"   Loading Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10 on {device}...")
        asr = pipeline("automatic-speech-recognition", model="Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10", device=device)
        
        for idx, item in enumerate(clips):
            try:
                res = asr(item["full_path"])
                raw_text = res.get("text", "")
                clean_text = re.sub(r'</?s>', '', raw_text).strip()
                clean_text = re.sub(r'\s+', ' ', clean_text)
                item["transcription"] = clean_text
            except Exception as e:
                print(f"   ⚠️ Error transcribing clip {idx+1}: {e}")
                item["transcription"] = ""
            print(f"   [{idx+1}/{len(clips)}] {item['file_name']} ({item['duration']}s): {item['transcription']}")
            
    elif engine == "whisper":
        import whisper
        print(f"   Loading OpenAI Whisper...")
        model = whisper.load_model("base")
        for idx, item in enumerate(clips):
            try:
                res = model.transcribe(item["full_path"], language="pa", temperature=0.0)
                item["transcription"] = res.get("text", "").strip()
            except Exception as e:
                print(f"   ⚠️ Error transcribing clip {idx+1}: {e}")
                item["transcription"] = ""
            print(f"   [{idx+1}/{len(clips)}] {item['file_name']} ({item['duration']}s): {item['transcription']}")
            
    return clips


def build_huggingface_dataset(
    dataset_dir: str,
    clips: list,
    repo_name: str,
    speaker: str = "Punjabi Speaker",
    source_url: str = ""
):
    """Generate metadata.csv, train.parquet, and README dataset card."""
    print("📦 Generating Hugging Face Dataset files...")
    data_dir = os.path.join(dataset_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    records = []
    for c in clips:
        records.append({
            "file_name": c["file_name"],
            "transcription": c.get("transcription", ""),
            "duration_seconds": c["duration"],
            "speaker": speaker,
            "language": "pa",
            "script": "Gurmukhi",
            "source": source_url
        })
        
    df = pd.DataFrame(records)
    metadata_csv = os.path.join(dataset_dir, "metadata.csv")
    df.to_csv(metadata_csv, index=False, encoding="utf-8")
    
    parquet_path = os.path.join(dataset_dir, "train.parquet")
    df.to_parquet(parquet_path, index=False)
    print(f"✅ metadata.csv and train.parquet generated with {len(df)} entries.")
    
    # Dataset Card README.md
    readme_content = f"""---
license: apache-2.0
task_categories:
- automatic-speech-recognition
- text-to-speech
language:
- pa
tags:
- audio
- speech
- punjabi
- gurmukhi
- indic
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

# ੴ {repo_name}
## ☬ Punjabi Speech & Audio Corpus (ਪੰਜਾਬੀ ਆਡੀਓ ਡਾਟਾਸੈੱਟ)

Published by **[Nam-toon Studio](https://huggingface.co/Nam-toon-studio)** & **Gurpreet Singh** as part of sovereign Indic speech AI research under **AMRIT Research OS**.

### 📊 Dataset Summary
- **Total Audio Clips:** {len(df)}
- **Audio Specification:** 16,000 Hz, 16-bit Mono WAV, Normalized (-20 dBFS)
- **Primary Language:** Punjabi (`pa`)
- **Primary Script:** Gurmukhi (ਗੁਰਮੁਖੀ)
- **Speaker / Source:** {speaker}
- **Source Reference:** [{source_url}]({source_url})
- **Annotation Pipeline:** VAD Silence Segmentation (3s - 12s) + Vakyansh Punjabi Acoustic Model

### 🗂️ Dataset Structure
```text
{repo_name}/
├── data/
│   ├── clip_0001.wav
│   ├── clip_0002.wav
│   └── ...
├── metadata.csv
├── train.parquet
└── README.md
```

### 🚀 Usage with Hugging Face Datasets
```python
from datasets import load_dataset

dataset = load_dataset("Nam-toon-studio/{repo_name}")
print(dataset["train"][0])
```

### 📜 Citation & Credits
If you use this dataset in your speech synthesis (TTS) or automatic speech recognition (ASR) research, please credit:
```bibtex
@dataset{{namtoon_{repo_name.lower().replace('-', '_')},
  author = {{Gurpreet Singh (Nam-toon Studio)}},
  title = {{{repo_name}: High-Quality Spoken Punjabi Gurmukhi Audio Corpus}},
  year = {{2026}},
  publisher = {{Hugging Face}},
  url = {{https://huggingface.co/datasets/Nam-toon-studio/{repo_name}}}
}}
```
"""
    readme_path = os.path.join(dataset_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✅ README.md dataset card created.")


def upload_to_huggingface(dataset_dir: str, repo_id: str):
    """Upload dataset directory directly to Hugging Face Hub."""
    print(f"🚀 Uploading dataset to Hugging Face: {repo_id} ...")
    api = HfApi()
    
    # Create repository if it doesn't exist
    try:
        create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)
        print(f"✅ Hugging Face repository confirmed: https://huggingface.co/datasets/{repo_id}")
    except Exception as e:
        print(f"ℹ️ Repo status: {e}")
        
    api.upload_folder(
        folder_path=dataset_dir,
        repo_id=repo_id,
        repo_type="dataset"
    )
    print(f"\n🎉 ਧੰਨਵਾਦ! Dataset is now LIVE at: https://huggingface.co/datasets/{repo_id}")


def main():
    parser = argparse.ArgumentParser(description="YouTube to Hugging Face Punjabi Audio Dataset")
    parser.add_argument("--url", type=str, required=True, help="YouTube Video URL")
    parser.add_argument("--repo", type=str, default="Punjabi-Speech-Voices-Corpus", help="Hugging Face Dataset repo name")
    parser.add_argument("--speaker", type=str, default="Punjabi Speaker", help="Speaker name or topic")
    parser.add_argument("--duration", type=int, default=300, help="Max duration in seconds to process (default 300 = 5 mins)")
    parser.add_argument("--engine", type=str, default="vakyansh", choices=["vakyansh", "whisper"], help="ASR Engine (default: vakyansh for clean Gurmukhi)")
    parser.add_argument("--upload", action="store_true", help="Automatically upload to Hugging Face")
    args = parser.parse_args()
    
    base_dir = os.path.join("audio_pipeline", args.repo)
    # Put raw audio in a scratch cache directory outside the repo folder so it is not pushed to HF
    raw_cache_dir = os.path.join("audio_pipeline", "raw_cache")
    os.makedirs(raw_cache_dir, exist_ok=True)
    raw_audio = os.path.join(raw_cache_dir, f"{args.repo}_raw.wav")
    data_dir = os.path.join(base_dir, "data")
    
    # 1. Download
    wav_path = download_youtube_audio(args.url, raw_audio, max_duration_sec=args.duration)
    
    # 2. Slice
    clips = slice_into_speech_clips(wav_path, data_dir)
    
    # 3. Transcribe
    clips = transcribe_clips(clips, engine=args.engine)
    
    # 4. Package
    build_huggingface_dataset(
        dataset_dir=base_dir,
        clips=clips,
        repo_name=args.repo,
        speaker=args.speaker,
        source_url=args.url
    )
    
    # 5. Upload if requested
    if args.upload:
        full_repo_id = f"Nam-toon-studio/{args.repo}"
        upload_to_huggingface(base_dir, full_repo_id)

if __name__ == "__main__":
    main()
