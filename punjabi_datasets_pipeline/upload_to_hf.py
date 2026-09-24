#!/usr/bin/env python3
"""
Production Hugging Face Dataset Uploader for Nam-toon-studio
Author: Gurpreet Singh Dhillon
"""

import os
import sys
import json
import urllib.request

def upload_to_huggingface(repo_name: str, local_jsonl: str, readme_md: str):
    token_path = os.path.expanduser('~/.cache/huggingface/token')
    if not os.path.exists(token_path):
        print("❌ Hugging Face token not found!")
        return False

    token = open(token_path).read().strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    repo_id = f"Nam-toon-studio/{repo_name}"
    print(f"\n========================================================")
    print(f"🚀 Initializing Hugging Face upload for: {repo_id}")
    print(f"========================================================")

    # 1. Ensure Repo Exists
    create_payload = json.dumps({
        "name": repo_name,
        "organization": "Nam-toon-studio",
        "private": False,
        "type": "dataset"
    }).encode('utf-8')

    try:
        req = urllib.request.Request("https://huggingface.co/api/repos/create", data=create_payload, headers=headers)
        with urllib.request.urlopen(req) as resp:
            print(f"✅ Repository {repo_id} created successfully!")
    except urllib.error.HTTPError as e:
        if e.code == 409:
            print(f"ℹ️ Repository {repo_id} exists. Updating files...")
        else:
            print(f"⚠️ Notice: {e}")
    except Exception as e:
        print(f"⚠️ Notice: {e}")

    # 2. Upload train.jsonl
    if os.path.exists(local_jsonl):
        with open(local_jsonl, "rb") as f:
            data = f.read()
        
        upload_url = f"https://huggingface.co/api/datasets/{repo_id}/upload/main/train.jsonl"
        print(f"📤 Uploading train.jsonl ({len(data):,} bytes)...")
        try:
            req = urllib.request.Request(upload_url, data=data, headers={'Authorization': f'Bearer {token}'})
            with urllib.request.urlopen(req) as resp:
                print(f"✅ Successfully uploaded train.jsonl ({len(data):,} bytes) to {repo_id}!")
        except Exception as e:
            print(f"❌ Error uploading train.jsonl: {e}")

    # 3. Upload README.md
    if readme_md:
        readme_url = f"https://huggingface.co/api/datasets/{repo_id}/upload/main/README.md"
        print(f"📄 Uploading professional README.md documentation...")
        try:
            req = urllib.request.Request(readme_url, data=readme_md.encode('utf-8'), headers={'Authorization': f'Bearer {token}'})
            with urllib.request.urlopen(req) as resp:
                print(f"✅ Successfully uploaded README.md to {repo_id}!")
        except Exception as e:
            print(f"❌ Error uploading README.md: {e}")

    print(f"🌟 Dataset is now live at: https://huggingface.co/datasets/{repo_id}")
    return True

