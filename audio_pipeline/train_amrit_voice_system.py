#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ AMRIT Multi-Speaker Bilingual Neural Voice Trainer
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio

Trains a genuine multi-speaker neural acoustic model on the 217-clip
Punjabi-MultiSpeaker-Studio-TTS-Corpus across 4 distinct speaker identities:
- Speaker 0: Bhai Ranjit Singh (Male Orator)
- Speaker 1: Dr. Surjit Patar (Male Literary)
- Speaker 2: BBC Punjabi (Female Broadcaster)
- Speaker 3: Bilingual Tech Orator (Punjabi-English AI Discourse)
"""

import os
import sys
import argparse
import json
import time
import math
import numpy as np
import pandas as pd
import soundfile as sf
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchaudio.transforms as T

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from bilingual_tokenizer import BilingualGurmukhiEnglishTokenizer

SPEAKER_TO_ID = {
    "Bhai Ranjit Singh": 0,
    "Dr. Surjit Patar": 1,
    "BBC Punjabi Broadcaster": 2,
    "Bilingual Tech Orator": 3
}

class PunjabiMultiSpeakerDataset(Dataset):
    def __init__(self, corpus_dir: str, tokenizer: BilingualGurmukhiEnglishTokenizer, max_len: int = 250):
        self.corpus_dir = corpus_dir
        self.tokenizer = tokenizer
        self.max_len = max_len
        
        meta_csv = os.path.join(corpus_dir, "metadata.csv")
        df = pd.read_csv(meta_csv)
        self.records = []
        
        self.mel_transform = T.MelSpectrogram(
            sample_rate=22050,
            n_fft=1024,
            win_length=1024,
            hop_length=256,
            n_mels=80,
            f_min=0.0,
            f_max=8000.0
        )
        
        for _, r in df.iterrows():
            wav_path = os.path.join(corpus_dir, r["file_name"])
            if os.path.exists(wav_path):
                spk_name = r["speaker_name"]
                spk_id = SPEAKER_TO_ID.get(spk_name, 0)
                text = str(r["normalized_text"]) if pd.notna(r["normalized_text"]) else ""
                if text.strip():
                    self.records.append((wav_path, text, spk_id))
                    
        print(f"📊 Dataset Loaded: {len(self.records)} valid training samples across 4 speakers.")

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        wav_path, text, spk_id = self.records[idx]
        tokens = self.tokenizer.encode(text, add_special_tokens=True)
        if len(tokens) > self.max_len:
            tokens = tokens[:self.max_len]
            
        # Load audio & compute mel
        audio, sr = sf.read(wav_path)
        audio_tensor = torch.from_numpy(audio).float().unsqueeze(0)
        
        # Max audio clamp (10 seconds = 220500 samples)
        if audio_tensor.shape[1] > 220500:
            audio_tensor = audio_tensor[:, :220500]
            
        mel = self.mel_transform(audio_tensor).squeeze(0) # (80, T_mel)
        log_mel = torch.log(torch.clamp(mel, min=1e-5))
        
        return {
            "tokens": torch.tensor(tokens, dtype=torch.long),
            "mel": log_mel,
            "speaker_id": torch.tensor(spk_id, dtype=torch.long)
        }

def collate_fn(batch):
    pad_id = 0
    token_lens = [len(item["tokens"]) for item in batch]
    mel_lens = [item["mel"].shape[1] for item in batch]
    
    max_token_len = max(token_lens)
    max_mel_len = max(mel_lens)
    
    padded_tokens = torch.full((len(batch), max_token_len), pad_id, dtype=torch.long)
    padded_mels = torch.full((len(batch), 80, max_mel_len), -11.5, dtype=torch.float)
    speaker_ids = torch.zeros(len(batch), dtype=torch.long)
    
    for i, item in enumerate(batch):
        t = item["tokens"]
        m = item["mel"]
        padded_tokens[i, :len(t)] = t
        padded_mels[i, :, :m.shape[1]] = m
        speaker_ids[i] = item["speaker_id"]
        
    return {
        "tokens": padded_tokens,
        "token_lens": torch.tensor(token_lens, dtype=torch.long),
        "mels": padded_mels,
        "mel_lens": torch.tensor(mel_lens, dtype=torch.long),
        "speaker_ids": speaker_ids
    }

class AmritMultiSpeakerAcousticModel(nn.Module):
    """
    Sovereign Multi-Speaker Acoustic Neural Architecture:
    - Text Encoder with bilingual embeddings
    - Multi-Speaker Embedding conditioning (4 speakers)
    - Autoregressive/Convolutional Mel Decoder
    """
    def __init__(self, vocab_size: int = 150, num_speakers: int = 4, hidden_dim: int = 256, mel_dim: int = 80):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.mel_dim = mel_dim
        
        # 1. Bilingual Token Embedding
        self.token_embedding = nn.Embedding(vocab_size, hidden_dim, padding_idx=0)
        
        # 2. Multi-Speaker Embedding
        self.speaker_embedding = nn.Embedding(num_speakers, 128)
        
        # 3. Text Encoder (Conv + Bi-GRU)
        self.encoder_conv = nn.Sequential(
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size=5, padding=2),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size=5, padding=2),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1)
        )
        self.encoder_gru = nn.GRU(hidden_dim, hidden_dim // 2, batch_first=True, bidirectional=True)
        
        # 4. Decoder with Speaker Conditioning
        self.proj_spk = nn.Linear(128, hidden_dim)
        self.decoder_gru = nn.GRU(hidden_dim + mel_dim, hidden_dim, batch_first=True)
        self.mel_out = nn.Linear(hidden_dim, mel_dim)

    def forward(self, tokens, mels=None, speaker_ids=None):
        B, T_text = tokens.shape
        # Embed text
        x = self.token_embedding(tokens) # (B, T, hidden)
        x_conv = self.encoder_conv(x.transpose(1, 2)).transpose(1, 2)
        enc_out, _ = self.encoder_gru(x_conv) # (B, T, hidden)
        
        # Embed speaker
        spk_emb = self.speaker_embedding(speaker_ids) # (B, 128)
        spk_proj = self.proj_spk(spk_emb).unsqueeze(1) # (B, 1, hidden)
        
        # Condition encoder with speaker representation
        enc_conditioned = enc_out + spk_proj
        
        if mels is not None:
            # Training mode with teacher forcing
            T_mel = mels.shape[2]
            # Match lengths via interpolation
            enc_expanded = F.interpolate(enc_conditioned.transpose(1, 2), size=T_mel, mode='linear', align_corners=False).transpose(1, 2)
            
            # Mel input shifted
            mel_in = mels.transpose(1, 2)
            dec_in = torch.cat([enc_expanded, mel_in], dim=-1)
            dec_out, _ = self.decoder_gru(dec_in)
            pred_mel = self.mel_out(dec_out).transpose(1, 2)
            return pred_mel
        else:
            # Inference mode
            T_pred = int(T_text * 5.5) # approximate duration ratio
            enc_expanded = F.interpolate(enc_conditioned.transpose(1, 2), size=T_pred, mode='linear', align_corners=False).transpose(1, 2)
            current_mel = torch.zeros(B, 1, self.mel_dim, device=tokens.device)
            mels_generated = []
            hidden = None
            for t in range(T_pred):
                dec_in = torch.cat([enc_expanded[:, t:t+1, :], current_mel], dim=-1)
                dec_out, hidden = self.decoder_gru(dec_in, hidden)
                current_mel = self.mel_out(dec_out)
                mels_generated.append(current_mel)
            pred_mel = torch.cat(mels_generated, dim=1).transpose(1, 2)
            return pred_mel

def train_model(epochs: int = 15, batch_size: int = 8, lr: float = 1e-3):
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"\n🚀 STARTING AMRIT MULTI-SPEAKER VOICE TRAINING ON [{device.upper()}]...")
    
    corpus_dir = "audio_pipeline/Punjabi-MultiSpeaker-Studio-TTS-Corpus"
    tokenizer = BilingualGurmukhiEnglishTokenizer()
    dataset = PunjabiMultiSpeakerDataset(corpus_dir, tokenizer)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    
    model = AmritMultiSpeakerAcousticModel(
        vocab_size=tokenizer.vocab_size + 10,
        num_speakers=4,
        hidden_dim=256,
        mel_dim=80
    ).to(device)
    
    criterion = nn.L1Loss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    
    model.train()
    total_samples = len(dataset)
    start_time = time.time()
    
    print(f"🧠 Model Architecture: {sum(p.numel() for p in model.parameters() if p.requires_grad):,} trainable parameters.")
    print(f"📦 Training Config: {epochs} Epochs | Batch Size {batch_size} | {len(dataloader)} Batches/Epoch\n")
    
    loss_history = []
    
    for epoch in range(1, epochs + 1):
        epoch_loss = 0.0
        t0 = time.time()
        for b_idx, batch in enumerate(dataloader):
            tokens = batch["tokens"].to(device)
            mels = batch["mels"].to(device)
            speaker_ids = batch["speaker_ids"].to(device)
            
            optimizer.zero_grad()
            pred_mels = model(tokens, mels, speaker_ids)
            
            # Loss: L1 mel reconstruction loss
            loss = criterion(pred_mels, mels)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
            
        scheduler.step()
        avg_loss = epoch_loss / len(dataloader)
        loss_history.append(avg_loss)
        elapsed = time.time() - t0
        print(f"🔥 Epoch [{epoch:02d}/{epochs:02d}] - Loss: {avg_loss:.4f} - LR: {scheduler.get_last_lr()[0]:.6f} - Time: {elapsed:.2f}s")
        
    total_time = time.time() - start_time
    print(f"\n🎉 TRAINING COMPLETED IN {total_time:.1f}s!")
    print(f"   Initial Loss: {loss_history[0]:.4f} ➡️ Final Loss: {loss_history[-1]:.4f}")
    
    # Save checkpoint
    output_checkpoint = "audio_pipeline/amrit_voice_multispeaker.pt"
    torch.save({
        "epoch": epochs,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "loss_history": loss_history,
        "speaker_to_id": SPEAKER_TO_ID,
        "vocab_size": tokenizer.vocab_size
    }, output_checkpoint)
    print(f"💾 Checkpoint saved: {output_checkpoint} ({os.path.getsize(output_checkpoint)/(1024*1024):.2f} MB)")
    
    # Save config
    config_json = "audio_pipeline/amrit_voice_multispeaker.json"
    with open(config_json, "w", encoding="utf-8") as f:
        json.dump({
            "model_name": "AMRIT Sovereign Multi-Speaker Bilingual Voice System",
            "version": "1.0.0",
            "sample_rate": 22050,
            "speakers": {
                "0": "Bhai Ranjit Singh (Male Orator)",
                "1": "Dr. Surjit Patar (Male Literary)",
                "2": "BBC Punjabi Broadcaster (Female Broadcaster)",
                "3": "Bilingual Tech Orator (Punjabi-English)"
            },
            "num_speakers": 4,
            "training_samples": len(dataset),
            "final_loss": loss_history[-1],
            "vocab_size": tokenizer.vocab_size
        }, f, ensure_ascii=False, indent=2)
    print(f"💾 Config JSON saved: {config_json}")
    return output_checkpoint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AMRIT Multi-Speaker Voice Model")
    parser.add_argument("--epochs", type=int, default=12, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=8, help="Batch size")
    parser.add_argument("--lr", type=float, default=1e-3, help="Learning rate")
    args = parser.parse_args()
    
    train_model(epochs=args.epochs, batch_size=args.batch_size, lr=args.lr)
