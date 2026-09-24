#!/usr/bin/env python3
"""
AMRIT Punjabi Clinical Dialogue & Medical Diagnosis Dataset Generator
Author: Gurpreet Singh Dhillon (Nam-toon-studio) / AMRIT Research OS Team
License: Apache-2.0 / MIT

Curates a gold-standard, evidence-based medical consultation and clinical reasoning
corpus in pure Punjabi (Gurmukhi) for AMRIT AI Doctor & Sehaj 86M fine-tuning.

Covers:
1. Endocrinology & Diabetes (ਸ਼ੂਗਰ, ਥਾਇਰਾਇਡ)
2. Cardiology & Hypertension (ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ, ਦਿਲ ਦੀ ਸਿਹਤ)
3. Pulmonology & Respiratory (ਦਮਾ, ਖੰਘ, ਨਮੂਨੀਆ, ਐਲਰਜੀ)
4. Gastroenterology (ਪੇਟ ਗੈਸ, ਐਸਿਡਿਟੀ, ਪੀਲੀਆ, ਲਿਵਰ)
5. Hematology & Anemia (ਅਨੀਮੀਆ, ਖੂਨ ਦੀ ਘਾਟ, ਪਲੇਟਲੈੱਟਸ)
6. Dermatology (ਚਮੜੀ ਰੋਗ, ਦਾਦ, ਖਾਰਸ਼, ਐਲਰਜੀ)
7. Pediatrics & Child Health (ਬੱਚਿਆਂ ਦੇ ਰੋਗ, ਟੀਕਾਕਰਨ)
8. Neurology & Mental Health (ਸਿਰ ਦਰਦ, ਮਾਈਗ੍ਰੇਨ, ਤਣਾਅ, ਅਨੀਂਦਰਾ)
9. Infectious Diseases & Fevers (ਡੇਂਗੂ, ਮਲੇਰੀਆ, ਟਾਈਫਾਈਡ, ਫਲੂ)
10. Preventive Health & Nutrition (ਖੁਰਾਕੀ ਪਰਹੇਜ਼, ਘਰੇਲੂ ਸਾਵਧਾਨੀਆਂ)
"""

import json
import os
import unicodedata
from typing import List, Dict, Any

def norm(text: str) -> str:
    return unicodedata.normalize('NFC', text.strip())