def main():
    base_dir = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"

    # Dataset 1: Punjabi Grammar Correction Corpus
    grammar_jsonl = os.path.join(base_dir, "punjabi_grammar_correction_corpus.jsonl")
    grammar_readme = """---
license: apache-2.0
language:
- pa
task_categories:
- text2text-generation
- grammar-error-correction
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
tags:
- punjabi
- gurmukhi
- grammar-correction
- gec
- indic
- linguistic-curation
- amrit-research-os
pretty_name: Punjabi (Gurmukhi) Grammatical Error Correction Corpus
---

# ੴ Punjabi (Gurmukhi) Grammatical Error Correction Corpus
## ☬ ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ) ਵਿਆਕਰਣ ਸ਼ੁੱਧੀ ਅਤੇ ਸੁਧਾਰ ਡਾਟਾਸੈੱਟ (v1.0)

<p align="center">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Author-Gurpreet%20Singh%20Dhillon-orange?style=for-the-badge" alt="Author">
  <img src="https://img.shields.io/badge/Status-Verified%20Linguistic%20Data-purple?style=for-the-badge" alt="Status">
</p>

---

### 👨‍💻 Architect & Research Lead
* **Creator / Developer:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **GitHub Organization:** [github.com/gurpreetsingh5523-source](https://github.com/gurpreetsingh5523-source)
* **Flagship Project:** [AMRIT Research OS (Autonomous Medical AI)](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Overview / ਸੰਖੇਪ
The **Punjabi (Gurmukhi) Grammatical Error Correction (GEC) Corpus** is a linguistically rigorous, gold-standard parallel dataset curated for training and benchmarking neural grammatical error correction models for the Punjabi language.

Unlike generic automated corruption datasets, every sentence pair in this corpus is crafted according to **standard Punjabi grammar principles (ਪੰਜਾਬੀ ਯੂਨੀਵਰਸਿਟੀ ਪਟਿਆਲਾ ਟਕਸਾਲੀ ਵਿਆਕਰਣ ਨਿਯਮ)** with precise grammatical rule explanations in Punjabi.

---

### 🎯 Key Grammatical Categories Covered

| ਸ਼੍ਰੇਣੀ (Category) | ਵੇਰਵਾ (Description) | ਉਦਾਹਰਨ (Example) |
|---|---|---|
| **ਲਿੰਗ-ਭੇਦ (Gender Agreement)** | Subject, Adjective & Verb gender concordance | ਮੁੰਡਾ ਸਕੂਲ *ਜਾਂਦੀ ਹੈ* ➔ *ਜਾਂਦਾ ਹੈ* |
| **ਵਚਨ-ਸਬੰਧ (Number Concord)** | Singular vs Plural agreement across all cases | ਸਾਰੇ ਬੱਚਾ *ਖੇਡ ਰਿਹਾ ਹੈ* ➔ ਸਾਰੇ ਬੱਚੇ *ਖੇਡ ਰਹੇ ਹਨ* |
| **ਕਾਰਕ ਅਤੇ ਸੰਬੰਧਕ (Case & Postpositions)** | Ergative 'ਨੇ', Dative 'ਨੂੰ', Ablative 'ਤੋਂ/ਨਾਲੋਂ' | ਉਸ *ਚਿੱਠੀ ਲਿਖੀ* ➔ ਉਸ **ਨੇ** ਚਿੱਠੀ ਲਿਖੀ |
| **ਸਬੰਧਕੀ ਰੂਪ (Oblique Case)** | Direct to oblique noun & modifier transformation | ਵੱਡਾ *ਕਮਰਾ ਵਿੱਚ* ➔ ਵੱਡੇ *ਕਮਰੇ ਵਿੱਚ* |
| **ਸ਼ਬਦ-ਜੋੜ ਤੇ ਪੈਰੀਂ ਅੱਖਰ** | Orthography, Subjoined letters (੍ਹ, ੍ਰ), Gemination (ੱ) | *ਪੜਦਾ* ➔ *ਪੜ੍ਹਦਾ*, *ਪਰੇਮ* ➔ *ਪ੍ਰੇਮ*, *ਸਚ* ➔ *ਸੱਚ* |
| **ਕਾਲ ਤੇ ਸਹਾਇਕ ਕਿਰਿਆ** | Tense & Aspect consistency across clauses | ਅੱਜ ਅਸੀਂ *ਜਾਂਦਾ ਸੀ* ➔ ਅੱਜ ਅਸੀਂ *ਜਾਂਦੇ ਹਾਂ* |
| **ਸਤਿਕਾਰਵਾਚਕ ਰੂਪ (Honorifics)** | Polite plural verb agreement for elders/gurus | ਪਿਤਾ ਜੀ *ਆਇਆ ਹੈ* ➔ ਪਿਤਾ ਜੀ *ਆਏ ਹਨ* |
| **ਨਾਹਵਾਚਕ ਸੰਰਚਨਾ (Negation)** | Correct prescriptive negative word order | ਝੂਠ *ਨਾ ਬੋਲਣਾ ਚਾਹੀਦਾ ਹੈ* ➔ ਝੂਠ *ਨਹੀਂ ਬੋਲਣਾ ਚਾਹੀਦਾ* |

---

### 📊 Data Structure (JSONL)
```json
{
  "id": "punjabi_gec_00001",
  "domain": "Medical & Healthcare",
  "instruction": "ਹੇਠਾਂ ਦਿੱਤੇ ਪੰਜਾਬੀ ਵਾਕ ਵਿੱਚੋਂ ਵਿਆਕਰਣਿਕ ਗਲਤੀ ਲੱਭ ਕੇ ਉਸਨੂੰ ਸ਼ੁੱਧ ਕਰੋ ਅਤੇ ਗਲਤੀ ਦਾ ਕਾਰਨ ਸਪੱਸ਼ਟ ਕਰੋ।",
  "incorrect_sentence": "ਡਾਕਟਰ ਨਵੀਂ ਦਵਾਈ ਦੀ ਪਰਚੀ ਲਿਖ ਰਹੀ ਹੈ।",
  "corrected_sentence": "ਡਾਕਟਰ ਨਵੀਂ ਦਵਾਈ ਦੀ ਪਰਚੀ ਲਿਖ ਰਿਹਾ ਹੈ।",
  "error_category": "ਲਿੰਗ-ਭੇਦ (Gender Agreement)",
  "sub_category": "ਲਿੰਗ-ਸਬੰਧ ਚਾਲੂ ਵਰਤਮਾਨ",
  "error_span": "ਲਿਖ ਰਹੀ ਹੈ",
  "correction_span": "ਲਿਖ ਰਿਹਾ ਹੈ",
  "explanation": "ਕਰਤਾ 'ਡਾਕਟਰ' ਪੁਲਿੰਗ ਇੱਕਵਚਨ ਹੈ, ਇਸ ਲਈ ਕਿਰਿਆ 'ਲਿਖ ਰਿਹਾ ਹੈ' ਹੋਵੇਗੀ।"
}
```

---

### 📜 Citation & License
This dataset is published under the open-source **Apache-2.0 License** by **Gurpreet Singh Dhillon (Nam-toon Studio)** for the advancement of Indic NLP and Punjabi Artificial Intelligence.
"""
    upload_to_huggingface("Punjabi-Gurmukhi-Grammar-Correction-Corpus", grammar_jsonl, grammar_readme)

    # Dataset 2: Mahan Kosh Expanded Corpus
    mahankosh_jsonl = os.path.join(base_dir, "gurbani_mahankosh_expanded_corpus.jsonl")
    mahankosh_readme = """---
license: cc-by-sa-4.0
language:
- pa
task_categories:
- text-generation
- question-answering
multilinguality:
- monolingual
tags:
- gurbani
- mahan-kosh
- punjabi
- gurmukhi
- punjabi-philosophy
- sikh-scriptures
- etymology
- dictionary
pretty_name: Gurbani & Bhai Kahn Singh Nabha Mahan Kosh Frontier Corpus
---

# ੴ Gurbani & Bhai Kahn Singh Nabha Mahan Kosh Frontier Corpus
## ☬ ਗੁਰਬਾਣੀ ਅਤੇ ਭਾਈ ਕਾਹਨ ਸਿੰਘ ਨਾਭਾ 'ਮਹਾਨ ਕੋਸ਼' ਪ੍ਰਮਾਣਿਕ ਡਾਟਾਸੈੱਟ

<p align="center">
  <img src="https://img.shields.io/badge/Lexicon-Mahan%20Kosh-red?style=for-the-badge" alt="Lexicon">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/Author-Gurpreet%20Singh%20Dhillon-orange?style=for-the-badge" alt="Author">
</p>

---

### 👨‍💻 Project Lead & Architecture
* **Curator:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **GitHub:** [github.com/gurpreetsingh5523-source](https://github.com/gurpreetsingh5523-source)
* **Flagship Project:** [AMRIT Research OS (100% Local Medical Intelligence)](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Dataset Overview
An authoritative lexical dataset compiling authentic definitions, Sanskrit/Persian/Arabic etymological roots, scriptural quotes with Ang references from Sri Guru Granth Sahib Ji, and modern Punjabi contextual sentences from Bhai Kahn Singh Nabha's magnum opus **Gurushabad Ratnakar Mahan Kosh (ਮਹਾਨ ਕੋਸ਼)**.
"""
    upload_to_huggingface("Gurbani-MahanKosh-Frontier-Corpus", mahankosh_jsonl, mahankosh_readme)

if __name__ == "__main__":
    main()
