#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ Upload Expanded 217-Clip Multi-Speaker Studio Dataset to Hugging Face
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio
"""

import os
from huggingface_hub import HfApi

def upload_dataset():
    repo_id = "Nam-toon-studio/Punjabi-MultiSpeaker-Studio-TTS-Corpus"
    local_dir = "audio_pipeline/Punjabi-MultiSpeaker-Studio-TTS-Corpus"
    
    print(f"🚀 Uploading expanded 217-clip multi-speaker dataset to https://huggingface.co/datasets/{repo_id}...")
    api = HfApi()
    
    # Upload metadata.csv and train.parquet
    api.upload_file(
        path_or_fileobj=os.path.join(local_dir, "metadata.csv"),
        path_in_repo="metadata.csv",
        repo_id=repo_id,
        repo_type="dataset",
        commit_message="ੴ Expand dataset to 217 studio clips across 4 sovereign speakers"
    )
    api.upload_file(
        path_or_fileobj=os.path.join(local_dir, "train.parquet"),
        path_in_repo="train.parquet",
        repo_id=repo_id,
        repo_type="dataset",
        commit_message="ੴ Update train.parquet with 217 samples and bilingual tech orator"
    )
    
    # Upload new wav files
    wavs_dir = os.path.join(local_dir, "wavs")
    for f in os.listdir(wavs_dir):
        if f.endswith(".wav") and ("spk4_" in f or "_part2_" in f):
            local_path = os.path.join(wavs_dir, f)
            print(f"Uploading new clip: {f}...")
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=f"wavs/{f}",
                repo_id=repo_id,
                repo_type="dataset",
                commit_message=f"ੴ Add {f}"
            )
            
    print("\n🎉 Dataset update on Hugging Face complete!")

if __name__ == "__main__":
    upload_dataset()
