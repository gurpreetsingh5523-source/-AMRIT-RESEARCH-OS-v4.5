#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ੴ AMRIT Sovereign Bilingual Punjabi-English Tokenizer
Author: Gurpreet Singh / AMRIT Research OS
Nam-toon Studio

Dual-script phonetic/grapheme tokenizer supporting:
- Complete Gurmukhi alphabet (ੳ-ੜ), matras (ਾ, ਿ, ੀ, ੁ, ੂ, ੇ, ੈ, ੋ, ੌ), halant (੍), bindi (ਂ), tippi (ੰ), addak (ੱ), nukta (਼)
- Full Latin/English alphabet (a-z, A-Z) for tech, medical, and scientific terms
- Numerical digits (0-9)
- Common punctuation
"""

import json
import os
import re
import unicodedata
from typing import List, Dict, Union

# Special Tokens
PAD_TOKEN = "<pad>"
UNK_TOKEN = "<unk>"
BOS_TOKEN = "<s>"
EOS_TOKEN = "</s>"

# Gurmukhi script definitions
PUNJABI_VOWELS = "ਅਆਇਈਉਊਏਐਓਔ"
PUNJABI_CONSONANTS = "ਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵੜਸ਼ਜ਼ਖ਼ਗ਼ਫ਼ਲ਼"
PUNJABI_MATRAS = "ਾਿੀੁੂੇੈੋੌ੍"
PUNJABI_DIACRITICS = "ਂੰੱ਼"

# Latin script definitions
ENGLISH_LOWER = "abcdefghijklmnopqrstuvwxyz"
ENGLISH_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Digits & Punctuation
DIGITS = "0123456789"
PUNCTUATIONS = " .,!?:;\'-_()\"/[]"

class BilingualGurmukhiEnglishTokenizer:
    def __init__(self, vocab_path: str = None):
        if vocab_path and os.path.exists(vocab_path):
            self.load_vocab(vocab_path)
        else:
            self._build_default_vocab()

    def _build_default_vocab(self):
        tokens = [PAD_TOKEN, UNK_TOKEN, BOS_TOKEN, EOS_TOKEN]
        
        # Add Gurmukhi
        for ch in PUNJABI_VOWELS + PUNJABI_CONSONANTS + PUNJABI_MATRAS + PUNJABI_DIACRITICS:
            if ch not in tokens:
                tokens.append(ch)
                
        # Add English
        for ch in ENGLISH_LOWER + ENGLISH_UPPER:
            if ch not in tokens:
                tokens.append(ch)
                
        # Add Digits & Punctuation
        for ch in DIGITS + PUNCTUATIONS:
            if ch not in tokens:
                tokens.append(ch)

        self.vocab: Dict[str, int] = {tok: idx for idx, tok in enumerate(tokens)}
        self.inv_vocab: Dict[int, str] = {idx: tok for tok, idx in self.vocab.items()}
        self.pad_id = self.vocab[PAD_TOKEN]
        self.unk_id = self.vocab[UNK_TOKEN]
        self.bos_id = self.vocab[BOS_TOKEN]
        self.eos_id = self.vocab[EOS_TOKEN]

    def encode(self, text: str, add_special_tokens: bool = True) -> List[int]:
        """Convert mixed Gurmukhi/English text into token IDs."""
        if not text:
            return []
        text = unicodedata.normalize("NFC", text)
        ids = []
        if add_special_tokens:
            ids.append(self.bos_id)
            
        for char in text:
            ids.append(self.vocab.get(char, self.unk_id))
            
        if add_special_tokens:
            ids.append(self.eos_id)
        return ids

    def decode(self, ids: List[int]) -> str:
        """Convert token IDs back to text."""
        chars = []
        for i in ids:
            tok = self.inv_vocab.get(i, "")
            if tok not in [PAD_TOKEN, UNK_TOKEN, BOS_TOKEN, EOS_TOKEN]:
                chars.append(tok)
        return "".join(chars)

    def save_vocab(self, path: str):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "vocab": self.vocab,
                "pad_id": self.pad_id,
                "unk_id": self.unk_id,
                "bos_id": self.bos_id,
                "eos_id": self.eos_id,
                "vocab_size": len(self.vocab)
            }, f, ensure_ascii=False, indent=2)

    def load_vocab(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.vocab = data["vocab"]
        self.inv_vocab = {int(v): k for k, v in self.vocab.items()}
        self.pad_id = data.get("pad_id", 0)
        self.unk_id = data.get("unk_id", 1)
        self.bos_id = data.get("bos_id", 2)
        self.eos_id = data.get("eos_id", 3)

    @property
    def vocab_size(self) -> int:
        return len(self.vocab)

if __name__ == "__main__":
    tok = BilingualGurmukhiEnglishTokenizer()
    sample = "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ! Welcome to AMRIT Research OS. ਇਹ AI ਬਹੁਤ fast ਹੈ।"
    ids = tok.encode(sample)
    decoded = tok.decode(ids)
    print(f"Vocab size: {tok.vocab_size}")
    print(f"Sample: {sample}")
    print(f"Tokens ({len(ids)}): {ids[:15]}...")
    print(f"Decoded: {decoded}")
    tok.save_vocab("audio_pipeline/bilingual_vocab.json")
    print("Saved audio_pipeline/bilingual_vocab.json")
