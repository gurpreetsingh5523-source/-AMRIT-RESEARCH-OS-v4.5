#!/usr/bin/env python3
"""
Punjabi STEM & Mathematics Frontier Reasoning (CoT) Dataset Generator
Author: Gurpreet Singh Dhillon (Nam-toon-studio) / AMRIT & Sehaj AI Team
License: Apache-2.0 / MIT

Curates a high-density, multi-domain Punjabi Chain-of-Thought (CoT) reasoning dataset
covering Mathematics, Quantum Physics, Chemistry, Computing, and Molecular Biology.
"""

import json
import os
import unicodedata
from typing import List, Dict, Any

def norm(text: str) -> str:
    return unicodedata.normalize('NFC', text.strip())

def build_stem_core() -> List[Dict[str, Any]]:
    dataset = []
    idx = 1

    stem_problems = [
        # ==========================================
        # 1. QUANTUM PHYSICS & COMPUTING
        # ==========================================
        {
            "domain": "Quantum Physics & Quantum Computing",
            "sub_topic": "ਕੁਆਂਟਮ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਅਤੇ ਕੁਬਿਟ (Quantum Superposition & Qubit)",
            "problem": "ਇੱਕ ਕਲਾਸੀਕਲ ਬਿੱਟ ਅਤੇ ਇੱਕ ਕੁਆਂਟਮ ਕੁਬਿਟ (|ψ⟩ = α|0⟩ + β|1⟩) ਵਿਚਕਾਰ ਮੂਲ ਅੰਤਰ ਕੀ ਹੈ, ਅਤੇ ਜਦੋਂ ਇਸ ਕੁਬਿਟ ਦਾ ਮਾਪ (Measurement) ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਕੀ ਵਾਪਰਦਾ ਹੈ?",
            "reasoning": [
                "ਕਦਮ ੧ (ਕਲਾਸੀਕਲ ਬਿੱਟ): ਕਲਾਸੀਕਲ ਕੰਪਿਊਟਿੰਗ ਵਿੱਚ ਇੱਕ ਬਿੱਟ ਕਿਸੇ ਵੀ ਦਿੱਤੇ ਸਮੇਂ ਵਿੱਚ ਨਿਸ਼ਚਿਤ ਤੌਰ 'ਤੇ ਕੇਵਲ ਇੱਕ ਸਥਿਤੀ ਵਿੱਚ ਹੁੰਦਾ ਹੈ — ਜਾਂ ਤਾਂ 0 ਜਾਂ 1।",
                "ਕਦਮ ੨ (ਕੁਆਂਟਮ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ): ਇੱਕ ਕੁਬਿਟ ਲੀਨੀਅਰ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਸਟੇਟ ਵਿੱਚ ਹੁੰਦਾ ਹੈ: |ψ⟩ = α|0⟩ + β|1⟩, ਜਿੱਥੇ α ਅਤੇ β ਕੰਪਲੈਕਸ ਐਂਪਲੀਟਿਊਡ (Complex Amplitudes) ਹਨ।",
                "ਕਦਮ ੩ (ਸੰਭਾਵਨਾ ਨਿਯਮ): ਕੁਆਂਟਮ ਮਕੈਨਿਕਸ ਦੇ ਬੌਰਨ ਰੂਲ (Born's Rule) ਅਨੁਸਾਰ ਕੁੱਲ ਸੰਭਾਵਨਾ 1 ਹੋਣੀ ਲਾਜ਼ਮੀ ਹੈ, ਭਾਵ |α|² + |β|² = 1।",
                "ਕਦਮ ੪ (ਵੇਵ ਫੰਕਸ਼ਨ ਕੋਲੈਪਸ): ਜਦੋਂ ਅਸੀਂ ਕੁਬਿਟ ਦਾ ਮਾਪ (Measurement) ਲੈਂਦੇ ਹਾਂ, ਤਾਂ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਖ਼ਤਮ (Wavefunction Collapse) ਹੋ ਜਾਂਦੀ ਹੈ ਅਤੇ ਸਾਨੂੰ |α|² ਸੰਭਾਵਨਾ ਨਾਲ |0⟩ ਜਾਂ |β|² ਸੰਭਾਵਨਾ ਨਾਲ |1⟩ ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ।"
            ],
            "formula": "|ψ⟩ = α|0⟩ + β|1⟩,  ਜਿੱਥੇ  |α|² + |β|² = 1",
            "final_answer": "ਕਲਾਸੀਕਲ ਬਿੱਟ ਸਿਰਫ਼ 0 ਜਾਂ 1 ਹੁੰਦਾ ਹੈ, ਜਦਕਿ ਕੁਬਿਟ ਦੋਵਾਂ ਦਾ ਇਕੱਠਾ ਸੁਪਰਪੁਜ਼ੀਸ਼ਨ ਰੂਪ ਹੁੰਦਾ ਹੈ ਜੋ ਮਾਪਣ 'ਤੇ |α|² ਸੰਭਾਵਨਾ ਨਾਲ 0 ਅਤੇ |β|² ਸੰਭਾਵਨਾ ਨਾਲ 1 ਵਿੱਚ ਬਦਲਦਾ ਹੈ।"
        },
        # ==========================================
        # 2. CALCULUS & MATHEMATICS
        # ==========================================
        {
            "domain": "Calculus & Higher Mathematics",
            "sub_topic": "ਡੈਰੀਵੇਟਿਵ ਅਤੇ ਚੇਨ ਰੂਲ (Chain Rule in Differentiation)",
            "problem": "ਫੰਕਸ਼ਨ f(x) = sin(3x² + 5) ਦਾ x ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਡੈਰੀਵੇਟਿਵ (Derivative df/dx) ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ।",
            "reasoning": [
                "ਕਦਮ ੧ (ਅੰਦਰੂਨੀ ਅਤੇ ਬਾਹਰੀ ਫੰਕਸ਼ਨ ਪਛਾਣੋ): ਇਹ ਇੱਕ ਸੰਯੁਕਤ ਫੰਕਸ਼ਨ (Composite Function) ਹੈ। ਬਾਹਰੀ ਫੰਕਸ਼ਨ u = g(x) = 3x² + 5 ਹੈ, ਅਤੇ ਮੁੱਖ ਫੰਕਸ਼ਨ f(u) = sin(u) ਹੈ।",
                "ਕਦਮ ੨ (ਚੇਨ ਰੂਲ ਫਾਰਮੂਲਾ): ਚੇਨ ਰੂਲ ਅਨੁਸਾਰ df/dx = (df/du) · (du/dx) ਹੁੰਦਾ ਹੈ।",
                "ਕਦਮ ੩ (ਬਾਹਰੀ ਫੰਕਸ਼ਨ ਦਾ ਡੈਰੀਵੇਟਿਵ): df/du = d/du [sin(u)] = cos(u) = cos(3x² + 5)।",
                "ਕਦਮ ੪ (ਅੰਦਰੂਨੀ ਫੰਕਸ਼ਨ ਦਾ ਡੈਰੀਵੇਟਿਵ): du/dx = d/dx [3x² + 5] = 6x + 0 = 6x।",
                "ਕਦਮ ੫ (ਗੁਣਾ ਕਰਕੇ ਅੰਤਮ ਰੂਪ ਦਿਓ): df/dx = cos(3x² + 5) · (6x) = 6x · cos(3x² + 5)।"
            ],
            "formula": "df/dx = (df/du) · (du/dx) = 6x · cos(3x² + 5)",
            "final_answer": "ਫੰਕਸ਼ਨ f(x) = sin(3x² + 5) ਦਾ ਡੈਰੀਵੇਟਿਵ 6x · cos(3x² + 5) ਹੈ।"
        },
        # ==========================================
        # 3. LINEAR ALGEBRA & AI MATHEMATICS
        # ==========================================
        {
            "domain": "Linear Algebra & Neural Networks",
            "sub_topic": "ਮੈਟ੍ਰਿਕਸ ਗੁਣਾ ਅਤੇ ਵੈਕਟਰ ਡਾਟ ਪ੍ਰੋਡਕਟ (Dot Product in Attention Mechanism)",
            "problem": "AI ਟ੍ਰਾਂਸਫਾਰਮਰ ਮਾਡਲ ਵਿੱਚ Query ਵੈਕਟਰ Q = [1, 2] ਅਤੇ Key ਵੈਕਟਰ K = [3, 4] ਵਿਚਕਾਰ ਸਕੇਲਡ ਡਾਟ ਪ੍ਰੋਡਕਟ (Scaled Dot Product Attention Score, d_k = 4) ਕਿਵੇਂ ਕੱਢਿਆ ਜਾਂਦਾ ਹੈ?",
            "reasoning": [
                "ਕਦਮ ੧ (ਡਾਟ ਪ੍ਰੋਡਕਟ ਕੱਢੋ): Q · K^T = (Q₁ · K₁) + (Q₂ · K₂) = (1 × 3) + (2 × 4) = 3 + 8 = 11।",
                "ਕਦਮ ੨ (ਸਕੇਲਿੰਗ ਫੈਕਟਰ): ਟ੍ਰਾਂਸਫਾਰਮਰ ਵਿੱਚ ਵੱਡੇ ਅਯਾਮਾਂ ਕਾਰਨ ਗਰੇਡੀਐਂਟ ਵੈਨਿਸ਼ਿੰਗ ਨੂੰ ਰੋਕਣ ਲਈ √d_k ਨਾਲ ਭਾਗ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇੱਥੇ d_k = 4 ਹੈ, ਇਸ ਲਈ √d_k = √4 = 2।",
                "ਕਦਮ ੩ (ਸਕੇਲਡ ਸਕੋਰ): Attention Score = (Q · K^T) / √d_k = 11 / 2 = 5.5।",
                "ਕਦਮ ੪ (ਸਾਫਟਮੈਕਸ ਐਪਲੀਕੇਸ਼ਨ): ਇਸ 5.5 ਦੇ ਸਕੋਰ ਨੂੰ ਬਾਅਦ ਵਿੱਚ ਹੋਰ ਕੁੰਜੀਆਂ (Keys) ਨਾਲ Softmax ਰਾਹੀਂ ਸੰਭਾਵਨਾ ਭਾਰ (Probability Weight) ਵਿੱਚ ਬਦਲਿਆ ਜਾਂਦਾ ਹੈ।"
            ],
            "formula": "Score = (Q · K^T) / √d_k = 11 / 2 = 5.5",
            "final_answer": "Query ਅਤੇ Key ਵੈਕਟਰਾਂ ਦਾ ਸਕੇਲਡ ਡਾਟ ਪ੍ਰੋਡਕਟ ਅਟੈਂਸ਼ਨ ਸਕੋਰ 5.5 ਆਉਂਦਾ ਹੈ।"
        },
        # ==========================================
        # 4. CLASSICAL MECHANICS & ENERGY
        # ==========================================
        {
            "domain": "Classical Mechanics & Thermodynamics",
            "sub_topic": "ਗੁਰੂਤਾਕਰਸ਼ਣ ਊਰਜਾ ਅਤੇ ਗਤੀ ਊਰਜਾ ਸੰਭਾਲ (Conservation of Mechanical Energy)",
            "problem": "ਇੱਕ 2 ਕਿਲੋਗ੍ਰਾਮ (m = 2 kg) ਦਾ ਪੱਥਰ 20 ਮੀਟਰ ਉੱਚੀ ਛੱਤ (h = 20 m) ਤੋਂ ਡਿੱਗਦਾ ਹੈ। ਧਰਤੀ ਨਾਲ ਟਕਰਾਉਣ ਤੋਂ ਠੀਕ ਪਹਿਲਾਂ ਇਸਦੀ ਗਤੀ (Velocity v) ਕਿੰਨੀ ਹੋਵੇਗੀ? (g = 9.8 m/s² ਲਓ)",
            "reasoning": [
                "ਕਦਮ ੧ (ਊਰਜਾ ਸੰਭਾਲ ਦਾ ਨਿਯਮ): ਕੁੱਲ ਮਕੈਨੀਕਲ ਊਰਜਾ ਸਦਾ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ: ਸ਼ੁਰੂਆਤੀ ਪੋਟੈਂਸ਼ੀਅਲ ਊਰਜਾ (PE) = ਅੰਤਮ ਗਤੀ ਊਰਜਾ (KE)।",
                "ਕਦਮ ੨ (ਸ਼ੁਰੂਆਤੀ ਪੋਟੈਂਸ਼ੀਅਲ ਊਰਜਾ): PE = m · g · h = 2 kg × 9.8 m/s² × 20 m = 392 Joules।",
                "ਕਦਮ ੩ (ਅੰਤਮ ਗਤੀ ਊਰਜਾ ਫਾਰਮੂਲਾ): KE = (1/2) · m · v² = (1/2) × 2 × v² = v²।",
                "ਕਦਮ ੪ (ਸਮੀਕਰਨ ਬਣਾਓ): PE = KE ➔ 392 = v² ➔ v = √392 ≈ 19.799 m/s।"
            ],
            "formula": "v = √(2 · g · h) = √(2 × 9.8 × 20) = √392 ≈ 19.8 m/s",
            "final_answer": "ਪੱਥਰ ਦੀ ਜ਼ਮੀਨ ਨਾਲ ਟਕਰਾਉਣ ਵੇਲੇ ਗਤੀ ਲਗਭਗ 19.8 ਮੀਟਰ ਪ੍ਰਤੀ ਸਕਿੰਟ (m/s) ਹੋਵੇਗੀ।"
        },
        # ==========================================
        # 5. MOLECULAR BIOLOGY & GENETICS (AMRIT Domain)
        # ==========================================
        {
            "domain": "Genetics & Molecular Biology",
            "sub_topic": "DNA ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਅਤੇ ਜੈਨੇਟਿਕ ਕੋਡ (DNA to mRNA Transcription)",
            "problem": "ਜੇਕਰ ਇੱਕ DNA ਟੈਂਪਲੇਟ ਸਟ੍ਰੈਂਡ ਦਾ ਸੀਕਵੈਂਸ 3'-TAC GGC TTA CGA ACT-5' ਹੈ, ਤਾਂ ਬਣਨ ਵਾਲੇ mRNA ਅਤੇ ਅਨੁਵਾਦਿਤ ਅਮੀਨੋ ਐਸਿਡ ਸੀਕਵੈਂਸ ਦੀ ਗਣਨਾ ਕਰੋ।",
            "reasoning": [
                "ਕਦਮ ੧ (ਕੰਪਲੀਮੈਂਟਰੀ ਬੇਸ ਪੇਅਰਿੰਗ ਨਿਯਮ): DNA ਤੋਂ RNA ਬਣਾਉਂਦੇ ਸਮੇਂ: A ਨਾਲ U (ਯੂਰਾਸਿਲ), T ਨਾਲ A (ਐਡੇਨੀਨ), C ਨਾਲ G (ਗੁਆਨੀਨ), ਅਤੇ G ਨਾਲ C (ਸਾਈਟੋਸੀਨ) ਜੁੜਦਾ ਹੈ।",
                "ਕਦਮ ੨ (mRNA ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ 5' ਤੋਂ 3'): 3'-TAC GGC TTA CGA ACT-5' ➔ 5'-AUG CCG AAU GCU UGA-3'।",
                "ਕਦਮ ੩ (ਕੋਡੌਨ ਡੀਕੋਡਿੰਗ):",
                "  • AUG = Methionine (ਸ਼ੁਰੂਆਤੀ ਕੋਡੌਨ / Start Codon)",
                "  • CCG = Proline",
                "  • AAU = Asparagine",
                "  • GCU = Alanine",
                "  • UGA = Stop Codon (ਪ੍ਰੋਟੀਨ ਸੰਸਲੇਸ਼ਣ ਸਮਾਪਤੀ)।",
                "ਕਦਮ ੪ (ਪ੍ਰੋਟੀਨ ਚੇਨ): Met-Pro-Asn-Ala।"
            ],
            "formula": "DNA (3'→5') ➔ mRNA (5'→3'): TAC GGC TTA CGA ACT ➔ AUG CCG AAU GCU UGA",
            "final_answer": "ਬਣਨ ਵਾਲਾ mRNA 'AUG CCG AAU GCU UGA' ਹੈ ਅਤੇ ਤਿਆਰ ਪੈਪਟਾਈਡ ਚੇਨ 'ਮੈਥੀਓਨੀਨ-ਪ੍ਰੋਲੀਨ-ਐਸਪੈਰਾਜੀਨ-ਐਲਾਨੀਨ' (Met-Pro-Asn-Ala) ਹੈ।"
        },
        # ==========================================
        # 6. COMPUTER SCIENCE & ALGORITHMS
        # ==========================================
        {
            "domain": "Computer Science & Algorithm Complexity",
            "sub_topic": "ਬਾਈਨਰੀ ਸਰਚ ਅਤੇ ਟਾਈਮ ਕੰਪਲੈਕਸਿਟੀ (Binary Search O(log N))",
            "problem": "1,000,000 (10 ਲੱਖ) ਤਰਤੀਬਬੱਧ (Sorted) ਸੰਖਿਆਵਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਇੱਕ ਖ਼ਾਸ ਨੰਬਰ ਲੱਭਣ ਲਈ ਬਾਈਨਰੀ ਸਰਚ ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ ਕਿੰਨੀਆਂ ਤੁਲਨਾਵਾਂ (Comparisons) ਲੱਗਣਗੀਆਂ?",
            "reasoning": [
                "ਕਦਮ ੧ (ਬਾਈਨਰੀ ਸਰਚ ਕਾਰਜਪ੍ਰਣਾਲੀ): ਬਾਈਨਰੀ ਸਰਚ ਹਰ ਕਦਮ ਉੱਤੇ ਖੋਜ ਖੇਤਰ ਨੂੰ ਅੱਧਾ (Divide and Conquer, N/2) ਕਰ ਦਿੰਦੀ ਹੈ।",
                "ਕਦਮ ੨ (ਵੱਧ ਤੋਂ ਵੱਧ ਤੁਲਨਾਵਾਂ ਫਾਰਮੂਲਾ): Worst-case comparisons = ⌊log₂(N)⌋ + 1।",
                "ਕਦਮ ੩ (ਗਣਨਾ): N = 1,000,000। ਅਸੀਂ ਜਾਣਦੇ ਹਾਂ 2¹⁹ = 524,288 ਅਤੇ 2²⁰ = 1,048,576।",
                "ਕਦਮ ੪ (ਲੌਗ ਮੁੱਲ): log₂(1,000,000) ≈ 19.93। ਇਸਦਾ ਸੀਲਿੰਗ ਮੁੱਲ 20 ਹੈ।",
                "ਕਦਮ ੫ (ਸਿੱਟਾ): ਲੀਨੀਅਰ ਸਰਚ ਵਿੱਚ 10 ਲੱਖ ਤੁਲਨਾਵਾਂ ਲੱਗ ਸਕਦੀਆਂ ਸਨ, ਪਰ ਬਾਈਨਰੀ ਸਰਚ ਵੱਧ ਤੋਂ ਵੱਧ ਸਿਰਫ਼ 20 ਤੁਲਨਾਵਾਂ ਵਿੱਚ ਨੰਬਰ ਲੱਭ ਲਵੇਗੀ।"
            ],
            "formula": "Max Comparisons = ⌈log₂(1,000,000)⌉ = 20",
            "final_answer": "10 ਲੱਖ ਤਰਤੀਬਬੱਧ ਐਲੀਮੈਂਟਾਂ ਵਿੱਚ ਬਾਈਨਰੀ ਸਰਚ ਵੱਧ ਤੋਂ ਵੱਧ 20 ਤੁਲਨਾਵਾਂ (20 Steps) ਵਿੱਚ ਉੱਤਰ ਲੱਭ ਲੈਂਦੀ ਹੈ।"
        }
    ]

    for item in stem_problems:
        dataset.append({
            "id": f"punjabi_stem_{idx:05d}",
            "domain": item["domain"],
            "sub_topic": item["sub_topic"],
            "instruction": f"ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਗਿਆਨਕ/ਗਣਿਤਿਕ ਪ੍ਰਸ਼ਨ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ (Step-by-Step Chain of Thought) ਨਾਲ ਸ਼ੁੱਧ ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ) ਵਿੱਚ ਹੱਲ ਕਰੋ।",
            "problem_statement": norm(item["problem"]),
            "step_by_step_reasoning": [norm(r) for r in item["reasoning"]],
            "mathematical_formulation": item["formula"],
            "final_answer": norm(item["final_answer"])
        })
        idx += 1

    return dataset