def build_clinical_core() -> List[Dict[str, Any]]:
    dataset = []
    idx = 1

    clinical_cases = [
        # 1. Diabetes / Endocrinology
        {
            "domain": "Endocrinology & Metabolic Health",
            "age": "48 ਸਾਲ",
            "gender": "ਪੁਰਸ਼",
            "chief_complaint": "ਵਾਰ-ਵਾਰ ਪਿਸ਼ਾਬ ਆਉਣਾ, ਬਹੁਤ ਜ਼ਿਆਦਾ ਪਿਆਸ ਲੱਗਣਾ ਅਤੇ ਅਚਾਨਕ ਭਾਰ ਘਟਣਾ।",
            "patient_query": "ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਨੂੰ ਪਿਛਲੇ ਵੀਹ ਦਿਨਾਂ ਤੋਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਪਿਆਸ ਲੱਗ ਰਹੀ ਹੈ, ਰਾਤ ਨੂੰ ਕਈ ਵਾਰ ਪਿਸ਼ਾਬ ਜਾਣਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਥਕਾਵਟ ਬਣੀ ਰਹਿੰਦੀ ਹੈ। ਮੈਨੂੰ ਕੀ ਹੋ ਸਕਦਾ ਹੈ?",
            "clinical_assessment": "ਮਰੀਜ਼ ਦੇ ਲੱਛਣ (Polyuria, Polydipsia, Weight loss) ਸ਼ੂਗਰ (Type 2 Diabetes Mellitus) ਦੇ ਕਲਾਸੀਕਲ ਲੱਛਣਾਂ ਵੱਲ ਸੰਕੇਤ ਕਰਦੇ ਹਨ। ਖੂਨ ਵਿੱਚ ਗਲੂਕੋਜ਼ ਵਧਣ ਕਾਰਨ ਗੁਰਦੇ ਵੱਧ ਪਾਣੀ ਬਾਹਰ ਕੱਢਦੇ ਹਨ।",
            "suspected_conditions": ["ਟਾਈਪ 2 ਸ਼ੂਗਰ (Type 2 Diabetes Mellitus)", "ਪ੍ਰੀ-ਡਾਇਬੀਟੀਜ਼", "ਹਾਈਪਰਗਲਾਈਸੀਮੀਆ"],
            "triage_level": "ਮੱਧਮ (Moderate - ੨੪-੪੮ ਘੰਟਿਆਂ ਵਿੱਚ ਡਾਕਟਰੀ ਜਾਂਚ ਜ਼ਰੂਰੀ)",
            "suggested_tests": ["Fasting Blood Sugar (FBS)", "Postprandial Blood Sugar (PPBS)", "HbA1c (੩ ਮਹੀਨਿਆਂ ਦੀ ਔਸਤ ਸ਼ੂਗਰ)", "Urine Routine for Ketones/Glucose"],
            "guidance_and_precautions": "ਮਿੱਠੀਆਂ ਚੀਜ਼ਾਂ, ਖੰਡ, ਗੁੜ, ਕੋਲਡ ਡਰਿੰਕਸ ਅਤੇ ਮੈਦੇ ਤੋਂ ਤੁਰੰਤ ਪਰਹੇਜ਼ ਕਰੋ। ਰੋਜ਼ਾਨਾ ੩੦-੪੦ ਮਿੰਟ ਸੈਰ ਕਰੋ। ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਤੋਂ ਬਿਨਾਂ ਕੋਈ ਅੰਨ੍ਹੇਵਾਹ ਦਵਾਈ ਨਾ ਲਓ।",
            "disclaimer": "ਇਹ ਜਾਣਕਾਰੀ ਕੇਵਲ ਮੈਡੀਕਲ ਸਿੱਖਿਆ ਅਤੇ ਸਲਾਹ ਲਈ ਹੈ। ਸਹੀ ਇਲਾਜ ਲਈ ਨੇੜਲੇ ਮੈਡੀਕਲ ਸੈਂਟਰ ਵਿੱਚ ਖੂਨ ਦੀ ਜਾਂਚ ਕਰਵਾ ਕੇ ਡਾਕਟਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।"
        },
        # 2. Cardiology / Hypertension
        {
            "domain": "Cardiology & Vascular Health",
            "age": "55 ਸਾਲ",
            "gender": "ਇਸਤਰੀ",
            "chief_complaint": "ਸਿਰ ਦੇ ਪਿਛਲੇ ਪਾਸੇ ਭਾਰੀਪਣ, ਚੱਕਰ ਆਉਣਾ ਅਤੇ ਅੱਖਾਂ ਅੱਗੇ ਧੁੰਦਲਾਪਣ।",
            "patient_query": "ਮੈਨੂੰ ਸਵੇਰ ਤੋਂ ਸਿਰ ਦੇ ਪਿਛਲੇ ਪਾਸੇ ਗਰਦਨ ਕੋਲ ਤੇਜ਼ ਦਰਦ ਤੇ ਭਾਰੀਪਣ ਮਹਿਸੂਸ ਹੋ ਰਿਹਾ ਹੈ ਅਤੇ ਚੱਕਰ ਆ ਰਹੇ ਹਨ। ਘਰ ਬੈਠਿਆਂ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?",
            "clinical_assessment": "ਸਿਰ ਦੇ ਪਿਛਲੇ ਹਿੱਸੇ (Occipital region) ਵਿੱਚ ਭਾਰੀਪਣ ਅਤੇ ਚੱਕਰ ਹਾਈ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ (Hypertension) ਦੇ ਮੁੱਖ ਲੱਛਣ ਹਨ। ਇਸਨੂੰ ਅਣਗੌਲਿਆ ਕਰਨ ਨਾਲ ਦਿਲ ਜਾਂ ਦਿਮਾਗ ਦੀਆਂ ਨਾੜਾਂ 'ਤੇ ਦਬਾਅ ਵਧ ਸਕਦਾ ਹੈ।",
            "suspected_conditions": ["ਹਾਈ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ (Essential Hypertension)", "ਸਰਵਾਈਕਲ ਸਪੌਂਡਿਲਾਈਟਿਸ", "ਤਣਾਅ/ਅਨੀਂਦਰਾ"],
            "triage_level": "ਮੱਧਮ ਤੋਂ ਉੱਚ (Moderate to High - ਤੁਰੰਤ ਬੀਪੀ ਚੈੱਕ ਕਰੋ)",
            "suggested_tests": ["Blood Pressure Monitoring (੩ ਵਾਰ ਅਲੱਗ ਸਮੇਂ)", "Lipid Profile (ਕੋਲੈਸਟ੍ਰੋਲ)", "Kidney Function Test (KFT)", "ECG"],
            "guidance_and_precautions": "ਲੂਣ (Sodium) ਦੀ ਵਰਤੋਂ ਤੁਰੰਤ ਘਟਾਓ। ਆਚਾਰ, ਪਾਪੜ, ਨਮਕੀਨ ਭੋਜਨ ਬੰਦ ਕਰੋ। ਸ਼ਾਂਤ ਹੋ ਕੇ ਆਰਾਮ ਕਰੋ। ਜੇਕਰ ਬੀਪੀ ੧੬੦/੧੦੦ ਤੋਂ ਵੱਧ ਆਵੇ ਤਾਂ ਤੁਰੰਤ ਐਮਰਜੈਂਸੀ ਜਾਓ।",
            "disclaimer": "ਐਮਰਜੈਂਸੀ ਹਾਲਤ ਵਿੱਚ ਘਰੇਲੂ ਨੁਸਖਿਆਂ 'ਤੇ ਨਿਰਭਰ ਨਾ ਰਹੋ, ਤੁਰੰਤ ਨਜ਼ਦੀਕੀ ਕਲੀਨਿਕ ਪਹੁੰਚੋ।"
        },
        # 3. Pulmonology / Respiratory
        {
            "domain": "Pulmonology & Respiratory Medicine",
            "age": "32 ਸਾਲ",
            "gender": "ਪੁਰਸ਼",
            "chief_complaint": "ਸੁੱਕੀ ਖੰਘ, ਛਾਤੀ ਵਿੱਚੋਂ ਸੀਟੀ ਵਰਗੀ ਆਵਾਜ਼ (Wheezing) ਅਤੇ ਸਾਹ ਲੈਣ ਵਿੱਚ ਤਕਲੀਫ਼।",
            "patient_query": "ਡਾਕਟਰ ਸਾਹਿਬ, ਰਾਤ ਵੇਲੇ ਠੰਢ ਵਿੱਚ ਮੇਰਾ ਸਾਹ ਘੁੱਟਣ ਲੱਗਦਾ ਹੈ ਅਤੇ ਛਾਤੀ ਵਿੱਚੋਂ ਸੀਟੀ ਵਰਗੀ ਆਵਾਜ਼ ਆਉਂਦੀ ਹੈ। ਖੰਘ ਵੀ ਨਹੀਂ ਹਟ ਰਹੀ।",
            "clinical_assessment": "ਛਾਤੀ ਵਿੱਚੋਂ Wheezing ਅਤੇ ਰਾਤ ਨੂੰ ਸਾਹ ਚੜ੍ਹਨਾ ਬ੍ਰੌਂਕੀਅਲ ਅਸਥਮਾ (Asthma) ਜਾਂ ਐਲਰਜੀਕ ਬ੍ਰੌਨਕਾਈਟਿਸ ਦੇ ਲੱਛਣ ਹਨ, ਜਿਸ ਵਿੱਚ ਸਾਹ ਨਾਲੀਆਂ ਸੁੰਗੜ ਜਾਂਦੀਆਂ ਹਨ।",
            "suspected_conditions": ["ਦਮਾ / ਅਸਥਮਾ (Bronchial Asthma)", "ਐਲਰਜੀਕ ਬ੍ਰੌਨਕਾਈਟਿਸ (Allergic Bronchitis)", "ਧੂੜ-ਮਿੱਟੀ ਤੋਂ ਐਲਰਜੀ"],
            "triage_level": "ਮੱਧਮ (ਜੇਕਰ ਸਾਹ ਬਹੁਤ ਔਖਾ ਆਵੇ ਤਾਂ ਤੁਰੰਤ ਐਮਰਜੈਂਸੀ)",
            "suggested_tests": ["Spirometry / Pulmonary Function Test (PFT)", "Chest X-Ray (PA View)", "Complete Blood Count (Absolute Eosinophil Count - AEC)"],
            "guidance_and_precautions": "ਧੂੰਏਂ, ਧੂੜ-ਮਿੱਟੀ, ਪਰਾਲੀ ਦੇ ਧੂੰਏਂ ਅਤੇ ਠੰਢੇ ਪਾਣੀ/ਆਈਸਕ੍ਰੀਮ ਤੋਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਬਚੋ। ਗਰਮ ਪਾਣੀ ਦੀ ਭਾਫ਼ (Steam Inhalation) ਲਓ। ਮਾਸਕ ਦੀ ਵਰਤੋਂ ਕਰੋ।",
            "disclaimer": "ਜੇਕਰ ਬੁੱਲ੍ਹ ਨੀਲੇ ਪੈਣ ਜਾਂ ਸਾਹ ਬਿਲਕੁਲ ਰੁਕਦਾ ਜਾਪੇ ਤਾਂ ਬਿਨਾਂ ਦੇਰੀ ਹਸਪਤਾਲ ਜਾਓ।"
        },
        # 4. Hematology / Anemia
        {
            "domain": "Hematology & Blood Health",
            "age": "24 ਸਾਲ",
            "gender": "ਇਸਤਰੀ",
            "chief_complaint": "ਹਮੇਸ਼ਾ ਥਕਾਵਟ ਰਹਿਣਾ, ਚਿਹਰਾ ਪੀਲਾ ਪੈਣਾ, ਨਹੁੰ ਕਮਜ਼ੋਰ ਹੋਣਾ ਅਤੇ ਦਿਲ ਦੀ ਧੜਕਣ ਤੇਜ਼ ਹੋਣੀ।",
            "patient_query": "ਮੈਨੂੰ ਥੋੜ੍ਹਾ ਜਿਹਾ ਤੁਰਨ 'ਤੇ ਵੀ ਸਾਹ ਚੜ੍ਹ ਜਾਂਦਾ ਹੈ, ਚੱਕਰ ਆਉਂਦੇ ਹਨ ਅਤੇ ਪਿੰਡੇ ਵਿੱਚ ਜਾਨ ਨਹੀਂ ਲੱਗਦੀ। ਮੇਰੀ ਰਿਪੋਰਟ ਵਿੱਚ ਹੀਮੋਗਲੋਬਿਨ ੭.੨ ਆਇਆ ਹੈ।",
            "clinical_assessment": "ਹੀਮੋਗਲੋਬਿਨ ੭.੨ g/dL ਗੰਭੀਰ ਖੂਨ ਦੀ ਘਾਟ (Moderate to Severe Iron Deficiency Anemia) ਦਰਸਾਉਂਦਾ ਹੈ। ਆਇਰਨ ਦੀ ਕਮੀ ਕਾਰਨ ਸਰੀਰ ਦੇ ਅੰਗਾਂ ਤੱਕ ਆਕਸੀਜਨ ਪੂਰੀ ਨਹੀਂ ਪਹੁੰਚ ਰਹੀ।",
            "suspected_conditions": ["ਆਇਰਨ ਦੀ ਘਾਟ ਵਾਲਾ ਅਨੀਮੀਆ (Iron Deficiency Anemia)", "ਪੋਸ਼ਣ ਦੀ ਘਾਟ", "ਵਿਟਾਮਿਨ ਬੀ-੧੨ ਦੀ ਕਮੀ"],
            "triage_level": "ਮੱਧਮ (ਡਾਕਟਰ ਤੋਂ ਆਇਰਨ ਸਪਲੀਮੈਂਟ ਲਿਖਵਾਓ)",
            "suggested_tests": ["Complete Blood Count (CBC with Peripheral Smear)", "Serum Ferritin (ਸਰੀਰ ਵਿੱਚ ਜਮ੍ਹਾਂ ਆਇਰਨ)", "Vitamin B12 & Folic Acid levels"],
            "guidance_and_precautions": "ਹਰੀਆਂ ਪੱਤੇਦਾਰ ਸਬਜ਼ੀਆਂ (ਪਾਲਕ, ਮੇਥੀ), ਚੁਕੰਦਰ, ਅਨਾਰ, ਸੇਬ, ਗੁੜ, ਅਤੇ ਕਾਲੇ ਛੋਲੇ ਖੁਰਾਕ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ। ਚਾਹ/ਕੌਫੀ ਭੋਜਨ ਦੇ ਨਾਲ ਨਾ ਪੀਓ ਕਿਉਂਕਿ ਇਹ ਆਇਰਨ ਸੋਖਣ ਵਿੱਚ ਰੁਕਾਵਟ ਪਾਉਂਦੀ ਹੈ।",
            "disclaimer": "ਗੰਭੀਰ ਅਨੀਮੀਆ ਵਿੱਚ ਖੁਰਾਕ ਦੇ ਨਾਲ-ਨਾਲ ਡਾਕਟਰੀ ਆਇਰਨ ਦੀਆਂ ਗੋਲੀਆਂ ਲਾਜ਼ਮੀ ਹੁੰਦੀਆਂ ਹਨ।"
        },
        # 5. Gastroenterology / Liver & Digestion
        {
            "domain": "Gastroenterology & Hepatology",
            "age": "40 ਸਾਲ",
            "gender": "ਪੁਰਸ਼",
            "chief_complaint": "ਛਾਤੀ ਅਤੇ ਪੇਟ ਦੇ ਉੱਪਰਲੇ ਹਿੱਸੇ ਵਿੱਚ ਸੜਨ (Heartburn), ਖੱਟੇ ਡਕਾਰ ਅਤੇ ਭੋਜਨ ਤੋਂ ਬਾਅਦ ਭਾਰੀਪਣ।",
            "patient_query": "ਕੁਝ ਵੀ ਖਾਣ ਤੋਂ ਬਾਅਦ ਛਾਤੀ ਵਿੱਚ ਤੇਜ਼ ਅੱਗ ਵਰਗੀ ਸੜਨ ਹੁੰਦੀ ਹੈ ਅਤੇ ਗਲੇ ਵਿੱਚ ਖੱਟਾ ਪਾਣੀ ਆਉਂਦਾ ਹੈ। ਇਸਦਾ ਪੱਕਾ ਹੱਲ ਕੀ ਹੈ?",
            "clinical_assessment": "ਇਹ ਗੈਸਟ੍ਰੋ-ਈਸੋਫੇਜੀਅਲ ਰਿਫਲਕਸ ਡਿਜ਼ੀਜ਼ (GERD / Acid Reflux) ਅਤੇ ਹਾਈਪਰ-ਐਸਿਡਿਟੀ ਦੇ ਲੱਛਣ ਹਨ। ਪੇਟ ਦਾ ਤੇਜ਼ਾਬ ਭੋਜਨ ਨਲੀ (Esophagus) ਵਿੱਚ ਵਾਪਸ ਆਉਣ ਕਾਰਨ ਸੜਨ ਹੁੰਦੀ ਹੈ।",
            "suspected_conditions": ["ਐਸਿਡ ਰਿਫਲਕਸ (GERD)", "ਗੈਸਟ੍ਰਾਈਟਿਸ (Gastritis)", "ਪੈਪਟਿਕ ਅਲਸਰ"],
            "triage_level": "ਹਲਕਾ ਤੋਂ ਮੱਧਮ (Lifestyle & Medical Management)",
            "suggested_tests": ["Upper GI Endoscopy (ਜੇਕਰ ਸਮੱਸਿਆ ਲੰਬੀ ਰਹੇ)", "H. Pylori Stool Antigen Test", "Ultrasound Abdomen"],
            "guidance_and_precautions": "ਤਲੀਆਂ, ਮਸਾਲੇਦਾਰ ਅਤੇ ਖੱਟੀਆਂ ਚੀਜ਼ਾਂ ਤੋਂ ਪਰਹੇਜ਼ ਕਰੋ। ਰਾਤ ਦਾ ਖਾਣਾ ਸੌਣ ਤੋਂ ੨-੩ ਘੰਟੇ ਪਹਿਲਾਂ ਖਾਓ। ਖਾਣਾ ਖਾਂਦੇ ਹੀ ਸਿੱਧਾ ਨਾ ਲੇਟੋ। ਧੂਮਰਪਾਨ ਅਤੇ ਸ਼ਰਾਬ ਬਿਲਕੁਲ ਬੰਦ ਕਰੋ।",
            "disclaimer": "ਜੇਕਰ ਉਲਟੀ ਵਿੱਚ ਖੂਨ ਆਵੇ ਜਾਂ ਕਾਲੇ ਰੰਗ ਦਾ ਮਲ ਆਵੇ ਤਾਂ ਤੁਰੰਤ ਹਸਪਤਾਲ ਜਾਓ।"
        },
        # 6. Infectious Diseases / Fevers
        {
            "domain": "Infectious Diseases & Virology",
            "age": "28 ਸਾਲ",
            "gender": "ਪੁਰਸ਼",
            "chief_complaint": "ਤੇਜ਼ ਬੁਖ਼ਾਰ, ਅੱਖਾਂ ਦੇ ਪਿੱਛੇ ਦਰਦ, ਹੱਡੀਆਂ-ਜੋੜਾਂ ਵਿੱਚ ਅਸਹਿ ਪੀੜ ਅਤੇ ਸਰੀਰ 'ਤੇ ਲਾਲ ਦਾਣੇ।",
            "patient_query": "ਮੈਨੂੰ ੩ ਦਿਨਾਂ ਤੋਂ ੧੦੩ ਡਿਗਰੀ ਬੁਖ਼ਾਰ ਹੈ, ਲੱਤਾਂ-ਬਾਹਾਂ ਟੁੱਟ ਰਹੀਆਂ ਹਨ ਅਤੇ ਅੱਖਾਂ ਹਿਲਾਉਣ 'ਤੇ ਵੀ ਦਰਦ ਹੁੰਦਾ ਹੈ। ਕੀ ਇਹ ਡੇਂਗੂ ਹੋ ਸਕਦਾ ਹੈ?",
            "clinical_assessment": "ਅੱਖਾਂ ਦੇ ਪਿੱਛੇ ਦਰਦ (Retro-orbital pain) ਅਤੇ ਤੇਜ਼ ਹੱਡ-ਤੋੜ ਬੁਖ਼ਾਰ (Break-bone fever) ਡੇਂਗੂ ਵਾਇਰਸ (Dengue Fever) ਦੇ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਸੰਕੇਤ ਹਨ। ਪਲੇਟਲੈੱਟਸ ਦੀ ਨਿਗਰਾਨੀ ਜ਼ਰੂਰੀ ਹੈ।",
            "suspected_conditions": ["ਡੇਂਗੂ ਬੁਖ਼ਾਰ (Dengue Fever)", "ਚਿਕਨਗੁਨੀਆ (Chikungunya)", "ਵਾਇਰਲ ਫਲੂ"],
            "triage_level": "ਉੱਚ (High - ਤੁਰੰਤ CBC ਅਤੇ ਡੇਂਗੂ ਟੈਸਟ ਕਰਵਾਓ)",
            "suggested_tests": ["Dengue NS1 Antigen (ਪਹਿਲੇ ੫ ਦਿਨਾਂ ਵਿੱਚ)", "Dengue IgM/IgG Antibodies", "CBC (ਪਲੇਟਲੈੱਟ ਕਾਊਂਟ ਅਤੇ Hematocrit ਦੀ ਰੋਜ਼ਾਨਾ ਜਾਂਚ)"],
            "guidance_and_precautions": "ਤਰਲ ਪਦਾਰਥ (ਨਾਰੀਅਲ ਪਾਣੀ, ਓ.ਆਰ.ਐੱਸ, ਤਾਜ਼ੇ ਫਲਾਂ ਦਾ ਜੂਸ, ਦਾਲ ਦਾ ਪਾਣੀ) ਵੱਧ ਤੋਂ ਵੱਧ ਪੀਓ। ਬੁਖ਼ਾਰ ਲਈ ਸਿਰਫ਼ ਪੈਰਾਸੀਟਾਮੋਲ ਲਓ। ਐਸਪਰੀਨ (Aspirin) ਜਾਂ ਬਰੂਫਿਨ (Ibuprofen) ਬਿਲਕੁਲ ਨਾ ਲਓ ਕਿਉਂਕਿ ਇਹ ਖੂਨ ਪਤਲਾ ਕਰਦੀਆਂ ਹਨ।",
            "disclaimer": "ਜੇਕਰ ਨੱਕ, ਮਸੂੜਿਆਂ ਵਿੱਚੋਂ ਖੂਨ ਆਵੇ ਜਾਂ ਲਗਾਤਾਰ ਉਲਟੀਆਂ ਹੋਣ ਤਾਂ ਬਿਨਾਂ ਦੇਰੀ ਹਸਪਤਾਲ ਦਾਖਲ ਹੋਵੋ।"
        }
    ]

    for case in clinical_cases:
        dataset.append({
            "id": f"amrit_clinical_{idx:05d}",
            "domain": case["domain"],
            "instruction": "ਮਰੀਜ਼ ਦੇ ਪੰਜਾਬੀ ਵਿੱਚ ਦੱਸੇ ਲੱਛਣਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਭਾਵਿਤ ਕਲੀਨਿਕਲ ਮੁਲਾਂਕਣ, ਜ਼ਰੂਰੀ ਲੈਬ ਟੈਸਟ, ਪਰਹੇਜ਼ ਅਤੇ ਡਾਕਟਰੀ ਸਲਾਹ ਤਿਆਰ ਕਰੋ।",
            "patient_profile": {
                "age": case["age"],
                "gender": case["gender"],
                "chief_complaint": norm(case["chief_complaint"])
            },
            "patient_query": norm(case["patient_query"]),
            "clinical_assessment": norm(case["clinical_assessment"]),
            "suspected_conditions": [norm(c) for c in case["suspected_conditions"]],
            "triage_level": norm(case["triage_level"]),
            "suggested_tests": [norm(t) for t in case["suggested_tests"]],
            "guidance_and_precautions": norm(case["guidance_and_precautions"]),
            "disclaimer": norm(case["disclaimer"])
        })
        idx += 1

    return dataset

