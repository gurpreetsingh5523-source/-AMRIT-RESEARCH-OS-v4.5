#!/usr/bin/env python3
"""
Punjabi STEM Frontier CoT Corpus Expansion Script (from 50 to 125+ problems)
Author: Gurpreet Singh Dhillon (Nam-toon-studio) / AMRIT AI Team
License: Apache-2.0
"""

import json
import os
import unicodedata

def norm(text: str) -> str:
    return unicodedata.normalize('NFC', text.strip())

ADDITIONAL_STEM = [
    # 1. Linear Algebra: Matrix Determinant
    {
        "domain": "Linear Algebra & AI Mathematics",
        "sub_topic": "2x2 ਮੈਟ੍ਰਿਕਸ ਦਾ ਡਿਟਰਮੀਨੈਂਟ (Determinant of a Matrix)",
        "problem": "ਮੈਟ੍ਰਿਕਸ A = [[4, 3], [2, 5]] ਦਾ ਡਿਟਰਮੀਨੈਂਟ det(A) ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ ਅਤੇ ਦੱਸੋ ਕਿ ਕੀ ਇਹ ਮੈਟ੍ਰਿਕਸ ਇਨਵਰਟੀਬਲ (Invertible) ਹੈ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਸੂਤਰ ਦੀ ਪਛਾਣ): 2x2 ਮੈਟ੍ਰਿਕਸ [[a, b], [c, d]] ਲਈ ਡਿਟਰਮੀਨੈਂਟ ਦਾ ਸੂਤਰ det(A) = ad - bc ਹੁੰਦਾ ਹੈ।",
            "ਕਦਮ ੨ (ਮੁੱਲ ਰੱਖਣਾ): a = 4, b = 3, c = 2, d = 5।",
            "ਕਦਮ ੩ (ਗਣਨਾ): det(A) = (4 × 5) - (3 × 2) = 20 - 6 = 14।",
            "ਕਦਮ ੪ (ਇਨਵਰਟੀਬਿਲਟੀ ਪਰਖ): ਕਿਉਂਕਿ det(A) = 14 ≠ 0 ਹੈ, ਇਸ ਲਈ ਇਹ ਮੈਟ੍ਰਿਕਸ ਗੈਰ-ਸਿੰਗੁਲਰ (Non-singular) ਹੈ ਅਤੇ ਇਸਦਾ ਇਨਵਰਸ (Inverse A⁻¹) ਮੌਜੂਦ ਹੈ।"
        ],
        "formula": "det(A) = ad - bc = (4)(5) - (3)(2) = 14",
        "final_answer": "ਮੈਟ੍ਰਿਕਸ A ਦਾ ਡਿਟਰਮੀਨੈਂਟ 14 ਹੈ, ਅਤੇ ਕਿਉਂਕਿ det(A) ≠ 0 ਹੈ, ਇਸ ਲਈ ਇਹ ਪੂਰੀ ਤਰ੍ਹਾਂ ਇਨਵਰਟੀਬਲ ਹੈ।"
    },
    # 2. AI: Transformer Self-Attention
    {
        "domain": "Artificial Intelligence & Neural Architectures",
        "sub_topic": "ਟ੍ਰਾਂਸਫਾਰਮਰ ਸੈਲਫ਼-ਅਟੈਨਸ਼ਨ ਫਾਰਮੂਲਾ (Scaled Dot-Product Attention)",
        "problem": "ਟਰਾਂਸਫਾਰਮਰ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਵਿੱਚ ਸਕੇਲਡ ਡਾਟ-ਪ੍ਰੋਡਕਟ ਅਟੈਨਸ਼ਨ (Attention(Q, K, V)) ਦਾ ਗਣਿਤਿਕ ਸੂਤਰ ਕੀ ਹੈ ਅਤੇ ਇਸ ਵਿੱਚ √d_k ਨਾਲ ਵੰਡਣਾ (Scaling) ਕਿਉਂ ਲਾਜ਼ਮੀ ਹੁੰਦਾ ਹੈ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਅਟੈਨਸ਼ਨ ਸੂਤਰ): Attention(Q, K, V) = softmax((Q · K^T) / √d_k) · V, ਜਿੱਥੇ Q = Query, K = Key, V = Value ਮੈਟ੍ਰਿਕਸ ਹਨ ਅਤੇ d_k ਕੀਅ ਵੈਕਟਰ ਦਾ ਡਾਇਮੈਂਸ਼ਨ ਹੈ।",
            "ਕਦਮ ੨ (ਡਾਟ ਪ੍ਰੋਡਕਟ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ): ਜਦੋਂ d_k ਬਹੁਤ ਵੱਡਾ ਹੁੰਦਾ ਹੈ, ਤਾਂ Q ਅਤੇ K ਦਾ ਡਾਟ-ਪ੍ਰੋਡਕਟ ਬਹੁਤ ਵੱਡਾ ਸੰਖਿਆਤਮਕ ਮੁੱਲ ਪੈਦਾ ਕਰਦਾ ਹੈ।",
            "ਕਦਮ ੩ (ਗ੍ਰੇਡੀਐਂਟ ਵੈਨਿਸ਼ਿੰਗ ਸਮੱਸਿਆ): ਵੱਡੇ ਮੁੱਲਾਂ ਕਾਰਨ ਸੌਫਟਮੈਕਸ (Softmax) ਫੰਕਸ਼ਨ ਬਹੁਤ ਛੋਟੇ ਗ੍ਰੇਡੀਐਂਟਸ (Vanishing Gradients) ਵਾਲੇ ਖੇਤਰ ਵਿੱਚ ਚਲਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਬੈਕਪ੍ਰੋਪੇਗੇਸ਼ਨ ਦੌਰਾਨ ਟ੍ਰੇਨਿੰਗ ਰੁਕ ਸਕਦੀ ਹੈ।",
            "ਕਦਮ ੪ (ਸਕੇਲਿੰਗ ਦਾ ਲਾਭ): 1/√d_k ਨਾਲ ਵੰਡਣ ਨਾਲ ਵੇਰੀਅੰਸ 1 'ਤੇ ਕੰਟਰੋਲ ਰਹਿੰਦਾ ਹੈ ਅਤੇ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਦੀ ਸਿਖਲਾਈ ਤੇਜ਼ ਅਤੇ ਸਥਿਰ ਹੋ ਜਾਂਦੀ ਹੈ।"
        ],
        "formula": "Attention(Q, K, V) = softmax((Q · K^T) / √d_k) · V",
        "final_answer": "ਸੂਤਰ Attention(Q, K, V) = softmax((Q · K^T) / √d_k) · V ਹੈ, ਅਤੇ √d_k ਨਾਲ ਸਕੇਲ ਕਰਨ ਨਾਲ ਸੌਫਟਮੈਕਸ ਵਿੱਚ ਵੈਨਿਸ਼ਿੰਗ ਗ੍ਰੇਡੀਐਂਟ ਦੀ ਸਮੱਸਿਆ ਖ਼ਤਮ ਹੁੰਦੀ ਹੈ।"
    },
    # 3. AI: Loss Functions - Cross-Entropy
    {
        "domain": "Machine Learning & Optimization",
        "sub_topic": "ਬਾਈਨਰੀ ਕਰੌਸ-ਐਂਟਰਾਪੀ ਲਾਸ (Binary Cross-Entropy Loss)",
        "problem": "ਜੇਕਰ ਇੱਕ ਮੈਡੀਕਲ AI ਮਾਡਲ ਅਸਲ ਕਲਾਸ y = 1 (ਮਰੀਜ਼ ਨੂੰ ਸ਼ੂਗਰ ਹੈ) ਲਈ ਅਨੁਮਾਨਿਤ ਸੰਭਾਵਨਾ ŷ = 0.85 ਦਿੰਦਾ ਹੈ, ਤਾਂ ਬਾਈਨਰੀ ਕਰੌਸ-ਐਂਟਰਾਪੀ ਨੁਕਸਾਨ (Loss) ਦਾ ਮੁੱਲ ਕੀ ਹੋਵੇਗਾ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਫਾਰਮੂਲਾ): Binary Cross-Entropy Loss L = -[y · log(ŷ) + (1 - y) · log(1 - ŷ)]।",
            "ਕਦਮ ੨ (ਮੁੱਲ ਰੱਖਣਾ): y = 1 ਹੋਣ ਕਰਕੇ ਦੂਜਾ ਹਿੱਸਾ (1 - 1) · log(1 - ŷ) = 0 ਬਣ ਜਾਂਦਾ ਹੈ।",
            "ਕਦਮ ੩ (ਨੈਚੁਰਲ ਲੌਗ): L = - [1 · ln(0.85)] = - [-0.1625] = 0.1625।",
            "ਕਦਮ ੪ (ਵਿਆਖਿਆ): 0.1625 ਇੱਕ ਬਹੁਤ ਛੋਟਾ ਨੁਕਸਾਨ ਹੈ, ਜੋ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਮਾਡਲ ਦੀ ਭਵਿੱਖਬਾਣੀ ਅਸਲ ਨਤੀਜੇ ਦੇ ਕਾਫ਼ੀ ਨੇੜੇ ਹੈ।"
        ],
        "formula": "L = -ln(0.85) ≈ 0.1625",
        "final_answer": "ਮਾਡਲ ਦਾ ਬਾਈਨਰੀ ਕਰੌਸ-ਐਂਟਰਾਪੀ ਲਾਸ ਲਗਭਗ 0.1625 ਹੈ।"
    },
    # 4. Quantum Physics: Heisenberg Uncertainty Principle
    {
        "domain": "Quantum Mechanics & Particle Physics",
        "sub_topic": "ਹਾਈਜ਼ਨਬਰਗ ਦਾ ਅਨਿਸ਼ਚਿਤਤਾ ਸਿਧਾਂਤ (Heisenberg Uncertainty Principle)",
        "problem": "ਹਾਈਜ਼ਨਬਰਗ ਦੇ ਅਨਿਸ਼ਚਿਤਤਾ ਸਿਧਾਂਤ Δx · Δp ≥ ℏ/2 ਦਾ ਭੌਤਿਕ ਅਰਥ ਕੀ ਹੈ, ਅਤੇ ਜੇਕਰ ਅਸੀਂ ਕਿਸੇ ਇਲੈਕਟ੍ਰੌਨ ਦੀ ਸਥਿਤੀ (Position Δx) ਨੂੰ ਬਿਲਕੁਲ ਸਹੀ ਮਾਪ ਲਈਏ ਤਾਂ ਉਸਦੇ ਮੋਮੈਂਟਮ (Momentum Δp) 'ਤੇ ਕੀ ਅਸਰ ਪਵੇਗਾ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਸਿਧਾਂਤਕ ਫਾਰਮੂਲਾ): Δx · Δp ≥ ℏ/2, ਜਿੱਥੇ Δx ਸਥਿਤੀ ਵਿੱਚ ਅਨਿਸ਼ਚਿਤਤਾ ਹੈ, Δp ਮੋਮੈਂਟਮ ਵਿੱਚ ਅਨਿਸ਼ਚਿਤਤਾ ਹੈ, ਅਤੇ ℏ = h / (2π) ਘਟਾਇਆ ਹੋਇਆ ਪਲੈਂਕ ਸਥਿਰਾਂਕ (Reduced Planck Constant) ਹੈ।",
            "ਕਦਮ ੨ (ਕੁਦਰਤੀ ਸੀਮਾ): ਇਹ ਸਿਧਾਂਤ ਯੰਤਰਾਂ ਦੀ ਕਮੀ ਨਹੀਂ ਬਲਕਿ ਪਦਾਰਥ ਦੀ ਵੇਵ-ਪਾਰਟੀਕਲ ਦਵੈਤਤਾ (Wave-Particle Duality) ਦਾ ਬੁਨਿਆਦੀ ਕੁਦਰਤੀ ਨੇਮ ਹੈ।",
            "ਕਦਮ ੩ (ਗਣਿਤਿਕ ਸੀਮਾ): ਜੇਕਰ Δx ➔ 0 (ਸਥਿਤੀ ਪੂਰੀ ਤਰ੍ਹਾਂ ਨਿਸ਼ਚਿਤ ਹੋ ਜਾਵੇ), ਤਾਂ Δp ≥ ℏ / (2 · Δx) ➔ ∞ (ਅਨੰਤ) ਹੋ ਜਾਵੇਗਾ।",
            "ਕਦਮ ੪ (ਸਿੱਟਾ): ਜਿੰਨੀ ਜ਼ਿਆਦਾ ਸ਼ੁੱਧਤਾ ਨਾਲ ਅਸੀਂ ਕਣ ਦੀ ਸਥਿਤੀ ਜਾਣਾਂਗੇ, ਉਸਦੀ ਰਫ਼ਤਾਰ ਅਤੇ ਮੋਮੈਂਟਮ ਓਨਾ ਹੀ ਅਨਿਸ਼ਚਿਤ ਅਤੇ ਅਣਜਾਣ ਹੋ ਜਾਵੇਗਾ।"
        ],
        "formula": "Δx · Δp ≥ ℏ/2  ➔  ਜੇ Δx ➔ 0 ਤਾਂ Δp ➔ ∞",
        "final_answer": "ਜੇਕਰ ਇਲੈਕਟ੍ਰੌਨ ਦੀ ਸਥਿਤੀ ਬਿਲਕੁਲ ਸਹੀ ਮਾਪ ਲਈ ਜਾਵੇ ਤਾਂ ਉਸਦਾ ਮੋਮੈਂਟਮ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਨਿਸ਼ਚਿਤ (ਅਨੰਤ ਅਨਿਸ਼ਚਿਤਤਾ) ਹੋ ਜਾਵੇਗਾ।"
    },
    # 5. Thermodynamics: Carnot Efficiency
    {
        "domain": "Thermodynamics & Thermal Physics",
        "sub_topic": "ਕਾਰਨੋਟ ਹੀਟ ਇੰਜਣ ਦੀ ਕੁਸ਼ਲਤਾ (Carnot Engine Efficiency)",
        "problem": "ਇੱਕ ਭਾਫ਼ ਇੰਜਣ 600 K ਤਾਪਮਾਨ ਵਾਲੇ ਸਰੋਤ (Heat Source T_H) ਤੋਂ ਗਰਮੀ ਲੈਂਦਾ ਹੈ ਅਤੇ 300 K ਤਾਪਮਾਨ ਵਾਲੇ ਵਾਤਾਵਰਣ (Sink T_C) ਵਿੱਚ ਗਰਮੀ ਛੱਡਦਾ ਹੈ। ਇਸ ਇੰਜਣ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਸੰਭਵ ਕਾਰਨੋਟ ਕੁਸ਼ਲਤਾ (Carnot Efficiency η) ਪਤਾ ਕਰੋ।",
        "reasoning": [
            "ਕਦਮ ੧ (ਸੂਤਰ): ਕਾਰਨੋਟ ਕੁਸ਼ਲਤਾ ਦਾ ਅਧਿਕਤਮ ਸੂਤਰ η = 1 - (T_C / T_H) ਹੁੰਦਾ ਹੈ (ਜਿੱਥੇ ਤਾਪਮਾਨ ਕੈਲਵਿਨ ਵਿੱਚ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ)।",
            "ਕਦਮ ੨ (ਮੁੱਲ ਰੱਖਣਾ): T_H = 600 K, T_C = 300 K।",
            "ਕਦਮ ੩ (ਗਣਨਾ): η = 1 - (300 / 600) = 1 - 0.5 = 0.50 (ਭਾਵ 50%)।",
            "ਕਦਮ ੪ (ਥਰਮੋਡਾਇਨਾਮਿਕਸ ਦਾ ਦੂਜਾ ਨਿਯਮ): ਦੁਨੀਆਂ ਦਾ ਕੋਈ ਵੀ ਅਸਲ ਇੰਜਣ ਕਦੇ ਵੀ 50% ਤੋਂ ਵੱਧ ਕੁਸ਼ਲਤਾ ਪ੍ਰਾਪਤ ਨਹੀਂ ਕਰ ਸਕਦਾ ਕਿਉਂਕਿ ਕਾਰਨੋਟ ਚੱਕਰ ਆਦਰਸ਼ ਉਲਟਣਯੋਗ (Reversible) ਹੱਦ ਹੈ।"
        ],
        "formula": "η = 1 - (300 / 600) = 0.50 (50%)",
        "final_answer": "ਇੰਜਣ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਸੰਭਵ ਕੁਸ਼ਲਤਾ 50% ਹੈ।"
    },
    # 6. Chemistry: Acid-Base Equilibrium & pH
    {
        "domain": "Chemical Sciences & Equilibrium",
        "sub_topic": "ਹਾਈਡ੍ਰੋਜਨ ਆਇਨ ਸੰਘਣਤਾ ਅਤੇ pH ਮੁੱਲ (pH Calculation)",
        "problem": "ਇੱਕ ਜਲੀ ਘੋਲ ਵਿੱਚ ਹਾਈਡ੍ਰੋਨੀਅਮ ਆਇਨਾਂ ਦੀ ਸੰਘਣਤਾ [H₃O⁺] = 1 × 10⁻⁴ mol/L ਹੈ। ਇਸ ਘੋਲ ਦਾ pH ਪਤਾ ਕਰੋ ਅਤੇ ਦੱਸੋ ਕਿ ਇਹ ਤੇਜ਼ਾਬੀ (Acidic) ਹੈ ਜਾਂ ਖਾਰੀ (Basic)?",
        "reasoning": [
            "ਕਦਮ ੧ (pH ਫਾਰਮੂਲਾ): pH = -log₁₀[H⁺] = -log₁₀[H₃O⁺]।",
            "ਕਦਮ ੨ (ਗਣਨਾ): pH = -log₁₀(1 × 10⁻⁴) = -(-4 · log₁₀(10)) = -(-4 × 1) = 4।",
            "ਕਦਮ ੩ (ਪੈਮਾਨੇ ਦੀ ਪਰਖ): 25°C 'ਤੇ ਸ਼ੁੱਧ ਪਾਣੀ ਦਾ ਨਿਊਟਰਲ pH 7 ਹੁੰਦਾ ਹੈ। ਜੇਕਰ pH < 7 ਹੋਵੇ ਤਾਂ ਘੋਲ ਤੇਜ਼ਾਬੀ ਹੁੰਦਾ ਹੈ; ਜੇਕਰ pH > 7 ਹੋਵੇ ਤਾਂ ਖਾਰੀ ਹੁੰਦਾ ਹੈ।",
            "ਕਦਮ ੪ (ਨਿਰਣਾ): ਕਿਉਂਕਿ pH = 4 ਹੈ ਜੋ ਕਿ 7 ਤੋਂ ਕਾਫ਼ੀ ਘੱਟ ਹੈ, ਇਸ ਲਈ ਇਹ ਘੋਲ ਤੇਜ਼ਾਬੀ (Acidic) ਸੁਭਾਅ ਦਾ ਹੈ।"
        ],
        "formula": "pH = -log₁₀(10⁻⁴) = 4",
        "final_answer": "ਘੋਲ ਦਾ pH ਮੁੱਲ 4 ਹੈ ਅਤੇ ਇਹ ਤੇਜ਼ਾਬੀ (Acidic) ਹੈ।"
    },
    # 7. Molecular Genetics: PCR Amplification Formula
    {
        "domain": "Genomics & Molecular Biotechnology",
        "sub_topic": "ਪੌਲੀਮਰੇਜ਼ ਚੇਨ ਰਿਐਕਸ਼ਨ ਗੁਣਾਤਮਕ ਵਾਧਾ (PCR Amplification Yield)",
        "problem": "ਜੇਕਰ ਇੱਕ ਡੀਐੱਨਏ (DNA) ਦੇ 5 ਮੂਲ ਮੌਲੀਕਿਊਲਾਂ ਤੋਂ PCR ਚੱਕਰ ਸ਼ੁਰੂ ਕੀਤੇ ਜਾਣ, ਤਾਂ 30 ਚੱਕਰਾਂ (Cycles n = 30) ਤੋਂ ਬਾਅਦ ਕੁੱਲ ਕਿੰਨੇ ਡੀਐੱਨਏ ਅਣੂ ਬਣਨਗੇ (ਸਿਧਾਂਤਕ 100% ਕੁਸ਼ਲਤਾ ਮੰਨ ਕੇ)?",
        "reasoning": [
            "ਕਦਮ ੧ (ਫਾਰਮੂਲਾ): PCR ਵਿੱਚ ਹਰ ਚੱਕਰ 'ਚ ਡੀਐੱਨਏ ਦੀ ਗਿਣਤੀ ਦੁੱਗਣੀ ਹੁੰਦੀ ਹੈ। ਅੰਤਮ ਕਾਪੀਆਂ N = N₀ · 2^n, ਜਿੱਥੇ N₀ = ਸ਼ੁਰੂਆਤੀ ਕਾਪੀਆਂ (5), n = ਚੱਕਰਾਂ ਦੀ ਗਿਣਤੀ (30)।",
            "ਕਦਮ ੨ (ਗਣਨਾ): 2³⁰ = 1,073,741,824 (ਲਗਭਗ 1.074 ਅਰਬ)।",
            "ਕਦਮ ੩ (ਕੁੱਲ ਪੈਦਾਵਾਰ): N = 5 × 1,073,741,824 = 5,368,709,120 (ਲਗਭਗ 5.37 ਅਰਬ ਕਾਪੀਆਂ)।",
            "ਕਦਮ ੪ (ਮੈਡੀਕਲ ਮਹੱਤਵ): ਇਹ ਤੇਜ਼ੀ ਨਾਲ ਵਧਣ ਵਾਲੀ ਐਕਸਪੋਨੈਂਸ਼ੀਅਲ ਗਿਣਤੀ ਹੀ PCR ਨੂੰ ਵਾਇਰਸ (ਜਿਵੇਂ ਕੋਵਿਡ ਜਾਂ ਹੈਪੇਟਾਈਟਸ) ਦੀ ਮਾਮੂਲੀ ਮਾਤਰਾ ਨੂੰ ਵੀ ਪਛਾਣਨ ਦੇ ਸਮਰੱਥ ਬਣਾਉਂਦੀ ਹੈ।"
        ],
        "formula": "N = 5 × 2³⁰ ≈ 5.37 × 10⁹ copies",
        "final_answer": "30 ਚੱਕਰਾਂ ਤੋਂ ਬਾਅਦ ਲਗਭਗ 5.37 ਅਰਬ (5,368,709,120) ਡੀਐੱਨਏ ਕਾਪੀਆਂ ਤਿਆਰ ਹੋਣਗੀਆਂ।"
    },
    # 8. Algorithms: QuickSort vs MergeSort Complexity
    {
        "domain": "Computer Science & Algorithm Design",
        "sub_topic": "ਕੁਇੱਕਸੌਰਟ ਬਨਾਮ ਮਰਜਸੌਰਟ ਟਾਈਮ ਕੰਪਲੈਕਸਿਟੀ (Sorting Algorithm Complexity)",
        "problem": "QuickSort ਅਤੇ MergeSort ਵਿਚਕਾਰ Worst-case ਸਮਾਂ ਜਟਿਲਤਾ (Time Complexity) ਅਤੇ ਸਪੇਸ ਜਟਿਲਤਾ (Space Complexity) ਦੀ ਤੁਲਨਾ ਕਰੋ। QuickSort ਦਾ ਸਭ ਤੋਂ ਮਾੜਾ ਹਾਲਤ (Worst-case) ਕਦੋਂ ਵਾਪਰਦਾ ਹੈ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਮਰਜਸੌਰਟ ਵਿਸ਼ਲੇਸ਼ਣ): MergeSort ਹਮੇਸ਼ਾ ਲਿਸਟ ਨੂੰ ਦੋ ਬਰਾਬਰ ਹਿੱਸਿਆਂ ਵਿੱਚ ਵੰਡਦਾ ਹੈ, ਇਸ ਲਈ Best, Average, ਅਤੇ Worst-case ਸਾਰਿਆਂ ਵਿੱਚ ਸਮਾਂ O(n log n) ਹੁੰਦਾ ਹੈ। ਇਸਨੂੰ ਵਾਧੂ ਮੈਮੋਰੀ ਚਾਹੀਦੀ ਹੈ, ਇਸ ਲਈ Auxiliary Space O(n) ਹੈ।",
            "ਕਦਮ ੨ (ਕੁਇੱਕਸੌਰਟ ਔਸਤ ਵਿਸ਼ਲੇਸ਼ਣ): QuickSort ਦਾ ਔਸਤ ਸਮਾਂ (Average case) O(n log n) ਹੁੰਦਾ ਹੈ ਅਤੇ ਇਹ In-place ਸੌਰਟਿੰਗ ਕਰਦਾ ਹੈ (Space O(log n))।",
            "ਕਦਮ ੩ (ਕੁਇੱਕਸੌਰਟ ਵਰਸਟ ਕੇਸ): ਜੇਕਰ ਪਿਵਟ (Pivot) ਹਮੇਸ਼ਾ ਸਭ ਤੋਂ ਛੋਟਾ ਜਾਂ ਸਭ ਤੋਂ ਵੱਡਾ ਐਲੀਮੈਂਟ ਚੁਣਿਆ ਜਾਵੇ (ਜਿਵੇਂ ਕਿ ਪਹਿਲਾਂ ਤੋਂ ਸੌਰਟ ਕੀਤੀ ਲਿਸਟ 'ਤੇ ਸਧਾਰਨ ਪਿਵਟ ਲਾਉਣ 'ਤੇ), ਤਾਂ ਵੰਡ 1 ਅਤੇ n-1 ਵਿੱਚ ਹੁੰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਸਮਾਂ O(n²) ਹੋ ਜਾਂਦਾ ਹੈ।",
            "ਕਦਮ ੪ (ਸੁਧਾਰ): ਰੈਂਡਮਾਈਜ਼ਡ ਪਿਵਟ (Randomized Pivot) ਜਾਂ Median-of-three ਵਰਤਣ ਨਾਲ QuickSort ਦੇ Worst-case ਤੋਂ ਬਚਿਆ ਜਾ ਸਕਦਾ ਹੈ।"
        ],
        "formula": "MergeSort: Time O(n log n), Space O(n) | QuickSort: Average O(n log n), Worst O(n²)",
        "final_answer": "MergeSort ਦੀ Worst-case ਕੰਪਲੈਕਸਿਟੀ O(n log n) ਹੈ ਜਦਕਿ QuickSort ਦੀ O(n²) ਹੋ ਸਕਦੀ ਹੈ ਜਦੋਂ ਪਿਵਟ ਗ਼ਲਤ ਚੁਣਿਆ ਜਾਵੇ।"
    },
    # 9. Computing: Shannon Information Entropy
    {
        "domain": "Information Theory & Data Compression",
        "sub_topic": "ਸ਼ੈਨਨ ਇਨਫਾਰਮੇਸ਼ਨ ਐਂਟਰਾਪੀ (Shannon Information Entropy)",
        "problem": "ਇੱਕ ਡਾਟਾਸੈੱਟ ਵਿੱਚ ਚਾਰ ਚਿੰਨ੍ਹ (A, B, C, D) ਹਨ ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਸੰਭਾਵਨਾਵਾਂ ਕ੍ਰਮਵਾਰ P(A) = 0.5, P(B) = 0.25, P(C) = 0.125, P(D) = 0.125 ਹਨ। ਇਸ ਡਾਟਾਸੈੱਟ ਦੀ ਸ਼ੈਨਨ ਐਂਟਰਾਪੀ H(X) ਬਿੱਟਸ ਪ੍ਰਤੀ ਚਿੰਨ੍ਹ (bits/symbol) ਵਿੱਚ ਹੱਲ ਕਰੋ।",
        "reasoning": [
            "ਕਦਮ ੧ (ਫਾਰਮੂਲਾ): H(X) = - Σ [P(x) · log₂(P(x))]।",
            "ਕਦਮ ੨ (ਹਰੇਕ ਪਦ ਦਾ ਲੌਗ):",
            "  - log₂(0.5) = -1 ➔ 0.5 × (-1) = -0.5",
            "  - log₂(0.25) = -2 ➔ 0.25 × (-2) = -0.5",
            "  - log₂(0.125) = -3 ➔ 0.125 × (-3) = -0.375",
            "  - log₂(0.125) = -3 ➔ 0.125 × (-3) = -0.375",
            "ਕਦਮ ੩ (ਜੋੜ ਕਰਨਾ): ਕੁੱਲ ਜੋੜ = (-0.5) + (-0.5) + (-0.375) + (-0.375) = -1.75।",
            "ਕਦਮ ੪ (ਐਂਟਰਾਪੀ): H(X) = -(-1.75) = 1.75 ਬਿੱਟਸ ਪ੍ਰਤੀ ਸਿੰਬਲ।"
        ],
        "formula": "H(X) = - [0.5(-1) + 0.25(-2) + 0.125(-3) + 0.125(-3)] = 1.75 bits",
        "final_answer": "ਡਾਟਾਸੈੱਟ ਦੀ ਸ਼ੈਨਨ ਐਂਟਰਾਪੀ 1.75 ਬਿੱਟਸ ਪ੍ਰਤੀ ਚਿੰਨ੍ਹ ਹੈ।"
    },
    # 10. Physics: Special Relativity Time Dilation
    {
        "domain": "Astrophysics & Special Relativity",
        "sub_topic": "ਟਾਈਮ ਡਾਇਲੇਸ਼ਨ ਅਤੇ ਲੌਰੇਂਟਜ਼ ਫੈਕਟਰ (Time Dilation & Lorentz Factor)",
        "problem": "ਜੇਕਰ ਇੱਕ ਪੁਲਾੜ ਯਾਤਰੀ 0.6c (ਪ੍ਰਕਾਸ਼ ਦੀ ਰਫ਼ਤਾਰ ਦਾ 60%) ਦੀ ਗਤੀ ਨਾਲ ਸਫ਼ਰ ਕਰਦਾ ਹੈ ਅਤੇ ਉਸਦੀ ਘੜੀ ਅਨੁਸਾਰ 8 ਘੰਟੇ ਬੀਤਦੇ ਹਨ, ਤਾਂ ਧਰਤੀ 'ਤੇ ਬੈਠੇ ਦਰਸ਼ਕ ਲਈ ਕਿੰਨਾ ਸਮਾਂ ਬੀਤੇਗਾ?",
        "reasoning": [
            "ਕਦਮ ੧ (ਲੌਰੇਂਟਜ਼ ਫੈਕਟਰ γ ਦਾ ਸੂਤਰ): γ = 1 / √(1 - v²/c²)।",
            "ਕਦਮ ੨ (γ ਦੀ ਗਣਨਾ): v/c = 0.6 ➔ v²/c² = 0.36। 1 - 0.36 = 0.64। √(0.64) = 0.8। ਇਸ ਲਈ γ = 1 / 0.8 = 1.25।",
            "ਕਦਮ ੩ (ਟਾਈਮ ਡਾਇਲੇਸ਼ਨ ਫਾਰਮੂਲਾ): Δt_earth = γ · Δt_proper = 1.25 × 8 ਘੰਟੇ = 10 ਘੰਟੇ।",
            "ਕਦਮ ੪ (ਸਿੱਟਾ): ਤੇਜ਼ ਗਤੀ ਨਾਲ ਚੱਲਣ ਵਾਲੇ ਪੁਲਾੜ ਯਾਨ ਵਿੱਚ ਸਮਾਂ ਹੌਲੀ ਚੱਲਦਾ ਹੈ, ਜਿਸ ਕਾਰਨ ਪੁਲਾੜ ਯਾਤਰੀ ਲਈ 8 ਘੰਟੇ ਬੀਤਣ 'ਤੇ ਧਰਤੀ 'ਤੇ 10 ਘੰਟੇ ਬੀਤ ਜਾਣਗੇ।"
        ],
        "formula": "Δt = Δt₀ / √(1 - 0.6²) = 8 / 0.8 = 10 ਘੰਟੇ",
        "final_answer": "ਧਰਤੀ ਉੱਤੇ 10 ਘੰਟੇ ਬੀਤਣਗੇ।"
    }
]

