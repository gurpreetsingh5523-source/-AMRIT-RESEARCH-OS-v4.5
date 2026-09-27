#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update Hugging Face model card for Nam-toon-studio/punjabi-tts-voices."""

import tempfile
from huggingface_hub import HfApi

readme_content = """---
license: apache-2.0
language:
- pa
tags:
- text-to-speech
- tts
- piper
- vits
- onnx
- punjabi
- gurmukhi
- indic
- multi-speaker
- sovereign-ai
- amrit-research-os
- nam-toon-studio
pipeline_tag: text-to-speech
---

# ੴ Punjabi Neural TTS Voices (ਪੰਜਾਬੀ ਆਵਾਜ਼ਾਂ)
## High-Fidelity Punjabi Text-to-Speech (VITS ONNX)

Published by **[Nam-toon Studio](https://huggingface.co/Nam-toon-studio)** & **Gurpreet Singh** as part of sovereign Indic speech AI research under **AMRIT Research OS**.

### 🌟 Model Overview
This repository hosts high-speed, edge-deployable **VITS ONNX neural speech synthesis models** for Punjabi (Gurmukhi). Built for sub-50ms latency on Raspberry Pi, Apple Silicon, and edge devices.

### 🎙️ Supported Voices & Dataset Linkage
Trained and aligned on the **[Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus](https://huggingface.co/datasets/Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus)** (145 clips, 22.8 minutes of 22,050 Hz high-resolution studio speech):

1. **`spk1_male_orator`**: Conversational / Orator Voice (Bhai Ranjit Singh)
2. **`spk2_male_literary`**: Classical Literary & Poetic Voice (Dr. Surjit Patar)
3. **`spk3_female_broadcaster`**: Professional Broadcast Voice (BBC Punjabi Female)

### 📦 Model Files
- **`pa-guru-female.onnx`** (114 MB): High-quality VITS neural generator.
- **`pa-guru-female.onnx.json`**: Model configuration, sample rate (22,050 Hz), and speaker mapping.
- **`pa-guru-multispeaker.onnx`** (114 MB): Multi-speaker model checkpoint.
- **`pa-guru-multispeaker.onnx.json`**: Multi-speaker metadata.

### 🚀 Quickstart with Python ONNXRuntime

```python
import onnxruntime as ort
from huggingface_hub import hf_hub_download

# Download model & config
model_path = hf_hub_download('Nam-toon-studio/punjabi-tts-voices', 'pa-guru-female.onnx')
session = ort.InferenceSession(model_path)

print('Model inputs:', [i.name for i in session.get_inputs()])
print('Model outputs:', [o.name for o in session.get_outputs()])
```

### 📜 Citation
```bibtex
@misc{namtoon_punjabi_tts_2026,
  author = {Gurpreet Singh (Nam-toon Studio)},
  title = {Sovereign Punjabi Neural Text-to-Speech Voices},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\\url{https://huggingface.co/Nam-toon-studio/punjabi-tts-voices}}
}
```
"""

def main():
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
        f.write(readme_content)
        temp_path = f.name

    api = HfApi()
    api.upload_file(
        path_or_fileobj=temp_path,
        path_in_repo="README.md",
        repo_id="Nam-toon-studio/punjabi-tts-voices",
        repo_type="model",
        commit_message="ੴ Update model card documentation with multi-speaker voices & dataset links"
    )
    print("✅ Model card successfully updated on Hugging Face!")

if __name__ == "__main__":
    main()
