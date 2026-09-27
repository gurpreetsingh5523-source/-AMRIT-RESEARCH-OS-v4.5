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
  - **145 high-fidelity studio clips** (22,050Hz mono, 22.8 minutes total audio).
  - Multi-speaker voices: Bhai Ranjit Singh, Dr. Surjit Patar, BBC Punjabi Broadcaster.

---

### 🔊 Sovereign Punjabi Neural TTS (Text-to-Speech)
- **Model on Hugging Face**: **[Nam-toon-studio/punjabi-tts-voices](https://huggingface.co/Nam-toon-studio/punjabi-tts-voices)**
- **Architecture**: 114MB VITS Gurmukhi Neural Synthesis Engine (ONNX).
- **Run & Play Punjabi Speech via Speakers**:
```bash
# Generate Punjabi speech and listen immediately:
python3 audio_pipeline/test_and_play_tts.py --text "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ ਜੀ, ਅੰਮ੍ਰਿਤ ਰਿਸਰਚ ਓ.ਐਸ. ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ।"

# Download directly from Hugging Face Hub and play:
python3 audio_pipeline/test_and_play_tts.py --download-hf --text "ਪੰਜਾਬੀ ਬੋਲਣ ਵਾਲਾ ਮਾਡਲ ਹੁਣ ਪੂਰੀ ਤਰ੍ਹਾਂ ਤਿਆਰ ਹੈ।"
```