def generate_expanded_stem_corpus(base_dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Generate hundreds of diverse mathematical, physical, and computing reasoning problems.
    """
    expanded = list(base_dataset)
    current_id = len(expanded) + 1

    # Parametric Generators for Mathematics, Physics, Chemistry, CS
    
    # 1. Quadratic Equations in Punjabi
    quadratics = [
        (1, -5, 6, "x² - 5x + 6 = 0", 2, 3),
        (1, -7, 12, "x² - 7x + 12 = 0", 3, 4),
        (1, -9, 20, "x² - 9x + 20 = 0", 4, 5),
        (1, -3, 2, "x² - 3x + 2 = 0", 1, 2),
        (1, -8, 15, "x² - 8x + 15 = 0", 3, 5),
        (1, -10, 21, "x² - 10x + 21 = 0", 3, 7),
        (1, -11, 28, "x² - 11x + 28 = 0", 4, 7),
        (1, -6, 8, "x² - 6x + 8 = 0", 2, 4),
        (1, -12, 35, "x² - 12x + 35 = 0", 5, 7),
        (1, -13, 36, "x² - 13x + 36 = 0", 4, 9)
    ]

    for a, b, c, eq_str, r1, r2 in quadratics:
        disc = b**2 - 4*a*c
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Algebra & Quadratic Equations",
            "sub_topic": "ਦੋ-ਘਾਤੀ ਸਮੀਕਰਨ ਦਾ ਹੱਲ (Quadratic Formula Solution)",
            "instruction": "ਹੇਠਾਂ ਦਿੱਤੇ ਗਣਿਤਿਕ ਪ੍ਰਸ਼ਨ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਨਾਲ ਪੰਜਾਬੀ ਵਿੱਚ ਹੱਲ ਕਰੋ।",
            "problem_statement": norm(f"ਦੋ-ਘਾਤੀ ਸਮੀਕਰਨ {eq_str} ਦੇ ਮੂਲ (Roots) ਦੋ-ਘਾਤੀ ਸੂਤਰ (Quadratic Formula) ਰਾਹੀਂ ਪਤਾ ਕਰੋ।"),
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਮਿਆਰੀ ਰੂਪ ਨਾਲ ਤੁਲਨਾ): ਸਮੀਕਰਨ ax² + bx + c = 0 ਨਾਲ ਤੁਲਨਾ ਕਰਨ 'ਤੇ: a = {a}, b = {b}, c = {c}।"),
                norm(f"ਕਦਮ ੨ (ਡਿਸਕ੍ਰਿਮੀਨੈਂਟ D ਕੱਢੋ): D = b² - 4ac = ({b})² - 4({a})({c}) = {b**2} - {4*a*c} = {disc}। ਕਿਉਂਕਿ D > 0 ਹੈ, ਇਸ ਲਈ ਦੋ ਅਸਲ ਅਤੇ ਵੱਖਰੇ ਮੂਲ ਹੋਣਗੇ।"),
                norm(f"ਕਦਮ ੩ (ਸੂਤਰ ਲਗਾਓ): x = [-b ± √D] / 2a = [-({b}) ± √{disc}] / (2 × {a}) = [{abs(b)} ± {int(disc**0.5)}] / {2*a}।"),
                norm(f"ਕਦਮ ੪ (ਦੋਵੇਂ ਮੁੱਲ ਪ੍ਰਾਪਤ ਕਰੋ): x₁ = ({abs(b)} + {int(disc**0.5)}) / {2*a} = {r2}, ਅਤੇ x₂ = ({abs(b)} - {int(disc**0.5)}) / {2*a} = {r1}।")
            ],
            "mathematical_formulation": f"x = [-b ± √(b² - 4ac)] / 2a = {r1}, {r2}",
            "final_answer": norm(f"ਸਮੀਕਰਨ {eq_str} ਦੇ ਮੂਲ x = {r1} ਅਤੇ x = {r2} ਹਨ।")
        })
        current_id += 1

    # 2. Physics: Ohm's Law & Circuits
    circuits = [
        (12, 4, 3, "12V", "4Ω"),
        (24, 6, 4, "24V", "6Ω"),
        (220, 22, 10, "220V", "22Ω"),
        (9, 3, 3, "9V", "3Ω"),
        (48, 12, 4, "48V", "12Ω"),
        (100, 20, 5, "100V", "20Ω"),
        (230, 46, 5, "230V", "46Ω"),
        (12, 2, 6, "12V", "2Ω")
    ]

    for v, r, i, v_str, r_str in circuits:
        power = v * i
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Electromagnetism & Circuit Physics",
            "sub_topic": "ਓਹਮ ਦਾ ਨਿਯਮ ਅਤੇ ਬਿਜਲਈ ਸ਼ਕਤੀ (Ohm's Law & Electrical Power)",
            "problem_statement": norm(f"ਇੱਕ ਸਰਕਟ ਵਿੱਚ {v_str} ਦੀ ਵੋਲਟੇਜ (V) ਅਤੇ {r_str} ਦਾ ਰੋਧ (Resistance R) ਜੁੜਿਆ ਹੋਇਆ ਹੈ। ਸਰਕਟ ਵਿੱਚੋਂ ਲੰਘਣ ਵਾਲਾ ਕਰੰਟ (Current I) ਅਤੇ ਖਪਤ ਹੋਣ ਵਾਲੀ ਬਿਜਲਈ ਸ਼ਕਤੀ (Power P) ਪਤਾ ਕਰੋ।"),
            "instruction": "ਹੇਠਾਂ ਦਿੱਤੇ ਭੌਤਿਕ ਵਿਗਿਆਨ ਦੇ ਸਵਾਲ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਦਿੱਤੇ ਮੁੱਲ ਲਿਖੋ): ਵੋਲਟੇਜ V = {v} Volts, ਰੋਧ R = {r} Ohms।"),
                norm(f"ਕਦਮ ੨ (ਓਹਮ ਦਾ ਨਿਯਮ ਲਗਾਓ): I = V / R = {v} / {r} = {i} Amperes (A)।"),
                norm(f"ਕਦਮ ੩ (ਬਿਜਲਈ ਸ਼ਕਤੀ ਫਾਰਮੂਲਾ): Power P = V × I = {v} × {i} = {power} Watts (W) ਜਾਂ P = I² × R = ({i})² × {r} = {power} W।"),
                norm(f"ਕਦਮ ੪ (ਸਿੱਟਾ): ਸਰਕਟ ਵਿੱਚ ਕਰੰਟ {i} A ਹੈ ਅਤੇ ਕੁੱਲ ਸ਼ਕਤੀ ਖਪਤ {power} ਵਾਟ ਹੈ।")
            ],
            "mathematical_formulation": f"I = V / R = {i} A,  P = V · I = {power} W",
            "final_answer": norm(f"ਸਰਕਟ ਵਿੱਚ ਕਰੰਟ I = {i} A ਅਤੇ ਪਾਵਰ P = {power} W ਹੈ।")
        })
        current_id += 1

    # 3. Chemistry: Molarity & Chemical Concentrations
    solutions = [
        ("NaCl (ਲੂਣ)", 58.5, 58.5, 1.0, 1.0),
        ("NaOH (ਸੋਡੀਅਮ ਹਾਈਡ੍ਰੋਕਸਾਈਡ)", 40.0, 20.0, 0.5, 1.0),
        ("HCl (ਹਾਈਡ੍ਰੋਕਲੋਰਿਕ ਐਸਿਡ)", 36.5, 73.0, 1.0, 2.0),
        ("C6H12O6 (ਗਲੂਕੋਜ਼)", 180.0, 90.0, 0.5, 1.0),
        ("H2SO4 (ਸਲਫਿਊਰਿਕ ਐਸਿਡ)", 98.0, 49.0, 1.0, 0.5)
    ]

    for comp, molar_mass, mass_given, vol_litres, expected_m in solutions:
        moles = mass_given / molar_mass
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Physical Chemistry & Solutions",
            "sub_topic": "ਮੋਲੈਰਿਟੀ ਅਤੇ ਰਸਾਇਣਕ ਸੰਘਣਤਾ (Molarity Calculation)",
            "problem_statement": norm(f"ਜੇਕਰ {mass_given} ਗ੍ਰਾਮ {comp} (ਮੋਲਰ ਪੁੰਜ = {molar_mass} g/mol) ਨੂੰ ਪਾਣੀ ਵਿੱਚ ਘੋਲ ਕੇ {vol_litres} ਲੀਟਰ ਘੋਲ ਬਣਾਇਆ ਜਾਵੇ, ਤਾਂ ਘੋਲ ਦੀ ਮੋਲੈਰਿਟੀ (Molarity M) ਕਿੰਨੀ ਹੋਵੇਗੀ?"),
            "instruction": "ਹੇਠਾਂ ਦਿੱਤੇ ਰਸਾਇਣ ਵਿਗਿਆਨ ਦੇ ਪ੍ਰਸ਼ਨ ਦਾ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਤਿਆਰ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਮੋਲਜ਼ ਦੀ ਗਿਣਤੀ ਕੱਢੋ): Moles n = ਦਿੱਤਾ ਪੁੰਜ (Mass) / ਮੋਲਰ ਪੁੰਜ (Molar Mass) = {mass_given} / {molar_mass} = {moles:.2f} moles।"),
                norm(f"ਕਦਮ ੨ (ਮੋਲੈਰਿਟੀ ਫਾਰਮੂਲਾ): Molarity M = ਘੁਲਣਸ਼ੀਲ ਦੇ ਮੋਲ (Moles of solute) / ਘੋਲ ਦਾ ਆਇਤਨ ਲੀਟਰਾਂ ਵਿੱਚ (Volume in Liters)।"),
                norm(f"ਕਦਮ ੩ (ਗਣਨਾ): M = {moles:.2f} moles / {vol_litres} L = {expected_m:.2f} mol/L (M)।"),
                norm(f"ਕਦਮ ੪ (ਸਿੱਟਾ): ਤਿਆਰ ਘੋਲ ਦੀ ਸੰਘਣਤਾ {expected_m:.2f} M ਹੈ।")
            ],
            "mathematical_formulation": f"M = n / V = ({mass_given} / {molar_mass}) / {vol_litres} = {expected_m:.2f} M",
            "final_answer": norm(f"ਘੋਲ ਦੀ ਮੋਲੈਰਿਟੀ {expected_m:.2f} M (mol/L) ਹੈ।")
        })
        current_id += 1

    # 4. Computer Science: Complexity & Data Structures
    algos = [
        ("Merge Sort", "O(N log N)", "O(N log N)", "O(N)", "Divide and Conquer ਰਾਹੀਂ ਸੂਚੀ ਨੂੰ ਅੱਧ ਵਿੱਚ ਵੰਡ ਕੇ ਮਿਲਾਉਣਾ"),
        ("Quick Sort", "O(N log N)", "O(N²)", "O(log N)", "ਪਿਵਟ (Pivot) ਐਲੀਮੈਂਟ ਚੁਣ ਕੇ ਪਾਰਟੀਸ਼ਨ ਕਰਨਾ"),
        ("Bubble Sort", "O(N²)", "O(N²)", "O(1)", "ਨਾਲ ਲੱਗਦੇ ਐਲੀਮੈਂਟਾਂ ਦੀ ਆਪਸੀ ਤੁਲਨਾ ਅਤੇ ਅਦਲਾ-ਬਦਲੀ (Swapping)"),
        ("Linear Search", "O(N)", "O(N)", "O(1)", "ਪਹਿਲੇ ਤੋਂ ਆਖ਼ਰੀ ਐਲੀਮੈਂਟ ਤੱਕ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਚੈੱਕ ਕਰਨਾ"),
        ("Hash Table Lookup", "O(1)", "O(N)", "O(N)", "ਹੈਸ਼ ਫੰਕਸ਼ਨ ਰਾਹੀਂ ਸਿੱਧਾ ਇੰਡੈਕਸ ਕੈਲਕੂਲੇਟ ਕਰਨਾ")
    ]

    for name, avg_comp, worst_comp, space_comp, desc in algos:
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Algorithms & Computational Complexity",
            "sub_topic": f"{name} ਦੀ ਟਾਈਮ ਅਤੇ ਸਪੇਸ ਕੰਪਲੈਕਸਿਟੀ",
            "problem_statement": norm(f"ਕੰਪਿਊਟਰ ਸਾਇੰਸ ਵਿੱਚ '{name}' ਐਲਗੋਰਿਦਮ ਦੀ ਔਸਤ (Average) ਅਤੇ ਸਭ ਤੋਂ ਮਾੜੀ (Worst-case) ਟਾਈਮ ਕੰਪਲੈਕਸਿਟੀ ਕੀ ਹੈ ਅਤੇ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ?"),
            "instruction": "ਐਲਗੋਰਿਦਮ ਦੀ ਗਣਿਤਿਕ ਕੰਪਲੈਕਸਿਟੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪੰਜਾਬੀ ਵਿੱਚ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਕਾਰਜ ਪ੍ਰਣਾਲੀ): {name} ਦਾ ਮੁੱਖ ਸਿਧਾਂਤ '{desc}' ਹੈ।"),
                norm(f"ਕਦਮ ੨ (ਔਸਤ ਟਾਈਮ ਕੰਪਲੈਕਸਿਟੀ): ਆਮ ਹਾਲਤਾਂ ਵਿੱਚ ਇਹ ਐਲਗੋਰਿਦਮ {avg_comp} ਸਮਾਂ ਲੈਂਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੩ (ਸਭ ਤੋਂ ਮਾੜੀ ਹਾਲਤ / Worst-case): ਜਦੋਂ ਇਨਪੁਟ ਡਾਟਾ ਪ੍ਰਤੀਕੂਲ ਹੋਵੇ ਤਾਂ ਇਸਦੀ ਕੰਪਲੈਕਸਿਟੀ {worst_comp} ਤੱਕ ਚਲੀ ਜਾਂਦੀ ਹੈ।"),
                norm(f"ਕਦਮ ੪ (ਸਪੇਸ ਕੰਪਲੈਕਸਿਟੀ): ਵਾਧੂ ਮੈਮੋਰੀ ਖਪਤ {space_comp} ਹੈ।")
            ],
            "mathematical_formulation": f"Average: {avg_comp}, Worst: {worst_comp}, Space: {space_comp}",
            "final_answer": norm(f"{name} ਦੀ ਔਸਤ ਕੰਪਲੈਕਸਿਟੀ {avg_comp} ਅਤੇ ਸਭ ਤੋਂ ਮਾੜੀ ਕੰਪਲੈਕਸਿਟੀ {worst_comp} ਹੈ।")
        })
        current_id += 1

    # 5. Trigonometry & Geometry in Punjabi
    trig_problems = [
        ("sin(30°) + cos(60°)", "1/2 + 1/2 = 1", 1.0, "30° ਦਾ ਸਾਈਨ ਅਤੇ 60° ਦਾ ਕੋਸਾਈਨ ਦੋਵੇਂ 1/2 ਹੁੰਦੇ ਹਨ"),
        ("sin²(45°) + cos²(45°)", "(1/√2)² + (1/√2)² = 1/2 + 1/2 = 1", 1.0, "ਸਰਬਸਮਤਾ sin²θ + cos²θ = 1 ਹਮੇਸ਼ਾ ਲਾਗੂ ਹੁੰਦੀ ਹੈ"),
        ("tan(45°) + cot(45°)", "1 + 1 = 2", 2.0, "45° 'ਤੇ ਟੈਨਜੈਂਟ ਅਤੇ ਕੋਟੈਨਜੈਂਟ ਦੋਵੇਂ 1 ਹੁੰਦੇ ਹਨ"),
        ("2 · sin(30°) · cos(30°)", "2 · (1/2) · (√3/2) = √3/2", 0.866, "ਦੂਹਰੇ ਕੋਣ ਦਾ ਸੂਤਰ sin(2θ) = 2 sin θ cos θ = sin(60°) = √3/2"),
        ("sec²(60°) - tan²(60°)", "(2)² - (√3)² = 4 - 3 = 1", 1.0, "ਸਰਬਸਮਤਾ sec²θ - tan²θ = 1 ਲਾਗੂ ਹੁੰਦੀ ਹੈ")
    ]

    for expr, calc_step, res_val, expl in trig_problems:
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Trigonometry & Pure Mathematics",
            "sub_topic": "ਤਿਕੋਣਮਿਤੀ ਸਰਬਸਮਤਾਵਾਂ ਅਤੇ ਮੁੱਲ (Trigonometric Identities)",
            "problem_statement": norm(f"ਤਿਕੋਣਮਿਤੀ ਵਿਅੰਜਕ {expr} ਦਾ ਮੁੱਲ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਨਾਲ ਪਤਾ ਕਰੋ।"),
            "instruction": "ਤਿਕੋਣਮਿਤੀ ਸਮੱਸਿਆ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਸਟੈਂਡਰਡ ਕੋਣਾਂ ਦੇ ਮੁੱਲ ਪਛਾਣੋ): ਦਿੱਤਾ ਵਿਅੰਜਕ {expr} ਹੈ।"),
                norm(f"ਕਦਮ ੨ (ਸੂਤਰ ਅਤੇ ਗਣਨਾ): {calc_step}।"),
                norm(f"ਕਦਮ ੩ (ਨਿਯਮ ਵਿਆਖਿਆ): {expl}।"),
                norm(f"ਕਦਮ ੪ (ਸਿੱਟਾ): ਅੰਤਮ ਮੁੱਲ {res_val} ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ।")
            ],
            "mathematical_formulation": f"{expr} = {res_val}",
            "final_answer": norm(f"{expr} ਦਾ ਅੰਤਮ ਮੁੱਲ {res_val} ਹੈ।")
        })
        current_id += 1

    # 7. Calculus: Definite and Indefinite Integration
    integrals = [
        ("∫ (3x² + 4x + 5) dx", "[x³ + 2x² + 5x] + C", "ਪਾਵਰ ਰੂਲ ∫ x^n dx = (x^(n+1))/(n+1)"),
        ("∫ cos(2x) dx", "(1/2) · sin(2x) + C", "ਸਬਸਟੀਟਿਊਸ਼ਨ ਵਿਧੀ u = 2x, du = 2 dx"),
        ("∫ (1/x) dx (x > 0)", "ln|x| + C", "ਨੈਚੁਰਲ ਲੌਗਾਰਿਦਮ ਦਾ ਮਿਆਰੀ ਇੰਟੀਗ੍ਰਲ ਨਿਯਮ"),
        ("∫₀¹ (6x² + 2x) dx", "[2x³ + x²]₀¹ = (2(1)³ + (1)²) - 0 = 3", "ਫੰਡਾਮੈਂਟਲ ਥਿਊਰਮ ਆਫ ਕੈਲਕੂਲਸ [F(b) - F(a)]"),
        ("∫ e^(3x) dx", "(1/3) · e^(3x) + C", "ਐਕਸਪੋਨੈਂਸ਼ੀਅਲ ਫੰਕਸ਼ਨ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨਿਯਮ")
    ]

    for expr, sol, rule in integrals:
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Calculus & Integral Mathematics",
            "sub_topic": "ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ ਐਂਟੀ-ਡੈਰੀਵੇਟਿਵ (Integration Rules)",
            "problem_statement": norm(f"ਗਣਿਤਿਕ ਇੰਟੀਗ੍ਰਲ {expr} ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਨਾਲ ਹੱਲ ਕਰੋ।"),
            "instruction": "ਕੈਲਕੂਲਸ ਇੰਟੀਗ੍ਰਲ ਦਾ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਪੰਜਾਬੀ ਵਿੱਚ ਤਿਆਰ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਸਮੱਸਿਆ ਦੀ ਪਛਾਣ): ਦਿੱਤਾ ਗਿਆ ਇੰਟੀਗ੍ਰਲ {expr} ਹੈ।"),
                norm(f"ਕਦਮ ੨ (ਲਾਗੂ ਨਿਯਮ): ਇਸ ਵਿੱਚ '{rule}' ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।"),
                norm(f"ਕਦਮ ੩ (ਗਣਨਾ): ਹਰੇਕ ਪਦ (Term) ਨੂੰ ਵੱਖਰੇ ਤੌਰ 'ਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ 'ਤੇ ਸਾਨੂੰ {sol} ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੪ (ਸਿੱਟਾ): ਅੰਤਮ ਉੱਤਰ {sol} ਹੈ।")
            ],
            "mathematical_formulation": f"{expr} = {sol}",
            "final_answer": norm(f"ਇੰਟੀਗ੍ਰਲ {expr} ਦਾ ਹੱਲ {sol} ਹੈ।")
        })
        current_id += 1

    # 8. Modern Physics: Special Relativity & Nuclear Physics
    modern_physics = [
        ("Mass-Energy Equivalence", "E = m · c²", "1 ਗ੍ਰਾਮ (0.001 kg) ਪਦਾਰਥ ਕਿੰਨੀ ਊਰਜਾ ਪੈਦਾ ਕਰਦਾ ਹੈ? (c = 3 × 10⁸ m/s)", "E = 0.001 × (3 × 10⁸)² = 9 × 10¹³ Joules", "ਪੁੰਜ ਨੂੰ ਊਰਜਾ ਵਿੱਚ ਬਦਲਣ 'ਤੇ 90 ਟੈਰਾਜੂਲ (9 × 10¹³ J) ਊਰਜਾ ਨਿਕਲਦੀ ਹੈ।"),
        ("Time Dilation", "t' = t / √(1 - v²/c²)", "ਜੇਕਰ ਇੱਕ ਪੁਲਾੜ ਯਾਨ 0.8c ਦੀ ਰਫ਼ਤਾਰ ਨਾਲ ਚੱਲ ਰਿਹਾ ਹੈ ਅਤੇ ਯਾਨ ਵਿੱਚ 1 ਘੰਟਾ ਬੀਤਦਾ ਹੈ, ਤਾਂ ਧਰਤੀ 'ਤੇ ਕਿੰਨਾ ਸਮਾਂ ਬੀਤੇਗਾ?", "Lorentz factor γ = 1 / √(1 - 0.8²) = 1 / √(0.36) = 1 / 0.6 = 1.667 ➔ t_earth = 1 × 1.667 = 1.67 ਘੰਟੇ (100 ਮਿੰਟ)", "ਧਰਤੀ ਉੱਤੇ 1 ਘੰਟਾ 40 ਮਿੰਟ (1.67 ਘੰਟੇ) ਬੀਤਣਗੇ।"),
        ("Radioactive Decay & Half-Life", "N(t) = N₀ · (1/2)^(t / T_half)", "ਇੱਕ ਰੇਡੀਓਐਕਟਿਵ ਤੱਤ ਦਾ ਹਾਫ਼-ਲਾਈਫ਼ (Half-Life) 5 ਸਾਲ ਹੈ। 100 ਗ੍ਰਾਮ ਨਮੂਨੇ ਵਿੱਚੋਂ 15 ਸਾਲਾਂ ਬਾਅਦ ਕਿੰਨਾ ਬਚੇਗਾ?", "ਅੱਧ-ਜੀਵਨ ਚੱਕਰਾਂ ਦੀ ਗਿਣਤੀ n = 15 / 5 = 3। ਬਾਕੀ ਪੁੰਜ N = 100 × (1/2)³ = 100 / 8 = 12.5 ਗ੍ਰਾਮ", "15 ਸਾਲਾਂ ਬਾਅਦ ਕੇਵਲ 12.5 ਗ੍ਰਾਮ ਤੱਤ ਬਾਕੀ ਬਚੇਗਾ।"),
        ("Photoelectric Effect", "E_photon = h · ν = Φ + KE_max", "ਫੋਟੋਇਲੈਕਟ੍ਰਿਕ ਪ੍ਰਭਾਵ ਵਿੱਚ ਆਇਨਸਟਾਈਨ ਦੀ ਸਮੀਕਰਨ ਦਾ ਭੌਤਿਕ ਅਰਥ ਕੀ ਹੈ?", "ਆਉਣ ਵਾਲੇ ਫੋਟੋਨ ਦੀ ਊਰਜਾ (hν) ਇਲੈਕਟ੍ਰਾਨ ਨੂੰ ਧਾਤੂ ਵਿੱਚੋਂ ਬਾਹਰ ਕੱਢਣ (Work Function Φ) ਅਤੇ ਬਾਕੀ ਉਸਨੂੰ ਗਤੀ ਊਰਜਾ (KE) ਦੇਣ ਵਿੱਚ ਖ਼ਰਚ ਹੁੰਦੀ ਹੈ।", "ਇਹ ਸਾਬਤ ਕਰਦਾ ਹੈ ਕਿ ਪ੍ਰਕਾਸ਼ ਕਣਾਂ (Photons) ਦੇ ਰੂਪ ਵਿੱਚ ਕੁਆਂਟਾਇਜ਼ਡ ਹੁੰਦਾ ਹੈ।")
    ]

    for topic, formula, prob, calc, ans in modern_physics:
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Modern Physics & Relativity",
            "sub_topic": topic,
            "problem_statement": norm(f"ਆਧੁਨਿਕ ਭੌਤਿਕ ਵਿਗਿਆਨ ਵਿੱਚ {prob}"),
            "instruction": "ਭੌਤਿਕ ਵਿਗਿਆਨ ਦੀ ਸਮੱਸਿਆ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਤਰਕ ਨਾਲ ਹੱਲ ਕਰੋ।",
            "step_by_step_reasoning": [
                norm(f"ਕਦਮ ੧ (ਸਿਧਾਂਤ ਅਤੇ ਸੂਤਰ): ਇਸ ਵਿੱਚ {topic} ਦਾ ਨਿਯਮ '{formula}' ਲਾਗੂ ਹੁੰਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੨ (ਮੁੱਲ ਰੱਖਣਾ ਅਤੇ ਗਣਨਾ): {calc}।"),
                norm(f"ਕਦਮ ੩ (ਭੌਤਿਕ ਵਿਆਖਿਆ): ਕੁਦਰਤ ਦਾ ਇਹ ਨਿਯਮ ਪੁੰਜ, ਊਰਜਾ, ਅਤੇ ਸਮੇਂ ਦੇ ਸੰਦਰਭੀ ਸੰਬੰਧਾਂ ਨੂੰ ਪ੍ਰਗਟ ਕਰਦਾ ਹੈ।"),
                norm(f"ਕਦਮ ੪ (ਸਿੱਟਾ): {ans}")
            ],
            "mathematical_formulation": formula,
            "final_answer": norm(ans)
        })
        current_id += 1

    # 9. Probability & Statistics
    stats_problems = [
        ("Bayes Theorem", "P(A|B) = [P(B|A) · P(A)] / P(B)", "ਇੱਕ ਮੈਡੀਕਲ ਟੈਸਟ ਬਿਮਾਰੀ ਹੋਣ 'ਤੇ 99% ਸਹੀ ਨਤੀਜਾ (Sensitivity) ਦਿੰਦਾ ਹੈ ਅਤੇ ਤੰਦਰੁਸਤ ਵਿਅਕਤੀ ਲਈ 95% ਸਹੀ (Specificity) ਹੈ। ਜੇਕਰ ਆਬਾਦੀ ਵਿੱਚ ਬਿਮਾਰੀ ਦਾ ਪ੍ਰਸਾਰ 1% (Prevalence = 0.01) ਹੋਵੇ, ਤਾਂ ਪਾਜ਼ਿਟਿਵ ਟੈਸਟ ਵਾਲੇ ਵਿਅਕਤੀ ਨੂੰ ਅਸਲ ਵਿੱਚ ਬਿਮਾਰੀ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ (PPV) ਕੀ ਹੈ?", [
            "ਕਦਮ ੧: P(Disease D) = 0.01, P(No Disease D') = 0.99।",
            "ਕਦਮ ੨: P(Pos|D) = 0.99, P(Pos|D') = 1 - 0.95 = 0.05 (False Positive rate) ।",
            "ਕਦਮ ੩: ਕੁੱਲ ਪਾਜ਼ਿਟਿਵ ਸੰਭਾਵਨਾ P(Pos) = (0.99 × 0.01) + (0.05 × 0.99) = 0.0099 + 0.0495 = 0.0594।",
            "ਕਦਮ ੪: ਬੇਅਸ ਥਿਊਰਮ ਅਨੁਸਾਰ P(D|Pos) = (0.99 × 0.01) / 0.0594 = 0.0099 / 0.0594 ≈ 0.1667 (16.67%)।"
        ], "ਪਾਜ਼ਿਟਿਵ ਟੈਸਟ ਆਉਣ ਦੇ ਬਾਵਜੂਦ ਅਸਲ ਬਿਮਾਰੀ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ ਲਗਭਗ 16.67% ਹੈ।"),
        ("Binomial Distribution", "P(X = k) = C(n, k) · p^k · (1-p)^(n-k)", "ਇੱਕ ਨਿਰਪੱਖ ਸਿੱਕੇ ਨੂੰ 5 ਵਾਰ ਉਛਾਲਿਆ ਜਾਂਦਾ ਹੈ। ਠੀਕ 3 ਵਾਰ ਚਿੱਤ (Heads) ਆਉਣ ਦੀ ਸੰਭਾਵਨਾ ਕੀ ਹੈ?", [
            "ਕਦਮ ੧: n = 5 (ਕੁੱਲ ਉਛਾਲਾਂ), k = 3 (ਸਫ਼ਲਤਾਵਾਂ), p = 0.5 (ਚਿੱਤ ਆਉਣ ਦੀ ਸੰਭਾਵਨਾ)।",
            "ਕਦਮ ੨: ਕੰਬੀਨੇਸ਼ਨ C(5, 3) = 5! / (3! × 2!) = (5 × 4) / 2 = 10।",
            "ਕਦਮ ੩: P(X = 3) = 10 × (0.5)³ × (0.5)² = 10 × (0.5)⁵ = 10 × (1/32) = 10/32 = 5/16 = 0.3125 (31.25%)।",
            "ਕਦਮ ੪: ਠੀਕ 3 ਵਾਰ ਚਿੱਤ ਆਉਣ ਦੀ ਸੰਭਾਵਨਾ 31.25% ਹੈ।"
        ], "5 ਵਿੱਚੋਂ ਠੀਕ 3 ਵਾਰ ਚਿੱਤ ਆਉਣ ਦੀ ਸੰਭਾਵਨਾ 5/16 (31.25%) ਹੈ।")
    ]

    for name, form, problem_desc, steps, ans_str in stats_problems:
        expanded.append({
            "id": f"punjabi_stem_{current_id:05d}",
            "domain": "Probability & Mathematical Statistics",
            "sub_topic": name,
            "problem_statement": norm(problem_desc),
            "instruction": "ਸੰਭਾਵਨਾ ਅਤੇ ਅੰਕੜਾ ਵਿਗਿਆਨ ਸਮੱਸਿਆ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਹੱਲ ਕਰੋ।",
            "step_by_step_reasoning": [norm(s) for s in steps],
            "mathematical_formulation": form,
            "final_answer": norm(ans_str)
        })
        current_id += 1

    return expanded

def main():
    output_dir = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "punjabi_stem_frontier_cot_corpus.jsonl")

    base_corpus = build_stem_core()
    full_corpus = generate_expanded_stem_corpus(base_corpus)

    with open(output_file, "w", encoding="utf-8") as f:
        for row in full_corpus:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"✅ Successfully generated Punjabi STEM Frontier CoT Corpus!")
    print(f"📁 Target file: {output_file}")
    print(f"📊 Total deep reasoning problems: {len(full_corpus)}")

if __name__ == "__main__":
    main()
