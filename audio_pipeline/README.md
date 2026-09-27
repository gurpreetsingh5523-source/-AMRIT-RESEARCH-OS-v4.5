# 🎙️ Punjabi Spoken Audio & Speech Dataset Pipeline
### YouTube to Hugging Face Automated Corpus Builder (AMRIT Research OS)

This pipeline automates the end-to-end extraction, segmentation, loudness normalization, transcription, and Hugging Face publishing of spoken Punjabi speech from YouTube.

```
YouTube Video (URL)
      │
      ▼  [yt-dlp with android/ios client fallback]
16kHz Mono Master Audio (.wav)
      │
      ▼  [VAD Silence Slicing (pydub, 3s - 12s)]
Normalized Speech Chunks (-20 dBFS)
      │
      ▼  [Harveenchadha/vakyansh-wav2vec2-punjabi-pam-10 on Apple Silicon GPU / CUDA]
Pure Gurmukhi Transcriptions
      │
      ▼  [Hugging Face Hub API]
Live Dataset on Hugging Face (AudioFolder + metadata.csv + train.parquet)
```

---

### 🚀 Usage

#### 1. Generate & Upload Dataset
```bash
python3 audio_pipeline/youtube_punjabi_audio_pipeline.py \
  --url "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" \
  --repo "Punjabi-Conversational-Speech-Corpus" \
  --speaker "Speaker Name" \
  --duration 600 \
  --engine "vakyansh" \
  --upload
```

#### 2. Arguments
- `--url`: YouTube video URL.
- `--repo`: Target Hugging Face dataset name under `Nam-toon-studio/`.
- `--speaker`: Speaker name or discourse topic.
- `--duration`: Number of seconds to process (e.g., 600 for 10 minutes).
- `--engine`: `vakyansh` (High accuracy Gurmukhi, default) or `whisper`.
- `--upload`: Automatically creates and publishes dataset to Hugging Face.

---

### 🌐 Published Datasets
- **[Nam-toon-studio/Punjabi-Conversational-Speech-Corpus](https://huggingface.co/datasets/Nam-toon-studio/Punjabi-Conversational-Speech-Corpus)**: 
  - **91 verified 16kHz mono speech clips** (~16.5 minutes total audio).
  - Includes both `transcription` (100% human-verified, grammatically curated Gurmukhi) and `raw_transcription` (unprocessed CTC acoustic ASR output).
  - Speaker: Bhai Ranjit Singh (Dhadrianwale) on Mind-Body connection, health, and lifestyle.
- **[Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus](https://huggingface.co/datasets/Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus)**:
  - **217 high-fidelity studio clips** (22,050Hz mono, 33.2 minutes total audio).
  - 4 Distinct Sovereign Speakers:
    - `0`: **Bhai Ranjit Singh** (Male Orator / Conversational / Mind-Body) — 91 clips
    - `1`: **Dr. Surjit Patar** (Male Literary / Classical Poetry) — 58 clips
    - `2`: **BBC Punjabi Broadcaster** (Female Broadcaster / News) — 33 clips
    - `3`: **Bilingual Tech Orator** (Bilingual AI & Science Discourse) — 35 clips

---

### 🎙️ AMRIT Multi-Speaker Bilingual Voice Engine (`amrit_voice_system.py`)

A sovereign, universal neural speech engine that anyone can run locally for pure Gurmukhi and code-mixed Punjabi-English text.

#### 1. List Available Speakers
```bash
python3 audio_pipeline/amrit_voice_system.py --list-speakers
```

#### 2. Speak with Any Sovereign Voice
```bash
# Speaker 0: Bhai Ranjit Singh (Male Orator)
python3 audio_pipeline/amrit_voice_system.py --speaker 0 --text "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ ਜੀ, ਤਨ ਤੇ ਮਨ ਦਾ ਗਹਿਰਾ ਸੰਬੰਧ ਹੈ।"

# Speaker 1: Dr. Surjit Patar (Male Literary / Poet)
python3 audio_pipeline/amrit_voice_system.py --speaker 1 --text "ਕੋਈ ਡਾਲੀਆਂ ਚੋਂ ਲੰਘਿਆ ਹਵਾ ਬਣ ਕੇ, ਅਸੀਂ ਰਹਿ ਗਏ ਕੁਲਾਂ ਦੇ ਪੈਰ ਚੁੰਮਦੇ।"

# Speaker 2: BBC Punjabi (Female Broadcaster)
python3 audio_pipeline/amrit_voice_system.py --speaker 2 --text "ਬੀ.ਬੀ.ਸੀ. ਪੰਜਾਬੀ ਤੇ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ, ਅੱਜ ਦੀਆਂ ਮੁੱਖ ਖ਼ਬਰਾਂ ਸੁਣੋ।"

# Speaker 3: Bilingual Tech Orator (Punjabi + English AI)
python3 audio_pipeline/amrit_voice_system.py --speaker 3 --text "ਅੰਮ੍ਰਿਤ ਰਿਸਰਚ ਓ.ਐਸ. ਵਿੱਚ ਆਰਟੀਫਿਸ਼ੀਅਲ ਇੰਟੈਲੀਜੈਂਸ ਅਤੇ ਕੰਪਿਊਟਰ ਸਾਇੰਸ ਦੀ ਬਿਹਤਰੀਨ ਟੈਕਨਾਲੋਜੀ ਹੈ।"
```

#### 3. Neural Model Training
```bash
# Train on Apple Silicon GPU (MPS) with your multi-speaker dataset:
python3 audio_pipeline/train_amrit_voice_system.py --epochs 12 --batch-size 8
```

