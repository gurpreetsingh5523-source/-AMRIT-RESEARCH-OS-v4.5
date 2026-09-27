---
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
- n<1000
configs:
- config_name: default
  data_files:
  - split: train
    path: train.parquet
---

# ੴ Punjabi-Conversational-Speech-Corpus
## ☬ High-Precision Spoken Punjabi Gurmukhi Audio Corpus (ਪੰਜਾਬੀ ਸੰਵਾਦ ਅਤੇ ਭਾਸ਼ਣ ਆਡੀਓ ਕਾਰਪਸ)

Published by **[Nam-toon Studio](https://huggingface.co/Nam-toon-studio)** & **Gurpreet Singh** as part of sovereign Indic speech AI research under **AMRIT Research OS**.

### 📊 Dataset Summary
- **Total Audio Clips:** 91 verified clips
- **Total Audio Duration:** ~15.3 minutes of continuous conversational speech
- **Audio Specification:** 16,000 Hz, 16-bit Mono WAV, Normalized (-20 dBFS)
- **Primary Language:** Punjabi (`pa`)
- **Primary Script:** Gurmukhi (ਗੁਰਮੁਖੀ)
- **Speaker:** Bhai Ranjit Singh (Dhadrianwale)
- **Topic:** Mind-Body Connection, Subconscious Mind, Health, Mindfulness & Diet (ਮਨ ਅਤੇ ਸਰੀਰ ਦਾ ਸੰਬੰਧ, ਸਿਹਤ ਅਤੇ ਆਹਾਰ)
- **Source Reference:** [https://www.youtube.com/watch?v=t6wXJUD4p40](https://www.youtube.com/watch?v=t6wXJUD4p40)
- **Curation Method (ਸਹੀ ਕਰਨ ਵਾਲੀ ਵਿਧੀ):**
  1. VAD Silence-based speech segmentation (3s - 12s clean chunks).
  2. Vakyansh Wav2Vec2 CTC Acoustic Speech-to-Text inference.
  3. Context-aware Gurmukhi post-processing: loan-word normalization, phonetic typo repair, sub-character Unicode restoration, and punctuation alignment.

### 🗂️ Dataset Fields
- `file_name` (`string`): Relative path to audio clip in `data/`
- `transcription` (`string`): Fully curated, grammatically verified Gurmukhi text
- `raw_transcription` (`string`): Raw CTC acoustic ASR output (useful for ASR benchmark / post-editing research)
- `duration_seconds` (`float`): Duration of speech clip in seconds
- `speaker` (`string`): Speaker identity
- `language` (`string`): Language code (`pa`)
- `script` (`string`): Script (`Gurmukhi`)
- `source` (`string`): YouTube source URL

### 🚀 Usage with Hugging Face Datasets
```python
from datasets import load_dataset

dataset = load_dataset("Nam-toon-studio/Punjabi-Conversational-Speech-Corpus")
print(dataset["train"][0])
```

### 📜 Citation & Credits
```bibtex
@dataset{namtoon_punjabi_conversational_speech_corpus,
  author = {Gurpreet Singh (Nam-toon Studio)},
  title = {Punjabi-Conversational-Speech-Corpus: High-Precision Spoken Punjabi Gurmukhi Audio Corpus},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/Nam-toon-studio/Punjabi-Conversational-Speech-Corpus}
}
```
