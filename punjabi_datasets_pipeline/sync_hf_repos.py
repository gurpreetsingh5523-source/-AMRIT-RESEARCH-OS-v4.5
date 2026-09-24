#!/usr/bin/env python3
"""
Sync HF Repos with Git and Push
"""

import os
import subprocess
import shutil

token_path = os.path.expanduser('~/.cache/huggingface/token')
token = open(token_path).read().strip() if os.path.exists(token_path) else ''

def git_upload(repo_name, files_dict):
    repo_url = f'https://Nam-toon-studio:{token}@huggingface.co/datasets/Nam-toon-studio/{repo_name}'
    temp_dir = f'/tmp/hf_{repo_name}'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    print(f'\n🚀 Preparing & Syncing repository: {repo_name}...')
    # Create repo if not exists
    try:
        import urllib.request, json
        create_payload = json.dumps({
            "name": repo_name,
            "organization": "Nam-toon-studio",
            "private": False,
            "type": "dataset"
        }).encode('utf-8')
        req = urllib.request.Request("https://huggingface.co/api/repos/create", data=create_payload, headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        with urllib.request.urlopen(req) as resp:
            print(f'✅ Repository created: {repo_name}')
    except Exception as e:
        pass
    git_base = [
        'git',
        '-c', 'filter.lfs.smudge=cat',
        '-c', 'filter.lfs.clean=cat',
        '-c', 'filter.lfs.process=cat',
        '-c', 'filter.lfs.required=false'
    ]
    subprocess.run(git_base + ['clone', repo_url, temp_dir], check=True)
    
    for fname, content_or_path in files_dict.items():
        dst = os.path.join(temp_dir, fname)
        if isinstance(content_or_path, str) and os.path.exists(content_or_path):
            shutil.copy2(content_or_path, dst)
        else:
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(content_or_path)
    
    subprocess.run(git_base + ['-C', temp_dir, 'config', 'user.name', 'Gurpreet Singh'], check=True)
    subprocess.run(git_base + ['-C', temp_dir, 'config', 'user.email', 'gurpreetsingh5523@users.noreply.huggingface.co'], check=True)
    subprocess.run(git_base + ['-C', temp_dir, 'add', '.'], check=True)
    
    status = subprocess.check_output(git_base + ['-C', temp_dir, 'status', '--porcelain'], text=True)
    if not status.strip():
        print(f'ℹ️ No changes for {repo_name}.')
        shutil.rmtree(temp_dir)
        return
    
    subprocess.run(git_base + ['-C', temp_dir, 'commit', '-m', 'Professional documentation and expanded dataset release'], check=True)
    subprocess.run(git_base + ['-C', temp_dir, 'push', 'origin', 'main'], check=True)
    print(f'✅ Successfully updated {repo_name} on Hugging Face!')
    shutil.rmtree(temp_dir)

def main():
    base_dir = '/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline'

    grammar_readme = '''---
license: apache-2.0
language:
- pa
task_categories:
- text-generation
- question-answering
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
  <a href="https://github.com/gurpreetsingh5523-source"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0"><img src="https://img.shields.io/badge/Project-AMRIT%20OS-crimson?style=for-the-badge" alt="Project AMRIT"></a>
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
</p>

---

### 👨‍💻 Research & Engineering Lead
* **Creator & Architect:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **GitHub Profile:** [github.com/gurpreetsingh5523-source](https://github.com/gurpreetsingh5523-source)
* **Flagship Innovation:** [AMRIT Research OS (100% Locally-Run Autonomous Medical AI)](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Overview / ਸੰਖੇਪ
The **Punjabi (Gurmukhi) Grammatical Error Correction (GEC) Corpus** is a curated, gold-standard parallel dataset designed for training and benchmarking neural grammatical error correction models for the Punjabi language.

Every sentence pair in this corpus is crafted according to **standard Punjabi grammar principles (ਪੰਜਾਬੀ ਯੂਨੀਵਰਸਿਟੀ ਪਟਿਆਲਾ ਟਕਸਾਲੀ ਵਿਆਕਰਣ ਨਿਯਮ)** with precise grammatical rule explanations in Punjabi.

---

### 🎯 Key Grammatical Categories Covered (1,140+ Verified Pairs)

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

### 📜 Citation & License
Published under the **Apache-2.0 License** by **Gurpreet Singh Dhillon (Nam-toon Studio)**.
'''

    git_upload('Punjabi-Gurmukhi-Grammar-Correction-Corpus', {
        'train.jsonl': os.path.join(base_dir, 'punjabi_grammar_correction_corpus.jsonl'),
        'train.parquet': os.path.join(base_dir, 'punjabi_grammar_train.parquet'),
        'README.md': grammar_readme
    })

    mahankosh_readme = '''---
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
  <a href="https://github.com/gurpreetsingh5523-source"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0"><img src="https://img.shields.io/badge/Project-AMRIT%20OS-crimson?style=for-the-badge" alt="Project AMRIT"></a>
  <img src="https://img.shields.io/badge/Lexicon-Mahan%20Kosh-red?style=for-the-badge" alt="Lexicon">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
</p>

---

### 👨‍💻 Project Lead & Architecture
* **Curator & Developer:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **GitHub Profile:** [github.com/gurpreetsingh5523-source](https://github.com/gurpreetsingh5523-source)
* **Flagship Project:** [AMRIT Research OS (Autonomous Medical AI)](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Dataset Overview
An authoritative lexical dataset compiling authentic definitions, Sanskrit/Persian/Arabic etymological roots, scriptural quotes with Ang references from Sri Guru Granth Sahib Ji, and modern Punjabi contextual sentences from Bhai Kahn Singh Nabha's magnum opus **Gurushabad Ratnakar Mahan Kosh (ਮਹਾਨ ਕੋਸ਼)**.
'''

    git_upload('Gurbani-MahanKosh-Frontier-Corpus', {
        'train.jsonl': os.path.join(base_dir, 'gurbani_mahankosh_expanded_corpus.jsonl'),
        'train.parquet': os.path.join(base_dir, 'gurbani_mahankosh_train.parquet'),
        'README.md': mahankosh_readme
    })

    # 3. AMRIT Punjabi Clinical Dialogue Corpus
    amrit_med_readme = '''---
license: apache-2.0
language:
- pa
task_categories:
- question-answering
- text-generation
multilinguality:
- monolingual
size_categories:
- n<1K
tags:
- medical
- clinical-ai
- punjabi
- gurmukhi
- healthcare
- amrit-research-os
- diagnosis
- sovereign-ai
pretty_name: AMRIT Punjabi Clinical Dialogue & Medical Diagnosis Corpus
---

# ੴ AMRIT Punjabi Clinical Dialogue & Medical Diagnosis Corpus
## ☬ ਅੰਮ੍ਰਿਤ ਪੰਜਾਬੀ ਕਲੀਨਿਕਲ ਸੰਵਾਦ ਅਤੇ ਡਾਕਟਰੀ ਨਿਦਾਨ ਡਾਟਾਸੈੱਟ (v1.0)

<p align="center">
  <a href="https://github.com/gurpreetsingh5523-source"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0"><img src="https://img.shields.io/badge/Project-AMRIT%20OS-crimson?style=for-the-badge" alt="Project AMRIT"></a>
  <img src="https://img.shields.io/badge/Domain-Healthcare%20%26%20Medicine-red?style=for-the-badge" alt="Domain">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
</p>

---

### 👨‍💻 Research & Medical AI Architecture
* **Lead Developer:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **Mission:** **Free Autonomous AI Doctor for Humanity (ਦੁਨੀਆਂ ਦੇ ਲੋੜਵੰਦ ਲੋਕਾਂ ਲਈ ਮੁਫ਼ਤ AI ਡਾਕਟਰ)**
* **Flagship Platform:** [AMRIT Research OS (100% Local Medical Intelligence)](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Dataset Overview / ਸੰਖੇਪ
The **AMRIT Punjabi Clinical Dialogue Corpus** is an evidence-based clinical reasoning dataset curated in pure **Punjabi (Gurmukhi)** designed to train edge-native medical AI agents (AMRIT OS & Sehaj AI Doctor).

Every case in this dataset mirrors realistic rural and urban clinical patient presentations across Punjab, structured according to standardized clinical triage protocols.

---

### 🩺 Clinical Domains Covered (200+ Scenarios)
1. **Endocrinology:** Diabetes (ਟਾਈਪ ੨ ਸ਼ੂਗਰ, Fasting/PP/HbA1c), Thyroid disorders (ਹਾਈਪੋਥਾਇਰਾਇਡਿਜ਼ਮ)
2. **Cardiology & Emergency:** Hypertension (ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ), Angina/Heart Attack warning signs, Dyslipidemia (ਕੋਲੈਸਟ੍ਰੋਲ)
3. **Pulmonology:** Bronchial Asthma (ਦਮਾ), Tuberculosis (ਟੀ.ਬੀ), Seasonal Allergic Rhinitis
4. **Hematology:** Iron Deficiency Anemia (ਖੂਨ ਦੀ ਕਮੀ, Hb < 9), Thrombocytopenia
5. **Gastroenterology:** Acid Reflux (GERD), Peptic Ulcer, Gallbladder Stones (ਪਿੱਤੇ ਦੀ ਪੱਥਰੀ), Jaundice/Hepatitis (ਪੀਲੀਆ)
6. **Nephrology & Urology:** UTI (ਪਿਸ਼ਾਬ ਇਨਫੈਕਸ਼ਨ), Kidney Stones (ਗੁਰਦੇ ਦੀ ਪੱਥਰੀ), BPH (ਪ੍ਰੋਸਟੇਟ), CKD
7. **Neurology:** Migraine (ਮਾਈਗ੍ਰੇਨ), Stroke warning signs (ਲਕਵਾ / FAST protocol), Sciatica (ਸਿਆਟਿਕਾ)
8. **Dermatology & Skin:** Fungal infections (ਦਾਦ/ਖਾਰਸ਼), Eczema
9. **Pediatrics & Child Care:** Acute Gastroenteritis, Dehydration management (ORS)
10. **Gynecology & Women's Health:** PCOS / Hormonal imbalance
11. **Laboratory Reports:** Complete interpretation of CBC, Lipid Profile, LFT, KFT, and Urine Routine.

---

### 📊 Sample JSONL Format
```json
{
  "id": "amrit_clinical_00001",
  "domain": "Endocrinology & Metabolic Health",
  "instruction": "ਮਰੀਜ਼ ਦੇ ਪੰਜਾਬੀ ਵਿੱਚ ਦੱਸੇ ਲੱਛਣਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਭਾਵਿਤ ਕਲੀਨਿਕਲ ਮੁਲਾਂਕਣ, ਜ਼ਰੂਰੀ ਲੈਬ ਟੈਸਟ, ਪਰਹੇਜ਼ ਅਤੇ ਡਾਕਟਰੀ ਸਲਾਹ ਤਿਆਰ ਕਰੋ।",
  "patient_profile": {
    "age": "48 ਸਾਲ",
    "gender": "ਪੁਰਸ਼",
    "chief_complaint": "ਵਾਰ-ਵਾਰ ਪਿਸ਼ਾਬ ਆਉਣਾ, ਬਹੁਤ ਜ਼ਿਆਦਾ ਪਿਆਸ ਲੱਗਣਾ ਅਤੇ ਅਚਾਨਕ ਭਾਰ ਘਟਣਾ।"
  },
  "patient_query": "ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਨੂੰ ਪਿਛਲੇ ਵੀਹ ਦਿਨਾਂ ਤੋਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਪਿਆਸ ਲੱਗ ਰਹੀ ਹੈ, ਰਾਤ ਨੂੰ ਕਈ ਵਾਰ ਪਿਸ਼ਾਬ ਜਾਣਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਥਕਾਵਟ ਬਣੀ ਰਹਿੰਦੀ ਹੈ। ਮੈਨੂੰ ਕੀ ਹੋ ਸਕਦਾ ਹੈ?",
  "clinical_assessment": "ਮਰੀਜ਼ ਦੇ ਲੱਛਣ ਸ਼ੂਗਰ (Type 2 Diabetes Mellitus) ਦੇ ਕਲਾਸੀਕਲ ਲੱਛਣਾਂ ਵੱਲ ਸੰਕੇਤ ਕਰਦੇ ਹਨ।",
  "suspected_conditions": [
    "ਟਾਈਪ 2 ਸ਼ੂਗਰ (Type 2 Diabetes Mellitus)",
    "ਪ੍ਰੀ-ਡਾਇਬੀਟੀਜ਼",
    "ਹਾਈਪਰਗਲਾਈਸੀਮੀਆ"
  ],
  "triage_level": "ਮੱਧਮ (Moderate - ੨੪-੪੮ ਘੰਟਿਆਂ ਵਿੱਚ ਡਾਕਟਰੀ ਜਾਂਚ ਜ਼ਰੂਰੀ)",
  "suggested_tests": [
    "Fasting Blood Sugar (FBS)",
    "Postprandial Blood Sugar (PPBS)",
    "HbA1c (੩ ਮਹੀਨਿਆਂ ਦੀ ਔਸਤ ਸ਼ੂਗਰ)"
  ],
  "guidance_and_precautions": "ਮਿੱਠੀਆਂ ਚੀਜ਼ਾਂ, ਖੰਡ, ਗੁੜ, ਕੋਲਡ ਡਰਿੰਕਸ ਤੋਂ ਤੁਰੰਤ ਪਰਹੇਜ਼ ਕਰੋ। ਰੋਜ਼ਾਨਾ ੩੦-੪੦ ਮਿੰਟ ਸੈਰ ਕਰੋ।",
  "disclaimer": "ਇਹ ਜਾਣਕਾਰੀ ਕੇਵਲ ਮੈਡੀਕਲ ਸਿੱਖਿਆ ਲਈ ਹੈ। ਸਹੀ ਇਲਾਜ ਲਈ ਡਾਕਟਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।"
}
```

---

### 📜 License
Published under the **Apache-2.0 License** by **Gurpreet Singh Dhillon (Nam-toon Studio)** for open medical research.
'''

    git_upload('AMRIT-Punjabi-Clinical-Dialogue-Corpus', {
        'train.jsonl': os.path.join(base_dir, 'amrit_punjabi_clinical_dialogue_corpus.jsonl'),
        'train.parquet': os.path.join(base_dir, 'amrit_clinical_train.parquet'),
        'README.md': amrit_med_readme
    })

    # 4. Punjabi STEM & Frontier Reasoning CoT Corpus
    stem_readme = '''---
license: apache-2.0
language:
- pa
task_categories:
- question-answering
- text-generation
multilinguality:
- monolingual
tags:
- stem
- quantum-physics
- mathematics
- deep-reasoning
- chain-of-thought
- punjabi
- gurmukhi
- artificial-intelligence
- sovereign-ai
pretty_name: Punjabi (Gurmukhi) STEM & Frontier Chain-of-Thought (CoT) Corpus
---

# ੴ Punjabi STEM & Frontier Chain-of-Thought (CoT) Corpus
## ☬ ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ) ਵਿਗਿਆਨ ਅਤੇ ਉੱਚ-ਗਣਿਤ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਡਾਟਾਸੈੱਟ

<p align="center">
  <a href="https://github.com/gurpreetsingh5523-source"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0"><img src="https://img.shields.io/badge/Project-Sehaj%20AI-orange?style=for-the-badge" alt="Sehaj AI"></a>
  <img src="https://img.shields.io/badge/Domain-STEM%20%26%20Quantum-purple?style=for-the-badge" alt="STEM">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License">
</p>

---

### 👨‍💻 Research & Engineering Architecture
* **Architect & Developer:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **Vision:** Sovereign Indic Intelligence & Advanced Scientific Reasoning in Gurmukhi.
* **Flagship Innovation:** [AMRIT Research OS & Sehaj Sovereign Neural Model](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Dataset Overview / ਸੰਖੇਪ
The **Punjabi STEM & Frontier CoT Corpus** is a curated dataset providing rigorous, step-by-step **Chain-of-Thought (CoT)** solutions in Gurmukhi for complex problems across:
- **Quantum Mechanics & Qubits** (ਕੁਆਂਟਮ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ, ਬੌਰਨ ਰੂਲ, ਕੁਬਿਟ ਸਟੇਟਸ)
- **Calculus & Linear Algebra** (ਡੈਰੀਵੇਟਿਵਜ਼, ਚੇਨ ਰੂਲ, ਕੁਆਡ੍ਰੈਟਿਕ ਫਾਰਮੂਲਾ, ਟ੍ਰਾਂਸਫਾਰਮਰ ਅਟੈਂਸ਼ਨ ਮੈਥ)
- **Classical Physics & Electromagnetism** (ਊਰਜਾ ਸੰਭਾਲ, ਓਹਮ ਦਾ ਨਿਯਮ, ਬਿਜਲਈ ਸ਼ਕਤੀ)
- **Physical Chemistry & Kinetics** (ਮੋਲੈਰਿਟੀ, ਘੋਲ ਸੰਘਣਤਾ)
- **Computer Science & AI** (ਬਾਈਨਰੀ ਸਰਚ ਕੰਪਲੈਕਸਿਟੀ, ਸਾਰਟਿੰਗ ਐਲਗੋਰਿਦਮ, ਸਾਫਟਮੈਕਸ, ਕ੍ਰਾਸ-ਐਂਟ੍ਰੋਪੀ ਲਾਸ)
- **Molecular Biology & Genetics** (DNA ➔ mRNA ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ, ਅਮੀਨੋ ਐਸਿਡ ਡੀਕੋਡਿੰਗ)

---

### 📊 Sample CoT Format (JSONL)
```json
{
  "id": "punjabi_stem_00001",
  "domain": "Quantum Physics & Quantum Computing",
  "sub_topic": "ਕੁਆਂਟਮ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਅਤੇ ਕੁਬਿਟ",
  "instruction": "ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਗਿਆਨਕ/ਗਣਿਤਿਕ ਪ੍ਰਸ਼ਨ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਨਾਲ ਸ਼ੁੱਧ ਪੰਜਾਬੀ ਵਿੱਚ ਹੱਲ ਕਰੋ।",
  "problem_statement": "ਇੱਕ ਕਲਾਸੀਕਲ ਬਿੱਟ ਅਤੇ ਇੱਕ ਕੁਆਂਟਮ ਕੁਬਿਟ ਵਿਚਕਾਰ ਮੂਲ ਅੰਤਰ ਕੀ ਹੈ?",
  "step_by_step_reasoning": [
    "ਕਦਮ ੧ (ਕਲਾਸੀਕਲ ਬਿੱਟ): ਇੱਕ ਬਿੱਟ ਜਾਂ ਤਾਂ 0 ਜਾਂ 1 ਹੁੰਦਾ ਹੈ।",
    "ਕਦਮ ੨ (ਕੁਆਂਟਮ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ): ਇੱਕ ਕੁਬਿਟ |ψ⟩ = α|0⟩ + β|1⟩ ਅਵਸਥਾ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।",
    "ਕਦਮ ੩ (ਸੰਭਾਵਨਾ ਨਿਯਮ): |α|² + |β|² = 1 ਹੁੰਦਾ ਹੈ।",
    "ਕਦਮ ੪ (ਵੇਵ ਫੰਕਸ਼ਨ ਕੋਲੈਪਸ): ਮਾਪਣ 'ਤੇ ਇਹ 0 ਜਾਂ 1 ਵਿੱਚ ਕੋਲੈਪਸ ਹੋ ਜਾਂਦਾ ਹੈ।"
  ],
  "mathematical_formulation": "|ψ⟩ = α|0⟩ + β|1⟩",
  "final_answer": "ਕਲਾਸੀਕਲ ਬਿੱਟ ਸਿਰਫ਼ 0 ਜਾਂ 1 ਹੁੰਦਾ ਹੈ, ਜਦਕਿ ਕੁਬਿਟ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।"
```

---

### 📜 License
Published under the **Apache-2.0 License** by **Gurpreet Singh Dhillon (Nam-toon Studio)**.
'''

    git_upload('Punjabi-STEM-Frontier-CoT-Corpus', {
        'train.jsonl': os.path.join(base_dir, 'punjabi_stem_frontier_cot_corpus.jsonl'),
        'train.parquet': os.path.join(base_dir, 'punjabi_stem_train.parquet'),
        'README.md': stem_readme
    })

    # 5. Punjab Heritage, Gurmat Philosophy & Comparative Theology Corpus
    heritage_readme = '''---
license: cc-by-sa-4.0
language:
- pa
task_categories:
- question-answering
- text-generation
multilinguality:
- monolingual
tags:
- sikh-theology
- gurbani
- sggs
- gurmat
- punjab-history
- comparative-religion
- sovereign-ai
- scholarly-analysis
pretty_name: Punjab Heritage, Gurmat Philosophy & Comparative Theology Corpus
---

# ੴ Punjab Heritage, Gurmat Philosophy & Comparative Theology Corpus
## ☬ ਪੰਜਾਬੀ ਵਿਰਸਾ, ਗੁਰਮਤਿ ਫ਼ਲਸਫ਼ਾ ਅਤੇ ਤੁਲਨਾਤਮਕ ਧਰਮ ਅਧਿਐਨ ਪ੍ਰਮਾਣਿਕ ਡਾਟਾਸੈੱਟ

<p align="center">
  <a href="https://github.com/gurpreetsingh5523-source"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0"><img src="https://img.shields.io/badge/Project-AMRIT%20OS-crimson?style=for-the-badge" alt="Project AMRIT"></a>
  <img src="https://img.shields.io/badge/Domain-Theology%20%26%20Sikh%20History-navy?style=for-the-badge" alt="Domain">
  <img src="https://img.shields.io/badge/Language-Punjabi%20(Gurmukhi)-blue?style=for-the-badge" alt="Language">
  <img src="https://img.shields.io/badge/License-CC--BY--SA--4.0-green?style=for-the-badge" alt="License">
</p>

---

### 👨‍💻 Research & Academic Architecture
* **Lead Researcher & Curator:** **Gurpreet Singh Dhillon (Nam-toon Studio)**
* **Mission:** Authentic, Uncompromised, Source-Based Gurmat & Indic Historiography for Sovereign Artificial Intelligence.
* **Flagship Platform:** [AMRIT Research OS & Sehaj Sovereign AI](https://github.com/gurpreetsingh5523-source/-AMRIT-RESEARCH-OS-v3.0)

---

### 📖 Purpose & Scholarly Scope / ਡਾਟਾਸੈੱਟ ਦਾ ਉਦੇਸ਼ ਅਤੇ ਵਿਦਵਤਾਪੂਰਨ ਖੇਤਰ
This corpus provides definitive textual, historical, and philosophical ground truths to prevent AI hallucinations, misattributions, and theological distortions regarding Sikhism and historical Indic sects.

Key domains addressed:
1. **ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ ਦੀ ਇਕਲੌਤੀ ਗੁਰਤਾ (Sole Spiritual Sovereignty of SGGS):** 
   - Authentic Gurbani citations verifying that SGGS is the only spiritual Satguru ('ਏਕਾ ਬਾਣੀ ਇਕੁ ਗੁਰੁ').
   - Strict adherence to Sri Guru Gobind Singh Ji’s 1708 injunction at Nanded ('ਸਭ ਸਿੱਖਨ ਕਉ ਹੁਕਮ ਹੈ ਗੁਰੂ ਮਾਨਿਓ ਗ੍ਰੰਥ').
2. **ਬਚਿੱਤਰ ਨਾਟਕ (ਕਥਿਤ ਦਸਮ ਗ੍ਰੰਥ) ਅਤੇ ਸਰਬਲੋਹ ਗ੍ਰੰਥ ਦਾ ਅਕਾਦਮਿਕ ਮੁਲਾਂਕਣ:**
   - Detailed textual criticism clarifying that these compositions are Braj Bhasha poetic renderings and adaptations of classical Puranic/Hindu mythologies (Markandeya Purana, Chandi Charitra, Chaubis Avatar, Charitropakhyan) by royal court poets (ਦਰਬਾਰੀ ਕਵੀ).
   - Clear theological boundaries showing they are NOT spiritual scriptures equivalent to SGGS.
3. **ਤੁਲਨਾਤਮਕ ਅਧਿਐਨ (Comparative Theology):**
   - **ਸ਼ੈਵ ਮਤ (Shaivism):** Hatha yoga, renunciation, ash smearing, and how Guru Nanak Dev Ji’s *Sidh Gosht* reformed it into social responsibility and householder life.
   - **ਵੈਸ਼ਨਵ ਮਤ (Vaishnavism):** Incarnationism (ਅਵਤਾਰਵਾਦ), idol worship, fasting, and Gurbani’s strict doctrine of Ajuni (ਅਜੂਨੀ - beyond birth).
   - **ਸ਼ਾਕਤ ਮਤ (Shaktism):** Tantra, sacrificial blood rituals (ਬਲੀ ਪ੍ਰਥਾ), and Gurbani’s condemnation of the 'Sakat' mindset.
   - **ਨਾਨਕ ਮਤ / ਗੁਰਮਤਿ (Nanak Mat):** The sovereign 'Nirmal Panth'—rejection of caste divisions, gender equality, universal oneness (੧ਓ), and honest living (ਕਿਰਤ ਕਰੋ, ਨਾਮ ਜਪੋ, ਵੰਡ ਛਕੋ).
4. **ਪੰਜਾਬ ਦਾ ਸਾਵਰੇਨ ਇਤਿਹਾਸ (Punjab History & Sovereignty):**
   - Baba Banda Singh Bahadur’s 1710 Khalsa Republic and the revolutionary abolition of feudalism ('Land to the Tiller').
   - The democratic *Sarbat Khalsa* and Gurmata system of the 18th-century Sikh Misls.

---

### 📜 Sources & Methodology
* **Sri Guru Granth Sahib Ji** (Standard 1430 Angs)
* **Varan Bhai Gurdas Ji** (ਵਾਰਾਂ ਭਾਈ ਗੁਰਦਾਸ ਜੀ)
* **Mahan Kosh** (Bhai Kahn Singh Nabha)
* **Prof. Sahib Singh** (Gurbani Viakaran & Darpan)
* **Sikh Rehat Maryada** (SGPC 1945 Statutory Code)
* Contemporary Persian & British historical chronicles (Khafi Khan, Cunningham, Rattan Singh Bhangu).

---

### 📜 License
Published under **Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA-4.0)** for open academic and AI alignment research.
'''

    git_upload('Punjab-Heritage-Gurmat-Theology-Corpus', {
        'train.jsonl': os.path.join(base_dir, 'punjab_history_theology_critical_corpus.jsonl'),
        'train.parquet': os.path.join(base_dir, 'punjab_theology_train.parquet'),
        'README.md': heritage_readme
    })

if __name__ == '__main__':
    main()