def generate_expanded_clinical_corpus(base_dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Programmatically expand clinical scenarios across diverse demographics, symptoms,
    comorbidities, and rural Punjabi clinical settings.
    """
    expanded = list(base_dataset)
    current_id = len(expanded) + 1

    # Multi-disease symptom combinations across full medical spectrum
    symptom_matrix = [
        # 1. Nephrology
        (
            "Nephrology & Renal Health",
            "ਪਿਸ਼ਾਬ ਵਿੱਚ ਜਲਣ, ਧੁੰਦਲਾ ਪਿਸ਼ਾਬ ਅਤੇ ਪਿੱਠ ਦੇ ਹੇਠਲੇ ਪਾਸੇ ਦਰਦ",
            "ਪਿਸ਼ਾਬ ਵਿੱਚ ਜਲਣ ਅਤੇ ਪਿੱਠ ਦਰਦ ਯੂਰੀਨਰੀ ਟ੍ਰੈਕਟ ਇਨਫੈਕਸ਼ਨ (UTI) ਜਾਂ ਗੁਰਦੇ ਦੀ ਪੱਥਰੀ (Renal Calculi) ਦੇ ਸੰਕੇਤ ਹਨ।",
            ["ਯੂ.ਟੀ.ਆਈ (Urinary Tract Infection)", "ਗੁਰਦੇ ਦੀ ਪੱਥਰੀ (Kidney Stone)", "ਸਿਸਟਾਈਟਿਸ"],
            ["Urine Complete Examination & Culture", "Ultrasound KUB (Kidney, Ureter, Bladder)", "Serum Creatinine"],
            "ਦਿਨ ਵਿੱਚ ੩ ਤੋਂ ੪ ਲੀਟਰ ਸਾਫ਼ ਪਾਣੀ ਪੀਓ। ਪਿਸ਼ਾਬ ਨੂੰ ਜ਼ਿਆਦਾ ਦੇਰ ਨਾ ਰੋਕੋ। ਖੱਟੇ ਅਤੇ ਮਸਾਲੇਦਾਰ ਭੋਜਨ ਤੋਂ ਪਰਹੇਜ਼ ਕਰੋ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 2. Rheumatology
        (
            "Rheumatology & Bone Health",
            "ਸਵੇਰੇ ਉੱਠਣ ਵੇਲੇ ਗੋਡਿਆਂ ਅਤੇ ਹੱਥਾਂ ਦੇ ਜੋੜਾਂ ਵਿੱਚ ਅਕੜਾਅ ਅਤੇ ਸੋਜਿਸ਼",
            "ਸਵੇਰ ਵੇਲੇ ਜੋੜਾਂ ਦਾ ਅਕੜਾਅ (Morning stiffness > 30 mins) ਗਠੀਆ (Rheumatoid Arthritis) ਜਾਂ ਓਸਟੀਓ-ਆਰਥਰਾਈਟਿਸ ਦਾ ਲੱਛਣ ਹੈ।",
            ["ਗਠੀਆ (Rheumatoid Arthritis)", "ਓਸਟੀਓਆਰਥਰਾਈਟਿਸ (Osteoarthritis)", "ਯੂਰਿਕ ਐਸਿਡ / ਗਾਊਟ (Gout)"],
            ["RA Factor", "Anti-CCP", "Serum Uric Acid", "X-Ray of affected joints", "ESR / CRP (ਸੋਜਿਸ਼ ਦੇ ਮਾਰਕਰ)"],
            "ਜੋੜਾਂ ਨੂੰ ਠੰਢ ਤੋਂ ਬਚਾਓ। ਹਲਕੀ ਕਸਰਤ ਕਰੋ। ਜੇਕਰ ਯੂਰਿਕ ਐਸਿਡ ਵੱਧ ਹੈ ਤਾਂ ਦਾਲਾਂ, ਪਾਲਕ ਅਤੇ ਟਮਾਟਰ ਘਟਾਓ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 3. Neurology
        (
            "Neurology & Headaches",
            "ਸਿਰ ਦੇ ਅੱਧੇ ਹਿੱਸੇ ਵਿੱਚ ਧੜਕਣ ਵਰਗਾ ਤੇਜ਼ ਦਰਦ, ਉਲਟੀ ਦਾ ਮਨ ਅਤੇ ਰੌਸ਼ਨੀ ਤੋਂ ਚਿੜਚਿੜਾਪਣ",
            "ਅੱਧੇ ਸਿਰ ਦਾ ਦਰਦ (Unilateral throbbing pain) ਅਤੇ Photophobia ਮਾਈਗ੍ਰੇਨ (Migraine) ਦੇ ਪੱਕੇ ਲੱਛਣ ਹਨ।",
            ["ਮਾਈਗ੍ਰੇਨ (Migraine)", "ਟੈਂਸ਼ਨ ਹੈਡੇਕ (Tension Headache)", "ਸਾਈਨਸਾਈਟਿਸ"],
            ["MRI / CT Brain (ਜੇਕਰ ਦਰਦ ਅਸਾਧਾਰਨ ਹੋਵੇ)", "Eye Examination (ਨਜ਼ਰ ਦੀ ਜਾਂਚ)"],
            "ਹਨੇਰੇ ਅਤੇ ਸ਼ਾਂਤ ਕਮਰੇ ਵਿੱਚ ਆਰਾਮ ਕਰੋ। ਤੇਜ਼ ਧੁੱਪ, ਤੇਜ਼ ਆਵਾਜ਼ ਅਤੇ ਕੰਪਿਊਟਰ/ਮੋਬਾਈਲ ਸਕ੍ਰੀਨ ਤੋਂ ਦੂਰ ਰਹੋ। ਨਿਯਮਿਤ ਨੀਂਦ ਲਓ।",
            "ਹਲਕਾ ਤੋਂ ਮੱਧਮ (Mild to Moderate)"
        ),
        # 4. Dermatology
        (
            "Dermatology & Skin Allergies",
            "ਚਮੜੀ 'ਤੇ ਗੋਲ ਲਾਲ ਚੱਕਤੇ, ਤੇਜ਼ ਖਾਰਸ਼ ਅਤੇ ਪਸੀਨੇ ਨਾਲ ਜਲਣ",
            "ਗੋਲ ਲਾਲ ਚੱਕਤੇ ਅਤੇ ਖਾਰਸ਼ ਫੰਗਲ ਇਨਫੈਕਸ਼ਨ (Tinea / Ringworm / ਦਾਦ) ਦੇ ਲੱਛਣ ਹਨ, ਜੋ ਨਮੀ ਅਤੇ ਪਸੀਨੇ ਕਾਰਨ ਫੈਲਦੀ ਹੈ।",
            ["ਦਾਦ / ਫੰਗਲ ਇਨਫੈਕਸ਼ਨ (Tinea Corporis)", "ਐਗਜ਼ੀਮਾ (Eczema)", "ਕੰਟੈਕਟ ਡਰਮੇਟਾਇਟਸ"],
            ["Skin Scraping for Fungus (KOH Mount)", "Dermatology Clinical Examination"],
            "ਸਰੀਰ ਨੂੰ ਸੁੱਕਾ ਅਤੇ ਸਾਫ਼ ਰੱਖੋ। ਸੂਤੀ (Cotton) ਕੱਪੜੇ ਪਹਿਨੋ। ਦੂਜਿਆਂ ਦਾ ਤੌਲੀਆ ਜਾਂ ਕੱਪੜੇ ਨਾ ਵਰਤੋ। ਬਿਨਾਂ ਡਾਕਟਰੀ ਸਲਾਹ ਦੇ ਸਟੀਰੌਇਡ ਕਰੀਮ ਨਾ ਲਗਾਓ।",
            "ਹਲਕਾ (Mild)"
        ),
        # 5. Pediatrics
        (
            "Pediatrics & Child Care",
            "ਛੋਟੇ ਬੱਚੇ ਨੂੰ ਪਤਲੇ ਦਸਤ, ਵਾਰ-ਵਾਰ ਉਲਟੀਆਂ ਅਤੇ ਪਿਸ਼ਾਬ ਘੱਟ ਆਉਣਾ",
            "ਵਾਰ-ਵਾਰ ਦਸਤ ਅਤੇ ਉਲਟੀਆਂ ਕਾਰਨ ਬੱਚੇ ਅੰਦਰ ਪਾਣੀ ਦੀ ਘਾਟ (Acute Gastroenteritis with Dehydration) ਹੋ ਸਕਦੀ ਹੈ, ਜੋ ਖ਼ਤਰਨਾਕ ਹੈ।",
            ["ਵਾਇਰਲ ਡਾਇਰੀਆ (Rotavirus Gastroenteritis)", "ਫੂਡ ਪੋਇਜ਼ਨਿੰਗ", "ਡੀਹਾਈਡ੍ਰੇਸ਼ਨ"],
            ["Stool Routine & Microscopy", "Serum Electrolytes (Sodium, Potassium)"],
            "ਹਰ ਦਸਤ ਤੋਂ ਬਾਅਦ ਓ.ਆਰ.ਐੱਸ (ORS) ਦਾ ਘੋਲ ਜਾਂ ਉਬਲਿਆ ਠੰਢਾ ਪਾਣੀ ਚਮਚ-ਚਮਚ ਕਰਕੇ ਦਿਓ। ਮਾਂ ਦਾ ਦੁੱਧ ਜਾਰੀ ਰੱਖੋ।",
            "ਉੱਚ (ਜੇਕਰ ਬੱਚਾ ਸੁਸਤ ਹੋਵੇ ਜਾਂ ਅੱਖਾਂ ਧਸ ਜਾਣ ਤਾਂ ਤੁਰੰਤ ਹਸਪਤਾਲ)"
        ),
        # 6. Thyroid & Endocrinology
        (
            "Endocrinology & Thyroid",
            "ਅਚਾਨਕ ਭਾਰ ਵਧਣਾ, ਬਹੁਤ ਜ਼ਿਆਦਾ ਠੰਢ ਲੱਗਣਾ, ਗਲੇ ਵਿੱਚ ਸੋਜ ਅਤੇ ਵਾਲ ਝੜਨੇ",
            "ਭਾਰ ਵਧਣਾ ਅਤੇ ਠੰਢ ਬਰਦਾਸ਼ਤ ਨਾ ਹੋਣਾ ਹਾਈਪੋਥਾਇਰਾਇਡਿਜ਼ਮ (Hypothyroidism) ਦੇ ਸੰਕੇਤ ਹਨ, ਜਿਸ ਵਿੱਚ ਥਾਇਰਾਇਡ ਗਲੈਂਡ ਸੁਸਤ ਹੋ ਜਾਂਦੀ ਹੈ।",
            ["ਹਾਈਪੋਥਾਇਰਾਇਡਿਜ਼ਮ (Hypothyroidism)", "ਗਲਗੰਡ (Goitre)", "ਹਾਸ਼ੀਮੋਟੋ ਥਾਇਰਾਇਡਾਈਟਿਸ"],
            ["Thyroid Profile (TSH, Free T3, Free T4)", "Anti-TPO Antibodies", "Ultrasound Neck/Thyroid"],
            "ਆਇਓਡੀਨ ਯੁਕਤ ਲੂਣ ਵਰਤੋ। ਬੰਦਗੋਭੀ ਅਤੇ ਬ੍ਰੋਕਲੀ ਵਰਗੇ ਕੱਚੇ ਗੋਇਟ੍ਰੋਜਨਿਕ ਭੋਜਨ ਸੀਮਤ ਕਰੋ। ਸਵੇਰੇ ਖਾਲੀ ਪੇਟ ਥਾਇਰਾਇਡ ਦਵਾਈ ਲਓ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 7. Cardiology / Angina & Chest Pain
        (
            "Cardiology & Emergency Care",
            "ਛਾਤੀ ਦੇ ਵਿਚਕਾਰ ਭਾਰੀ ਦਬਾਅ, ਦਰਦ ਖੱਬੀ ਬਾਂਹ ਅਤੇ ਜਬਾੜੇ ਵੱਲ ਜਾਣਾ ਅਤੇ ਠੰਢੇ ਪਸੀਨੇ ਆਉਣੇ",
            "ਛਾਤੀ ਵਿੱਚ ਦਬਾਅ ਅਤੇ ਖੱਬੀ ਬਾਂਹ ਵਿੱਚ ਦਰਦ ਦਿਲ ਦੇ ਦੌਰੇ (Acute Myocardial Infarction / Angina) ਦਾ ਗੰਭੀਰ ਐਮਰਜੈਂਸੀ ਸੰਕੇਤ ਹੈ।",
            ["ਐਕਿਊਟ ਕੋਰੋਨਰੀ ਸਿੰਡਰੋਮ (Heart Attack / Angina)", "ਕੋਰੋਨਰੀ ਆਰਟਰੀ ਡਿਜ਼ੀਜ਼"],
            ["12-Lead ECG (ਤੁਰੰਤ)", "Troponin-I / Troponin-T (ਦਿਲ ਦੇ ਐਨਜ਼ਾਈਮ)", "Echocardiography (2D Echo)"],
            "ਮਰੀਜ਼ ਨੂੰ ਤੁਰੰਤ ਬਿਠਾਓ, ਹਿੱਲਣ-ਜੁੱਲਣ ਨਾ ਦਿਓ। ਤੁਰੰਤ ਐਂਬੂਲੈਂਸ ਬੁਲਾਓ ਜਾਂ ਨਜ਼ਦੀਕੀ ਐਮਰਜੈਂਸੀ ਹਸਪਤਾਲ ਲੈ ਕੇ ਜਾਓ।",
            "🚨 ਅਤਿ-ਗੰਭੀਰ ਐਮਰਜੈਂਸੀ (Immediate Emergency Hospitalization)"
        ),
        # 8. Hepatology / Jaundice
        (
            "Hepatology & Liver Health",
            "ਅੱਖਾਂ ਅਤੇ ਪਿਸ਼ਾਬ ਦਾ ਰੰਗ ਪੀਲਾ ਹੋਣਾ, ਭੁੱਖ ਬਿਲਕੁਲ ਨਾ ਲੱਗਣਾ ਅਤੇ ਸੱਜੇ ਪਾਸੇ ਪਸਲੀਆਂ ਹੇਠਾਂ ਦਰਦ",
            "ਪੀਲਾ ਪਿਸ਼ਾਬ ਅਤੇ ਭੁੱਖ ਨਾ ਲੱਗਣਾ ਪੀਲੀਆ (Jaundice / Acute Hepatitis) ਜਾਂ ਲਿਵਰ ਵਿੱਚ ਸੋਜਿਸ਼ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ।",
            ["ਹੈਪੇਟਾਈਟਿਸ (Viral Hepatitis A/E)", "ਪੀਲੀਆ (Obstructive/Infective Jaundice)", "ਫੈਟੀ ਲਿਵਰ (NAFLD)"],
            ["Liver Function Test (LFT - Bilirubin, SGOT, SGPT, Alkaline Phosphatase)", "Viral Hepatitis Serology", "Ultrasound Abdomen"],
            "ਤਲਿਆ, ਘਿਓ-ਤੇਲ ਵਾਲਾ ਭੋਜਨ ਬਿਲਕੁਲ ਬੰਦ ਕਰੋ। ਉਬਲਿਆ ਪਾਣੀ, ਗੰਨੇ ਦਾ ਤਾਜ਼ਾ ਸਾਫ਼ ਰਸ, ਨਿੰਬੂ ਪਾਣੀ ਅਤੇ ਹਲਕੀ ਖਿਚੜੀ ਖਾਓ।",
            "ਮੱਧਮ ਤੋਂ ਉੱਚ (Moderate to High)"
        ),
        # 9. Ophthalmology
        (
            "Ophthalmology & Eye Health",
            "ਅੱਖਾਂ ਵਿੱਚ ਲਾਲੀ, ਚਿਪਚਿਪਾ ਪਾਣੀ, ਰੜਕ ਅਤੇ ਸਵੇਰੇ ਪਲਕਾਂ ਜੁੜਨਾ",
            "ਅੱਖਾਂ ਵਿੱਚ ਲਾਲੀ ਅਤੇ ਚਿਪਚਿਪਾਪਣ ਕੰਜਕਟਿਵਾਇਟਿਸ (Conjunctivitis / ਅੱਖਾਂ ਆਉਣਾ) ਦਾ ਸੰਕੇਤ ਹੈ।",
            ["ਬੈਕਟੀਰੀਅਲ ਕੰਜਕਟਿਵਾਇਟਿਸ", "ਵਾਇਰਲ ਕੰਜਕਟਿਵਾਇਟਿਸ", "ਐਲਰਜੀਕ ਨੇਤਰ ਰੋਗ"],
            ["Slit Lamp Examination", "Visual Acuity Test"],
            "ਅੱਖਾਂ ਨੂੰ ਸਾਫ਼ ਠੰਢੇ ਪਾਣੀ ਨਾਲ ਧੋਵੋ। ਅੱਖਾਂ ਨੂੰ ਹੱਥ ਨਾ ਲਗਾਓ। ਕਾਲਾ ਚਸ਼ਮਾ ਪਹਿਨੋ। ਦੂਜਿਆਂ ਨਾਲ ਤੌਲੀਆ ਸਾਂਝਾ ਨਾ ਕਰੋ।",
            "ਹਲਕਾ (Mild)"
        ),
        # 10. Otolaryngology / ENT
        (
            "ENT & Throat Health",
            "ਗਲੇ ਵਿੱਚ ਤੇਜ਼ ਦਰਦ, ਕੁਝ ਵੀ ਨਿਗਲਣ ਵੇਲੇ ਤਕਲੀਫ਼, ਗਰਦਨ ਦੀਆਂ ਗਿਲਟੀਆਂ ਵਿੱਚ ਸੋਜ ਅਤੇ ਹਲਕਾ ਬੁਖ਼ਾਰ",
            "ਗਲੇ ਵਿੱਚ ਦਰਦ ਅਤੇ ਨਿਗਲਣ ਵਿੱਚ ਤਕਲੀਫ਼ ਟੌਨਸਿਲਾਈਟਿਸ (Acute Tonsillitis / Pharyngitis) ਦਾ ਸੰਕੇਤ ਹੈ।",
            ["ਟੌਨਸਿਲਾਈਟਿਸ (Acute Tonsillitis)", "ਫੈਰਿੰਜਾਈਟਿਸ (Pharyngitis)", "ਸਟ੍ਰੈਪ ਥਰੋਟ"],
            ["Throat Swab Examination", "CBC with ESR"],
            "ਕੋਸੇ ਪਾਣੀ ਵਿੱਚ ਲੂਣ ਪਾ ਕੇ ਦਿਨ ਵਿੱਚ ੩ ਵਾਰ ਗਰਾਰੇ ਕਰੋ। ਠੰਢਾ ਪਾਣੀ, ਕੋਲਡ ਡਰਿੰਕਸ ਬੰਦ ਕਰੋ। ਕੋਸਾ ਸੂਪ ਜਾਂ ਚਾਹ ਪੀਓ।",
            "ਹਲਕਾ (Mild)"
        ),
        # 11. Pulmonology / Tuberculosis & Chronic Cough
        (
            "Pulmonology & Infectious Diseases",
            "ਦੋ ਹਫ਼ਤਿਆਂ ਤੋਂ ਵੱਧ ਖੰਘ, ਬਲਗ਼ਮ ਵਿੱਚ ਖੂਨ ਦੇ ਧੱਬੇ, ਸ਼ਾਮ ਵੇਲੇ ਹਲਕਾ ਬੁਖ਼ਾਰ ਅਤੇ ਭਾਰ ਘਟਣਾ",
            "ਦੋ ਹਫ਼ਤਿਆਂ ਤੋਂ ਵੱਧ ਖੰਘ ਅਤੇ ਬਲਗ਼ਮ ਵਿੱਚ ਖੂਨ ਟੀ.ਬੀ (Pulmonary Tuberculosis) ਦੇ ਮੁੱਖ ਲੱਛਣ ਹਨ। ਸਰਕਾਰੀ ਸਿਹਤ ਕੇਂਦਰ ਵਿੱਚ ਮੁਫ਼ਤ ਜਾਂਚ ਉਪਲਬਧ ਹੈ।",
            ["ਫੇਫੜਿਆਂ ਦੀ ਟੀ.ਬੀ (Pulmonary Tuberculosis)", "ਬ੍ਰੌਨਕੀਐਕਟੇਸਿਸ", "ਕ੍ਰੌਨਿਕ ਬ੍ਰੌਨਕਾਈਟਿਸ"],
            ["Sputum AFB / CBNAAT (GeneXpert)", "Chest X-Ray PA View", "Complete Blood Count with ESR"],
            "ਖੰਘਣ ਵੇਲੇ ਰੁਮਾਲ ਜਾਂ ਮਾਸਕ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਖੁੱਲ੍ਹੇ ਵਿੱਚ ਨਾ ਥੁੱਕੋ। ਟੀ.ਬੀ ਦੀ ਦਵਾਈ (DOTS) ਬਿਨਾਂ ਨਾਗਾ ਪੂਰੇ ੬ ਮਹੀਨੇ ਖਾਣੀ ਜ਼ਰੂਰੀ ਹੈ।",
            "ਉੱਚ (High - ਤੁਰੰਤ ਬਲਗ਼ਮ ਜਾਂਚ ਕਰਵਾਓ)"
        ),
        # 12. Endocrinology / High Cholesterol & Dyslipidemia
        (
            "Cardiovascular & Lipidology",
            "ਥੋੜ੍ਹਾ ਜਿਹਾ ਤੁਰਨ 'ਤੇ ਸਾਹ ਫੁੱਲਣਾ, ਪਿੰਜਣੀਆਂ ਵਿੱਚ ਖਿਚਾਅ ਅਤੇ ਰਿਪੋਰਟ ਵਿੱਚ ਕੁੱਲ ਕੋਲੈਸਟ੍ਰੋਲ ੨੬੦ ਆਉਣਾ",
            "ਕੋਲੈਸਟ੍ਰੋਲ ੨੬੦ mg/dL ਹਾਈਪਰਲਿਪੀਡੀਮੀਆ (Dyslipidemia) ਦਰਸਾਉਂਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਖੂਨ ਦੀਆਂ ਨਾੜਾਂ ਵਿੱਚ ਚਰਬੀ ਜੰਮਣ ਦਾ ਖ਼ਤਰਾ ਵਧਦਾ ਹੈ।",
            ["ਹਾਈ ਕੋਲੈਸਟ੍ਰੋਲ (Hyperlipidemia)", "ਐਥੀਰੋਸਕਲੇਰੋਸਿਸ", "ਕੋਰੋਨਰੀ ਆਰਟਰੀ ਬਿਮਾਰੀ"],
            ["Fasting Lipid Profile (Total Cholesterol, LDL, HDL, Triglycerides)", "Liver Function Test", "ECG"],
            "ਦੇਸੀ ਘਿਓ, ਮੱਖਣ, ਤਲੀਆਂ ਚੀਜ਼ਾਂ, ਜੰਕ ਫੂਡ ਅਤੇ ਬੇਕਰੀ ਆਈਟਮਾਂ ਬੰਦ ਕਰੋ। ਅਲਸੀ (Flaxseeds), ਓਟਸ, ਅਤੇ ਲਸਣ ਖੁਰਾਕ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 13. Urology / BPH & Prostate Health
        (
            "Urology & Men's Health",
            "ਪਿਸ਼ਾਬ ਦੀ ਧਾਰ ਕਮਜ਼ੋਰ ਹੋਣਾ, ਪਿਸ਼ਾਬ ਕਰਨ ਵਿੱਚ ਜ਼ੋਰ ਲੱਗਣਾ ਅਤੇ ਰਾਤ ਨੂੰ ਬਾਰ-ਬਾਰ ਉੱਠਣਾ",
            "ਬਜ਼ੁਰਗਾਂ ਵਿੱਚ ਪਿਸ਼ਾਬ ਦੀ ਧਾਰ ਕਮਜ਼ੋਰ ਹੋਣਾ ਪ੍ਰੋਸਟੇਟ ਗ੍ਰੰਥੀ ਦੇ ਵਧਣ (BPH - Benign Prostatic Hyperplasia) ਦਾ ਲੱਛਣ ਹੈ।",
            ["ਪ੍ਰੋਸਟੇਟ ਦਾ ਵਧਣਾ (BPH)", "ਪ੍ਰੋਸਟੇਟਾਈਟਿਸ", "ਯੂਰੇਥਰਲ ਸਟ੍ਰਿਕਚਰ"],
            ["Serum PSA (Prostate Specific Antigen)", "Ultrasound Pelvis with Post-Void Residual Urine (PVR)", "Uroflowmetry"],
            "ਰਾਤ ਨੂੰ ਸੌਣ ਤੋਂ ਪਹਿਲਾਂ ਜ਼ਿਆਦਾ ਪਾਣੀ ਨਾ ਪੀਓ। ਚਾਹ ਅਤੇ ਕੌਫੀ ਘਟਾਓ। ਪਿਸ਼ਾਬ ਨੂੰ ਜ਼ਬਰਦਸਤੀ ਨਾ ਰੋਕੋ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 14. Gastroenterology / Gallbladder Stones
        (
            "Gastroenterology & Abdominal Surgery",
            "ਭਾਰੀ ਜਾਂ ਘਿਓ ਵਾਲਾ ਭੋਜਨ ਖਾਣ ਤੋਂ ਬਾਅਦ ਪੇਟ ਦੇ ਸੱਜੇ ਪਾਸੇ ਉੱਪਰ ਤੇਜ਼ ਦਰਦ ਜੋ ਪਿੱਠ ਦੇ ਮੋਢੇ ਵੱਲ ਜਾਵੇ",
            "ਭੋਜਨ ਤੋਂ ਬਾਅਦ ਸੱਜੇ ਪਾਸੇ ਦਰਦ ਪਿੱਤੇ ਦੀ ਪੱਥਰੀ (Gallstones / Cholelithiasis / Cholecystitis) ਦਾ ਲੱਛਣ ਹੈ।",
            ["ਪਿੱਤੇ ਦੀ ਪੱਥਰੀ (Gallstones)", "ਕੋਲੇਸਿਸਟਾਈਟਿਸ", "ਬਿਲੀਅਰੀ ਕੋਲਿਕ"],
            ["Ultrasound Whole Abdomen", "Liver Function Test (LFT)", "CBC"],
            "ਬਹੁਤ ਜ਼ਿਆਦਾ ਘਿਓ, ਤਲੀਆਂ ਚੀਜ਼ਾਂ ਅਤੇ ਭਾਰੇ ਭੋਜਨ ਤੋਂ ਪਰਹੇਜ਼ ਕਰੋ। ਦਰਦ ਵੇਲੇ ਹਲਕਾ ਭੋਜਨ ਲਓ। ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਨਾਲ ਅਲਟਰਾਸਾਊਂਡ ਕਰਵਾਓ।",
            "ਮੱਧਮ ਤੋਂ ਉੱਚ (Moderate to High)"
        ),
        # 15. Neurology / Stroke Warning Signs (FAST)
        (
            "Neurology & Emergency Care",
            "ਅਚਾਨਕ ਮੂੰਹ ਦਾ ਇੱਕ ਪਾਸਾ ਵਿੰਗਾ ਹੋਣਾ, ਇੱਕ ਬਾਂਹ ਵਿੱਚ ਕਮਜ਼ੋਰੀ ਅਤੇ ਬੋਲਣ ਵਿੱਚ ਥਿੜਕਣ",
            "ਇਹ ਲਕਵਾ / ਅਧਰੰਗ (Acute Ischemic Stroke) ਦੇ ਤੁਰੰਤ ਚੇਤਾਵਨੀ ਸੰਕੇਤ ਹਨ। ਪਹਿਲੇ ੪.੫ ਘੰਟੇ (Golden Hour) ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੁੰਦੇ ਹਨ।",
            ["ਦਿਮਾਗੀ ਦੌਰਾ / ਲਕਵਾ (Acute Ischemic Stroke)", "ਟ੍ਰਾਂਸੀਐਂਟ ਇਸਕੀਮਿਕ ਅਟੈਕ (TIA)"],
            ["NCCT Brain / MRI Brain (ਐਮਰਜੈਂਸੀ)", "Blood Sugar", "ECG", "Carotid Doppler"],
            "ਮਰੀਜ਼ ਨੂੰ ਕੁਝ ਵੀ ਖਾਣ-ਪੀਣ ਲਈ ਨਾ ਦਿਓ (ਕਿਉਂਕਿ ਨਿਗਲਣ ਵਿੱਚ ਸਮੱਸਿਆ ਹੋ ਸਕਦੀ ਹੈ)। ਤੁਰੰਤ ਨਜ਼ਦੀਕੀ ਸਟ੍ਰੋਕ ਹਸਪਤਾਲ ਲੈ ਕੇ ਜਾਓ।",
            "🚨 ਅਤਿ-ਗੰਭੀਰ ਐਮਰਜੈਂਸੀ (Immediate Stroke Emergency)"
        ),
        # 16. Orthopedics / Lower Back Pain & Sciatica
        (
            "Orthopedics & Spine Health",
            "ਕਮਰ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਤੋਂ ਸ਼ੁਰੂ ਹੋ ਕੇ ਦਰਦ ਪੂਰੀ ਲੱਤ ਦੇ ਪਿੱਛੇ ਪੈਰ ਦੀਆਂ ਉਂਗਲਾਂ ਤੱਕ ਜਾਣਾ ਅਤੇ ਸੁੰਨਪਣ",
            "ਲੱਤ ਵਿੱਚ ਉੱਤਰਦਾ ਦਰਦ ਅਤੇ ਸੁੰਨਪਣ ਸਿਆਟਿਕਾ (Sciatica / Lumbar Disc Herniation - L4-L5/L5-S1) ਦਾ ਲੱਛਣ ਹੈ।",
            ["ਸਿਆਟਿਕਾ (Sciatica)", "ਡਿਸਕ ਪ੍ਰੋਲੈਪਸ (Slipped Disc)", "ਲੰਬਰ ਸਪੌਂਡਿਲਾਈਟਿਸ"],
            ["MRI Lumbar Spine", "X-Ray LS Spine AP/Lateral"],
            "ਸਖ਼ਤ ਬਿਸਤਰੇ 'ਤੇ ਸੌਵੋ। ਭਾਰੀ ਸਮਾਨ ਨਾ ਚੁੱਕੋ। ਅੱਗੇ ਵੱਲ ਝੁਕਣ ਤੋਂ ਪਰਹੇਜ਼ ਕਰੋ। ਫਿਜ਼ੀਓਥੈਰੇਪੀ ਕਸਰਤਾਂ ਸ਼ੁਰੂ ਕਰੋ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 17. Psychiatry & Mental Wellbeing
        (
            "Psychiatry & Mental Health",
            "ਲਗਾਤਾਰ ਮਨ ਉਦਾਸ ਰਹਿਣਾ, ਕੰਮ ਵਿੱਚ ਦਿਲਚਸਪੀ ਖ਼ਤਮ ਹੋਣਾ, ਨੀਂਦ ਨਾ ਆਉਣਾ ਅਤੇ ਬੇਵਜ੍ਹਾ ਘਬਰਾਹਟ",
            "ਲਗਾਤਾਰ ਉਦਾਸੀ ਅਤੇ ਨੀਂਦ ਦੀ ਕਮੀ ਡਿਪ੍ਰੈਸ਼ਨ (Major Depressive Disorder) ਅਤੇ ਚਿੰਤਾ ਰੋਗ (Generalized Anxiety) ਵੱਲ ਸੰਕੇਤ ਕਰਦੀ ਹੈ।",
            ["ਡਿਪ੍ਰੈਸ਼ਨ (Clinical Depression)", "ਚਿੰਤਾ ਰੋਗ (Anxiety Disorder)", "ਇਨਸੌਮਨੀਆ"],
            ["Mental Health Clinical Evaluation", "Thyroid Profile (TSH)", "Serum Vitamin D & B12"],
            "ਆਪਣੀਆਂ ਭਾਵਨਾਵਾਂ ਪਰਿਵਾਰ ਜਾਂ ਮਨੋਵਿਗਿਆਨੀ ਨਾਲ ਸਾਂਝੀਆਂ ਕਰੋ। ਰੋਜ਼ਾਨਾ ਯੋਗਾ, ਧਿਆਨ ਅਤੇ ਸੈਰ ਕਰੋ। ਨਸ਼ਿਆਂ ਤੋਂ ਦੂਰ ਰਹੋ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 18. Gynecology & Women's Health
        (
            "Gynecology & Women's Health",
            "ਮਾਹਵਾਰੀ ਦੀ ਅਨਿਯਮਿਤਤਾ, ਚਿਹਰੇ 'ਤੇ ਅਣਚਾਹੇ ਵਾਲ, ਮੁਹਾਸੇ ਅਤੇ ਅਚਾਨਕ ਭਾਰ ਵਧਣਾ",
            "ਅਨਿਯਮਿਤ ਮਾਹਵਾਰੀ ਅਤੇ ਹਾਰਮੋਨਲ ਅਸੰਤੁਲਨ ਪੀ.ਸੀ.ਓ.ਡੀ / ਪੀ.ਸੀ.ਓ.ਐੱਸ (PCOS - Polycystic Ovary Syndrome) ਦੇ ਲੱਛਣ ਹਨ।",
            ["ਪੀ.ਸੀ.ਓ.ਐੱਸ (PCOS)", "ਹਾਰਮੋਨਲ ਅਸੰਤੁਲਨ", "ਹਾਈਪਰਐਂਡਰੋਜਨਿਜ਼ਮ"],
            ["Ultrasound Pelvis (TVS/TAS)", "Serum LH/FSH Ratio", "Serum Prolactin", "Fasting Insulin"],
            "ਖੁਰਾਕ ਵਿੱਚੋਂ ਮਿੱਠਾ ਅਤੇ ਮੈਦਾ ਬਿਲਕੁਲ ਬੰਦ ਕਰੋ। ਰੋਜ਼ਾਨਾ ੪੫ ਮਿੰਟ ਕਸਰਤ ਕਰਕੇ ਭਾਰ ਘਟਾਓ। ਹਰੀਆਂ ਸਬਜ਼ੀਆਂ ਵੱਧ ਖਾਓ।",
            "ਮੱਧਮ (Moderate)"
        ),
        # 19. Dental & Oral Health
        (
            "Dental & Oral Medicine",
            "ਮਸੂੜਿਆਂ ਵਿੱਚੋਂ ਖੂਨ ਆਉਣਾ, ਮੂੰਹ ਵਿੱਚੋਂ ਬਦਬੂ ਅਤੇ ਠੰਢਾ-ਗਰਮ ਪਾਣੀ ਲੱਗਣਾ",
            "ਮਸੂੜਿਆਂ ਵਿੱਚੋਂ ਖੂਨ ਆਉਣਾ ਜਿੰਜੀਵਾਈਟਿਸ (Gingivitis) ਅਤੇ ਦੰਦਾਂ ਦੀ ਸੜਨ (Dental Caries) ਦਾ ਸੰਕੇਤ ਹੈ।",
            ["ਮਸੂੜਿਆਂ ਦੀ ਸੋਜ (Gingivitis / Periodontitis)", "ਦੰਦਾਂ ਦੀ ਸੜਨ (Dental Caries)", "ਸੰਵੇਦਨਸ਼ੀਲਤਾ (Sensitivity)"],
            ["Dental Intra-Oral Examination", "IOPA X-Ray of teeth"],
            "ਦਿਨ ਵਿੱਚ ਦੋ ਵਾਰ ਬ੍ਰੱਸ਼ ਕਰੋ। ਕੋਸੇ ਲੂਣ ਵਾਲੇ ਪਾਣੀ ਨਾਲ ਕੁਰਲੀ ਕਰੋ। ਸਿਗਰਟ, ਤੰਬਾਕੂ ਅਤੇ ਗੁਟਖਾ ਬਿਲਕੁਲ ਬੰਦ ਕਰੋ।",
            "ਹਲਕਾ (Mild)"
        ),
        # 20. Immunology & Seasonal Allergies
        (
            "Immunology & Allergy Care",
            "ਮੌਸਮ ਬਦਲਣ ਵੇਲੇ ਲਗਾਤਾਰ ਛਿੱਕਾਂ ਆਉਣੀਆਂ, ਨੱਕ ਵਿੱਚੋਂ ਪਾਣੀ ਵਗਣਾ ਅਤੇ ਅੱਖਾਂ ਵਿੱਚ ਖਾਰਸ਼",
            "ਲਗਾਤਾਰ ਛਿੱਕਾਂ ਅਤੇ ਨੱਕ ਵਗਣਾ ਐਲਰਜੀਕ ਰਾਈਨਾਈਟਿਸ (Allergic Rhinitis / Hay Fever) ਦਾ ਲੱਛਣ ਹੈ ਜੋ ਪੋਲਨ ਜਾਂ ਮਿੱਟੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।",
            ["ਐਲਰਜੀਕ ਰਾਈਨਾਈਟਿਸ (Allergic Rhinitis)", "ਸੀਜ਼ਨਲ ਐਲਰਜੀ"],
            ["Absolute Eosinophil Count (AEC)", "Serum Total IgE Level", "Allergy Skin Prick Test"],
            "ਬਾਹਰ ਜਾਣ ਵੇਲੇ ਮਾਸਕ ਲਗਾਓ। ਖੁੱਲ੍ਹੇ ਵਿੱਚ ਧੂੜ-ਮਿੱਟੀ ਤੋਂ ਬਚੋ। ਕੋਸੇ ਪਾਣੀ ਨਾਲ ਸਟੀਮ (ਭਾਫ਼) ਲਓ।",
            "ਹਲਕਾ (Mild)"
        )
    ]

    age_groups = [
        ("੨੦-੩੦ ਸਾਲ", "ਨੌਜਵਾਨ"),
        ("੩੦-੪੫ ਸਾਲ", "ਵਿਅਕਤੀ"),
        ("੪੫-੬੦ ਸਾਲ", "ਪ੍ਰੌੜ੍ਹ"),
        ("੬੦+ ਸਾਲ", "ਬਜ਼ੁਰਗ")
    ]
    genders = [("ਪੁਰਸ਼", "ਭਰਾ ਜੀ"), ("ਇਸਤਰੀ", "ਭੈਣ ਜੀ")]

    # 1. Expand Symptom Consultations
    for cat, symp, assess, diff_list, tests, precs, tri in symptom_matrix:
        for age_str, age_label in age_groups:
            for g_str, g_salut in genders:
                query = f"ਡਾਕਟਰ ਸਾਹਿਬ, ਮੇਰੀ ਉਮਰ {age_str} ਹੈ। ਮੈਨੂੰ ਪਿਛਲੇ ਕੁਝ ਦਿਨਾਂ ਤੋਂ {symp} ਦੀ ਤਕਲੀਫ਼ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਦੱਸੋ ਮੈਨੂੰ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?"
                expanded.append({
                    "id": f"amrit_clinical_{current_id:05d}",
                    "domain": cat,
                    "instruction": "ਮਰੀਜ਼ ਦੇ ਪੰਜਾਬੀ ਵਿੱਚ ਦੱਸੇ ਲੱਛਣਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਭਾਵਿਤ ਕਲੀਨਿਕਲ ਮੁਲਾਂਕਣ, ਜ਼ਰੂਰੀ ਲੈਬ ਟੈਸਟ, ਪਰਹੇਜ਼ ਅਤੇ ਡਾਕਟਰੀ ਸਲਾਹ ਤਿਆਰ ਕਰੋ।",
                    "patient_profile": {
                        "age": age_str,
                        "gender": g_str,
                        "chief_complaint": norm(symp)
                    },
                    "patient_query": norm(query),
                    "clinical_assessment": norm(f"{assess} ({g_str}, ਉਮਰ {age_str})।"),
                    "suspected_conditions": [norm(c) for c in diff_list],
                    "triage_level": norm(tri),
                    "suggested_tests": [norm(t) for t in tests],
                    "guidance_and_precautions": norm(precs),
                    "disclaimer": norm("ਇਹ ਜਾਣਕਾਰੀ AMRIT AI ਰਿਸਰਚ ਮਾਡਲ ਦੁਆਰਾ ਮੈਡੀਕਲ ਸਿੱਖਿਆ ਲਈ ਦਿੱਤੀ ਗਈ ਹੈ। ਸਹੀ ਨਿਦਾਨ ਲਈ ਡਾਕਟਰ ਦੀ ਜਾਂਚ ਲਾਜ਼ਮੀ ਹੈ।")
                })
                current_id += 1

    # 2. Lab Interpretation Scenarios (CBC, HbA1c, Lipid, LFT, KFT, Thyroid)
    lab_scenarios = [
        (
            "Hematology Lab Interpretation",
            "ਖੂਨ ਦੀ ਰਿਪੋਰਟ (CBC): ਹੀਮੋਗਲੋਬਿਨ ੮.੫ g/dL, ਪਲੇਟਲੈੱਟਸ ੧,੪੦,੦੦੦, TLC (WBC) ੧੧,੫੦੦",
            "ਹੀਮੋਗਲੋਬਿਨ ੮.੫ g/dL ਅਨੀਮੀਆ (ਖੂਨ ਦੀ ਕਮੀ) ਦਰਸਾਉਂਦਾ ਹੈ। WBC ੧੧,੫੦੦ ਸਰੀਰ ਵਿੱਚ ਹਲਕੀ ਸੋਜਿਸ਼ ਜਾਂ ਇਨਫੈਕਸ਼ਨ ਦਾ ਸੰਕੇਤ ਹੈ। ਪਲੇਟਲੈੱਟਸ ੧.੪ ਲੱਖ ਨਾਰਮਲ ਰੇਂਜ ਦੇ ਨੇੜੇ ਹਨ।",
            ["ਮੱਧਮ ਅਨੀਮੀਆ (Moderate Anemia)", "ਹਲਕੀ ਬੈਕਟੀਰੀਅਲ ਇਨਫੈਕਸ਼ਨ"],
            ["Serum Ferritin", "Peripheral Blood Smear", "Repeat CBC after 1 week"],
            "ਆਇਰਨ ਯੁਕਤ ਖੁਰਾਕ (ਪਾਲਕ, ਗੁੜ, ਚੁਕੰਦਰ, ਦਾਲਾਂ) ਲਓ। ਕਾਫ਼ੀ ਪਾਣੀ ਪੀਓ ਅਤੇ ਡਾਕਟਰ ਤੋਂ ਆਇਰਨ ਸੀਰਪ ਜਾਂ ਗੋਲੀ ਲਿਖਵਾਓ।",
            "ਮੱਧਮ (Moderate)"
        ),
        (
            "Endocrinology Lab Interpretation",
            "ਸ਼ੂਗਰ ਦੀ ਜਾਂਚ: ਖਾਲੀ ਪੇਟ (Fasting) ੧੬੫ mg/dL, ਖਾਣਾ ਖਾਣ ਤੋਂ ਬਾਅਦ (PP) ੨੪੦ mg/dL, HbA1c ੮.੨%",
            "HbA1c ੮.੨% ਅਤੇ Fasting ੧੬੫ mg/dL ਅਨਕੰਟਰੋਲਡ ਸ਼ੂਗਰ (Uncontrolled Type 2 Diabetes) ਦਰਸਾਉਂਦੇ ਹਨ। ਇਸ ਨਾਲ ਅੱਖਾਂ, ਗੁਰਦਿਆਂ ਅਤੇ ਦਿਲ 'ਤੇ ਬੁਰਾ ਅਸਰ ਪੈ ਸਕਦਾ ਹੈ।",
            ["ਟਾਈਪ ੨ ਡਾਇਬੀਟੀਜ਼ (Type 2 Diabetes Mellitus - Uncontrolled)"],
            ["Urine Microalbumin", "Kidney Function Test (Serum Creatinine)", "Fundoscopy (ਅੱਖਾਂ ਦੇ ਪਰਦੇ ਦੀ ਜਾਂਚ)"],
            "ਮਿੱਠਾ, ਆਲੂ, ਚਾਵਲ ਅਤੇ ਮੈਦਾ ਬੰਦ ਕਰੋ। ਰੋਜ਼ਾਨਾ ੪੫ ਮਿੰਟ ਤੇਜ਼ ਸੈਰ ਕਰੋ। ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਨਾਲ ਦਵਾਈ ਦੀ ਡੋਜ਼ ਐਡਜਸਟ ਕਰਵਾਓ।",
            "ਉੱਚ (High - ੪੮ ਘੰਟਿਆਂ ਵਿੱਚ ਡਾਕਟਰੀ ਸਲਾਹ)"
        ),
        (
            "Lipidology Lab Interpretation",
            "ਲਿਪਿਡ ਪ੍ਰੋਫਾਈਲ: ਕੁੱਲ ਕੋਲੈਸਟ੍ਰੋਲ ੨੮੦ mg/dL, LDL (ਮਾੜਾ ਕੋਲੈਸਟ੍ਰੋਲ) ੧੮੫ mg/dL, ਟਰਾਈਗਲਿਸਰਾਈਡ ੨੪੦ mg/dL, HDL (ਚੰਗਾ ਕੋਲੈਸਟ੍ਰੋਲ) ੩੨ mg/dL",
            "LDL ੧੮੫ mg/dL ਅਤੇ ਟ੍ਰਾਈਗਲਿਸਰਾਈਡ ੨੪੦ mg/dL ਦਿਲ ਦੇ ਦੌਰੇ ਅਤੇ ਨਾੜਾਂ ਬੰਦ ਹੋਣ (Atherosclerosis) ਦੇ ਖ਼ਤਰੇ ਨੂੰ ਕਾਫ਼ੀ ਵਧਾਉਂਦੇ ਹਨ।",
            ["ਗੰਭੀਰ ਹਾਈਪਰਲਿਪੀਡੀਮੀਆ (Severe Dyslipidemia)", "ਕਾਰਡੀਓਵੈਸਕੁਲਰ ਰਿਸਕ"],
            ["12-Lead ECG", "TMT (Treadmill Test)", "High-Sensitivity CRP (hs-CRP)"],
            "ਤਲਿਆ ਭੋਜਨ, ਮੱਖਣ, ਦੇਸੀ ਘਿਓ ਅਤੇ ਮਿੱਠੇ ਪੀਣ ਵਾਲੇ ਪਦਾਰਥ ਬੰਦ ਕਰੋ। ਹਰੀਆਂ ਸਬਜ਼ੀਆਂ, ਸਲਾਦ, ਅਤੇ ਓਟਸ ਖਾਓ। ਸਟੈਟਿਨ ਦਵਾਈ ਬਾਰੇ ਡਾਕਟਰ ਨਾਲ ਗੱਲ ਕਰੋ।",
            "ਉੱਚ (High)"
        ),
        (
            "Hepatic Lab Interpretation",
            "ਲਿਵਰ ਫੰਕਸ਼ਨ ਟੈਸਟ (LFT): ਬਿਲੀਰੂਬਿਨ ੩.੮ mg/dL, SGPT (ALT) ੧੪੦ U/L, SGOT (AST) ੧੨੦ U/L",
            "ਬਿਲੀਰੂਬਿਨ ੩.੮ mg/dL ਅਤੇ ਵਧੇ ਹੋਏ ਲਿਵਰ ਐਨਜ਼ਾਈਮ (SGPT/SGOT) ਐਕਿਊਟ ਹੈਪੇਟਾਈਟਿਸ ਜਾਂ ਲਿਵਰ ਦੀ ਸੋਜਿਸ਼ (Acute Liver Injury / Jaundice) ਵੱਲ ਸੰਕੇਤ ਕਰਦੇ ਹਨ।",
            ["ਪੀਲੀਆ (Acute Hepatitis / Jaundice)", "ਫੈਟੀ ਲਿਵਰ ਗ੍ਰੇਡ ੨", "ਡਰੱਗ-ਇੰਡਿਊਸਡ ਲਿਵਰ ਇੰਜਰੀ"],
            ["Viral Hepatitis Profile (HBsAg, Anti-HCV, IgM Anti-HAV, IgM Anti-HEV)", "Ultrasound Abdomen"],
            "ਚਿਕਨਾਈ ਵਾਲਾ ਭੋਜਨ ਬਿਲਕੁਲ ਬੰਦ। ਉਬਲਿਆ ਪਾਣੀ ਅਤੇ ਹਲਕੀ ਖੁਰਾਕ ਲਓ। ਕੋਈ ਵੀ ਅਣਜਾਣ ਦੇਸੀ ਜੜ੍ਹੀ-ਬੂਟੀ ਜਾਂ ਪੇਨਕਿੱਲਰ ਨਾ ਖਾਓ।",
            "ਉੱਚ (High)"
        ),
        (
            "Renal Lab Interpretation",
            "ਗੁਰਦੇ ਦੀ ਜਾਂਚ (KFT): ਸੀਰਮ ਕ੍ਰੀਏਟੀਨਾਈਨ ੨.੪ mg/dL, ਬਲੱਡ ਯੂਰੀਆ ੬੫ mg/dL, ਯੂਰਿਕ ਐਸਿਡ ੮.੯ mg/dL",
            "ਕ੍ਰੀਏਟੀਨਾਈਨ ੨.੪ mg/dL ਗੁਰਦਿਆਂ ਦੇ ਫਿਲਟਰ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਘਟਣ (Renal Impairment / Early CKD) ਦਾ ਗੰਭੀਰ ਲੱਛਣ ਹੈ।",
            ["ਗੁਰਦੇ ਦੀ ਕਾਰਜਪ੍ਰਣਾਲੀ ਵਿੱਚ ਗਿਰਾਵਟ (Renal Impairment)", "ਹਾਈਪਰਯੂਰੀਸੀਮੀਆ"],
            ["24-Hour Urine Protein", "eGFR calculation", "Ultrasound KUB"],
            "ਲੂਣ ਅਤੇ ਪ੍ਰੋਟੀਨ ਦੀ ਮਾਤਰਾ ਡਾਕਟਰ ਅਨੁਸਾਰ ਸੀਮਤ ਕਰੋ। ਪੇਨਕਿੱਲਰ (NSAIDs) ਕਦੇ ਨਾ ਖਾਓ। ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ ਅਤੇ ਸ਼ੂਗਰ ਨੂੰ ਸਖ਼ਤੀ ਨਾਲ ਕੰਟਰੋਲ ਕਰੋ।",
            "🚨 ਅਤਿ-ਜ਼ਰੂਰੀ (Immediate Nephrologist Consultation)"
        )
    ]

    for cat, report_summary, assess, diff_list, tests, precs, tri in lab_scenarios:
        for age_str, age_label in age_groups:
            for g_str, g_salut in genders:
                query = f"ਡਾਕਟਰ ਸਾਹਿਬ, ਮੇਰੀ {cat} ਦੀ ਰਿਪੋਰਟ ਆਈ ਹੈ: {report_summary}। ਕਿਰਪਾ ਕਰਕੇ ਦੱਸੋ ਇਸਦਾ ਕੀ ਮਤਲਬ ਹੈ ਅਤੇ ਮੈਨੂੰ ਕੀ ਇਲਾਜ ਕਰਵਾਉਣਾ ਚਾਹੀਦਾ ਹੈ?"
                expanded.append({
                    "id": f"amrit_clinical_{current_id:05d}",
                    "domain": cat,
                    "instruction": "ਮਰੀਜ਼ ਦੀ ਲੈਬਾਰਟਰੀ ਟੈਸਟ ਰਿਪੋਰਟ ਦਾ ਡਾਕਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਭਾਵਿਤ ਸਮੱਸਿਆ, ਅਗਲੇ ਜ਼ਰੂਰੀ ਟੈਸਟ ਅਤੇ ਪਰਹੇਜ਼ ਸਪੱਸ਼ਟ ਕਰੋ।",
                    "patient_profile": {
                        "age": age_str,
                        "gender": g_str,
                        "chief_complaint": norm(report_summary)
                    },
                    "patient_query": norm(query),
                    "clinical_assessment": norm(f"{assess} ({g_str}, ਉਮਰ {age_str})।"),
                    "suspected_conditions": [norm(c) for c in diff_list],
                    "triage_level": norm(tri),
                    "suggested_tests": [norm(t) for t in tests],
                    "guidance_and_precautions": norm(precs),
                    "disclaimer": norm("ਇਹ ਵਿਆਖਿਆ AMRIT AI ਮੈਡੀਕਲ ਪ੍ਰਣਾਲੀ ਦੁਆਰਾ ਸਿੱਖਿਆ ਅਤੇ ਸਹਾਇਤਾ ਲਈ ਹੈ। ਰਿਪੋਰਟ ਦੀ ਅੰਤਮ ਪੁਸ਼ਟੀ ਯੋਗ ਡਾਕਟਰ ਤੋਂ ਕਰਵਾਓ।")
                })
                current_id += 1

    return expanded

def main():
    output_dir = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "amrit_punjabi_clinical_dialogue_corpus.jsonl")

    base_corpus = build_clinical_core()
    full_corpus = generate_expanded_clinical_corpus(base_corpus)

    with open(output_file, "w", encoding="utf-8") as f:
        for row in full_corpus:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"✅ Successfully generated AMRIT Punjabi Clinical Dialogue Corpus!")
    print(f"📁 Target file: {output_file}")
    print(f"📊 Total authentic clinical consultations: {len(full_corpus)}")

if __name__ == "__main__":
    main()
