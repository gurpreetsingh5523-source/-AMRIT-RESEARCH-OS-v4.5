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
## ☬ Punjabi Speech & Audio Corpus (ਪੰਜਾਬੀ ਆਡੀਓ ਡਾਟਾਸੈੱਟ)

Published by **[Nam-toon Studio](https://huggingface.co/Nam-toon-studio)** & **Gurpreet Singh** as part of sovereign Indic speech AI research under **AMRIT Research OS**.

### 📊 Dataset Summary
- **Total Audio Clips:** 60
- **Audio Specification:** 16,000 Hz, 16-bit Mono WAV, Normalized (-20 dBFS)
- **Primary Language:** Punjabi (`pa`)
- **Primary Script:** Gurmukhi (ਗੁਰਮੁਖੀ)
- **Speaker / Source:** Bhai Ranjit Singh (Dhadrianwale)
- **Source Reference:** [https://www.youtube.com/watch?v=t6wXJUD4p40](https://www.youtube.com/watch?v=t6wXJUD4p40)
- **Annotation Pipeline:** VAD Silence Segmentation (3s - 12s) + Vakyansh Punjabi Acoustic Model

### 🗂️ Dataset Structure
```text
Punjabi-Conversational-Speech-Corpus/
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

dataset = load_dataset("Nam-toon-studio/Punjabi-Conversational-Speech-Corpus")
print(dataset["train"][0])
```

### 📜 Citation & Credits
If you use this dataset in your speech synthesis (TTS) or automatic speech recognition (ASR) research, please credit:
```bibtex
@dataset{namtoon_punjabi_conversational_speech_corpus,
  author = {Gurpreet Singh (Nam-toon Studio)},
  title = {Punjabi-Conversational-Speech-Corpus: High-Quality Spoken Punjabi Gurmukhi Audio Corpus},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/Nam-toon-studio/Punjabi-Conversational-Speech-Corpus}
}
```
