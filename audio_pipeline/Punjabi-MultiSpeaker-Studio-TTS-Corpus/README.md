---
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
- n<1000
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
- **Total Audio Clips:** 145 clips
- **Total Audio Duration:** ~22.8 minutes of high-resolution studio speech
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