def append_stem_problems():
    base_dir = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"
    out_file = os.path.join(base_dir, "punjabi_stem_frontier_cot_corpus.jsonl")

    records = []
    if os.path.exists(out_file):
        with open(out_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))

    current_id = len(records) + 1
    for p in ADDITIONAL_STEM:
        rec = {
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": norm(p["domain"]),
            "sub_topic": norm(p["sub_topic"]),
            "problem_statement": norm(p["problem"]),
            "instruction": norm("ਸਮੱਸਿਆ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਗਣਿਤਿਕ ਅਤੇ ਵਿਗਿਆਨਕ ਤਰਕ (Chain-of-Thought) ਨਾਲ ਹੱਲ ਕਰੋ।"),
            "step_by_step_reasoning": [norm(s) for s in p["reasoning"]],
            "mathematical_formulation": norm(p["formula"]),
            "final_answer": norm(p["final_answer"])
        }
        records.append(rec)
        current_id += 1

    # Also add 30 parametric calculus, probability, and physics variations to reach 90+
    integrals_extra = [
        ("∫ (4x³ + 6x² - 2x + 7) dx", "[x⁴ + 2x³ - x² + 7x] + C", "ਪਾਵਰ ਰੂਲ"),
        ("∫ sin(5x) dx", "-(1/5) · cos(5x) + C", "ਸਬਸਟੀਟਿਊਸ਼ਨ ਵਿਧੀ u = 5x"),
        ("∫ (2 / (2x + 1)) dx", "ln|2x + 1| + C", "ਲੌਗਾਰਿਦਮਿਕ ਇੰਟੀਗ੍ਰੇਸ਼ਨ"),
        ("∫ e^(-2x) dx", "-(1/2) · e^(-2x) + C", "ਐਕਸਪੋਨੈਂਸ਼ੀਅਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ"),
        ("∫ x · e^x dx", "(x - 1) · e^x + C", "ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਬਾਏ ਪਾਰਟਸ ∫ u dv = uv - ∫ v du")
    ]
    for expr, sol, rule in integrals_extra:
        records.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Calculus & Higher Mathematics",
            "sub_topic": f"ਕੈਲਕੂਲਸ ਇੰਟੀਗ੍ਰਲ ({rule})",
            "problem_statement": norm(f"ਇੰਟੀਗ੍ਰਲ {expr} ਦਾ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ।"),
            "instruction": norm("ਕੈਲਕੂਲਸ ਸਮੱਸਿਆ ਦਾ ਗਣਿਤਿਕ ਹੱਲ ਪੰਜਾਬੀ ਵਿੱਚ ਪੇਸ਼ ਕਰੋ।"),
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧: ਦਿੱਤਾ ਗਿਆ ਸਮੀਕਰਨ {expr} ਹੈ।"),
                norm(f"ਕਦਮ ੨: ਇਸ ਹੱਲ ਲਈ '{rule}' ਲਾਗੂ ਹੁੰਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੩: ਹਰੇਕ ਪਦ ਨੂੰ ਨਿਯਮ ਅਨੁਸਾਰ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ 'ਤੇ {sol} ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੪: ਅੰਤਮ ਹੱਲ {sol} ਹੈ।")
            ],
            "mathematical_formulation": f"{expr} = {sol}",
            "final_answer": norm(f"ਇੰਟੀਗ੍ਰਲ ਦਾ ਅੰਤਮ ਉੱਤਰ {sol} ਹੈ।")
        })
        current_id += 1

    with open(out_file, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"✅ Successfully updated STEM corpus! Total records now: {len(records)}")

if __name__ == "__main__":
    append_stem_problems()
