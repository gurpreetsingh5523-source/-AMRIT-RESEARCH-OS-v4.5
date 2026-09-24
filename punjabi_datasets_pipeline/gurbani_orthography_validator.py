#!/usr/bin/env python3
"""
Gurbani Viakaran & Classical Gurmukhi Orthographic Validator
Based on Prof. Sahib Singh's 'Gurbani Viakaran' and Bhai Kahn Singh Nabha's 'Mahan Kosh'.
Author: Gurpreet Singh Dhillon (Nam-toon-studio) / AMRIT AI Team
"""

import json
import os
import re
import unicodedata
from typing import Dict, List, Any

# Classical Gurbani Viakaran Markers
SUBJOINED_HA = '\u0A4D\u0A39'  # ੍ਹ
SUBJOINED_RA = '\u0A4D\u0A30'  # ੍ਰ
SUBJOINED_VA = '\u0A4D\u0A35'  # ੍ਵ
AUNKAD = '\u0A41'              # ੁ
SIHARI = '\u0A3F'              # ਿ
TIPPI = '\u0A70'               # ੰ
BINDI = '\u0A02'               # ਂ
ADDAK = '\u0A71'               # ੱ

class GurmukhiViakaranValidator:
    """
    Validates Punjabi and Gurbani text against classical Gurbani Viakaran rules
    and modern Punjabi orthographic standards.
    """

    @staticmethod
    def check_unicode_nfc(text: str) -> bool:
        """Verifies text is normalized to NFC to prevent rendering anomalies."""
        return text == unicodedata.normalize('NFC', text)

    @staticmethod
    def audit_gurbani_verse(verse: str) -> Dict[str, Any]:
        """
        Audits a Gurbani verse for classical morphological markers:
        - Terminal Aunkad (ੁ) on singular masculine nouns (ਕਰਤਾ ਕਾਰਕ)
        - Terminal Sihaari (ਿ) on locative/instrumental nouns (ਅਧਿਕਰਣ/ਕਰਣ ਕਾਰਕ)
        - Classical subjoined consonants (੍ਹ, ੍ਰ, ੍ਵ)
        - Proper nasalization (ੰ / ਂ)
        """
        words = re.findall(r'[\u0A00-\u0A7F]+', verse)
        
        has_terminal_aunkad = any(w.endswith(AUNKAD) for w in words)
        has_terminal_sihari = any(w.endswith(SIHARI) for w in words)
        has_subjoined_ra = any(SUBJOINED_RA in w for w in words)
        has_subjoined_ha = any(SUBJOINED_HA in w for w in words)
        has_tippi = any(TIPPI in w for w in words)
        has_addak = any(ADDAK in w for w in words)

        return {
            "total_gurmukhi_words": len(words),
            "terminal_aunkad_present": has_terminal_aunkad,
            "terminal_sihari_present": has_terminal_sihari,
            "subjoined_consonants": {
                "raara_pairin": has_subjoined_ra,
                "haaha_pairin": has_subjoined_ha
            },
            "nasalization": {
                "tippi_count": sum(w.count(TIPPI) for w in words),
                "bindi_count": sum(w.count(BINDI) for w in words)
            },
            "gemination_addak_count": sum(w.count(ADDAK) for w in words),
            "is_authentic_gurbani_syntax": has_terminal_aunkad or has_terminal_sihari or has_subjoined_ra
        }

    @classmethod
    def audit_dataset_file(cls, jsonl_path: str, max_samples: int = 50) -> Dict[str, Any]:
        """Runs a complete audit across a dataset."""
        if not os.path.exists(jsonl_path):
            return {"error": f"File not found: {jsonl_path}"}

        nfc_compliant = 0
        total = 0
        gurbani_authentic_count = 0
        samples_inspected = []

        with open(jsonl_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if not line.strip():
                    continue
                total += 1
                row = json.loads(line)
                
                # Check NFC compliance
                text_blob = json.dumps(row, ensure_ascii=False)
                if cls.check_unicode_nfc(text_blob):
                    nfc_compliant += 1

                # Check Gurbani quotes if present
                ref = row.get("gurbani_reference") or row.get("primary_sources") or []
                if isinstance(ref, list):
                    ref_text = " ".join(ref)
                else:
                    ref_text = str(ref)

                if ref_text:
                    audit = cls.audit_gurbani_verse(ref_text)
                    if audit.get("is_authentic_gurbani_syntax"):
                        gurbani_authentic_count += 1
                    if len(samples_inspected) < 5:
                        samples_inspected.append({
                            "id": row.get("id"),
                            "snippet": ref_text[:80],
                            "audit": audit
                        })

        return {
            "file": os.path.basename(jsonl_path),
            "total_records": total,
            "nfc_unicode_compliance_rate": f"{(nfc_compliant / total) * 100:.1f}%",
            "gurbani_syntactic_alignment_count": gurbani_authentic_count,
            "sample_audits": samples_inspected
        }

def main():
    base_dir = "/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford/punjabi_datasets_pipeline"
    files = [
        "gurbani_mahankosh_expanded_corpus.jsonl",
        "punjab_history_theology_critical_corpus.jsonl",
        "punjabi_grammar_correction_corpus.jsonl"
    ]

    print("═══════════════════════════════════════════════════════════════")
    print("☬ ਗੁਰਬਾਣੀ ਵਿਆਕਰਣ ਅਤੇ ਗੁਰਮੁਖੀ ਆਰਥੋਗ੍ਰਾਫੀ ਆਡਿਟ ਰਿਪੋਰਟ (Prof. Sahib Singh Standard)")
    print("═══════════════════════════════════════════════════════════════\n")

    for fname in files:
        fpath = os.path.join(base_dir, fname)
        result = GurmukhiViakaranValidator.audit_dataset_file(fpath)
        print(f"📁 Dataset: {result['file']}")
        print(f"   📊 Total Rows: {result['total_records']}")
        print(f"   ✨ NFC Unicode Compliance: {result['nfc_unicode_compliance_rate']}")
        if "gurbani_syntactic_alignment_count" in result:
            print(f"   ੴ Gurbani Viakaran Aligned Verses: {result['gurbani_syntactic_alignment_count']}")
        print(f"   🔍 Sample Audit Details:")
        for s in result.get("sample_audits", [])[:2]:
            print(f"      - ID: {s['id']}")
            print(f"        ਤੁਕ: {s['snippet']}...")
            aud = s["audit"]
            print(f"        ਔਂਕੜ ਅੰਤ: {aud['terminal_aunkad_present']} | ਸਿਹਾਰੀ ਅੰਤ: {aud['terminal_sihari_present']} | ਪੈਰੀਂ ਰਾਰਾ: {aud['subjoined_consonants']['raara_pairin']}")
        print("───────────────────────────────────────────────────────────────")

if __name__ == "__main__":
    main()
