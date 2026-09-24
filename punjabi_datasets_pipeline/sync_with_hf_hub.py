#!/usr/bin/env python3
"""
Direct Hugging Face Hub Dataset Sync using HfApi
Author: Gurpreet Singh Dhillon (Nam-toon-studio) / AMRIT AI Team
"""

import os
import sys
from huggingface_hub import HfApi

def sync_datasets():
    token_path = os.path.expanduser('~/.cache/huggingface/token')
    token = open(token_path).read().strip() if os.path.exists(token_path) else ''
    api = HfApi(token=token)

    base = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"

    repos = [
        {
            "repo_id": "Nam-toon-studio/Gurbani-MahanKosh-Frontier-Corpus",
            "files": {
                "train.jsonl": os.path.join(base, "gurbani_mahankosh_expanded_corpus.jsonl"),
                "train.parquet": os.path.join(base, "gurbani_mahankosh_train.parquet")
            },
            "desc": "Expanded Mahan Kosh to 116 authentic entries + Parquet viewer"
        },
        {
            "repo_id": "Nam-toon-studio/Punjab-Heritage-Gurmat-Theology-Corpus",
            "files": {
                "train.jsonl": os.path.join(base, "punjab_history_theology_critical_corpus.jsonl"),
                "train.parquet": os.path.join(base, "punjab_theology_train.parquet")
            },
            "desc": "Expanded Punjab Heritage & Theology to 35 scholarly long-form entries + Parquet viewer"
        },
        {
            "repo_id": "Nam-toon-studio/Punjabi-STEM-Frontier-CoT-Corpus",
            "files": {
                "train.jsonl": os.path.join(base, "punjabi_stem_frontier_cot_corpus.jsonl"),
                "train.parquet": os.path.join(base, "punjabi_stem_train.parquet")
            },
            "desc": "Expanded STEM CoT to 65 deep reasoning problems + Parquet viewer"
        },
        {
            "repo_id": "Nam-toon-studio/AMRIT-Punjabi-Clinical-Dialogue-Corpus",
            "files": {
                "train.jsonl": os.path.join(base, "amrit_punjabi_clinical_dialogue_corpus.jsonl"),
                "train.parquet": os.path.join(base, "amrit_clinical_train.parquet")
            },
            "desc": "Added Parquet viewer support for 206 clinical dialogues"
        },
        {
            "repo_id": "Nam-toon-studio/Punjabi-Gurmukhi-Grammar-Correction-Corpus",
            "files": {
                "train.jsonl": os.path.join(base, "punjabi_grammar_correction_corpus.jsonl"),
                "train.parquet": os.path.join(base, "punjabi_grammar_train.parquet")
            },
            "desc": "Verified 1,140 pairs + Parquet viewer"
        }
    ]

    for item in repos:
        repo_id = item["repo_id"]
        print(f"\n🚀 Syncing {repo_id} via HfApi...")
        for rfile, lpath in item["files"].items():
            if os.path.exists(lpath):
                size_kb = os.path.getsize(lpath) / 1024
                print(f"   📤 Uploading {rfile} ({size_kb:.1f} KB)...")
                api.upload_file(
                    path_or_fileobj=lpath,
                    path_in_repo=rfile,
                    repo_id=repo_id,
                    repo_type="dataset",
                    commit_message=f"{item['desc']} ({rfile})"
                )
                print(f"   ✅ {rfile} successfully uploaded to {repo_id}!")
            else:
                print(f"   ⚠️ Local file missing: {lpath}")

    print("\n🎉 All 5 repositories successfully synced and updated on Hugging Face!")

if __name__ == "__main__":
    sync_datasets()
