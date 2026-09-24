import os
import json
import re
from typing import Dict, List, Optional
from datetime import datetime

class PatientIntake:
    """
    Manages patient registration, structured voice transcription parsing,
    and local persistence of patient files in data/patients.json.
    """

    def __init__(self, db_path: str = "data/patients.json"):
        self.db_path = db_path
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        # Initialize file if empty/missing
        if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load_all(self) -> List[Dict]:
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save_all(self, patients: List[Dict]):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(patients, f, indent=2, ensure_ascii=False)

    def parse_voice_intake(self, transcript: str) -> Dict:
        """
        Parses unstructured English/Punjabi voice transcripts to extract:
        name, address, emergency_phone, bp (blood pressure), weight.
        """
        parsed = {
            "name": "Unknown Patient",
            "address": "Not provided",
            "emergency_phone": "Not provided",
            "bp": "Not provided",
            "weight": "Not provided",
            "medical_history": [],
            "blood": {},
            "dna_variants": {}
        }

        # --- Name Extraction ---
        # English patterns
        name_match = re.search(r"(?:patient name is|patient named|register patient|patient)\s+(.+?)(?=\s+(?:address|phone|emergency|bp|weight|living|is from|$))", transcript, re.IGNORECASE)
        # Punjabi patterns
        pb_name_match = re.search(r"(?:ਮਰੀਜ਼|ਨਾਮ)\s+(.+?)(?=\s+(?:ਪਤਾ|ਫ਼ੋਨ|ਫੋਨ|ਬੀਪੀ|ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ|ਵਜ਼ਨ|$))", transcript)

        if name_match:
            name_cand = name_match.group(1).strip()
            if name_cand:
                parsed["name"] = name_cand
        elif pb_name_match:
            name_cand = pb_name_match.group(1).strip()
            if name_cand:
                parsed["name"] = name_cand

        # --- Address Extraction ---
        addr_match = re.search(r"(?:address is|address|lives in|living in|from)\s+([a-zA-Z0-9\s,]+?)(?:phone|emergency|bp|weight|blood|$)", transcript, re.IGNORECASE)
        pb_addr_match = re.search(r"(?:ਪਤਾ|ਰਹਿਣ ਵਾਲਾ)\s+(.+?)(?:ਫ਼ੋਨ|ਫੋਨ|ਬੀਪੀ|ਵਜ਼ਨ|$)", transcript)

        if addr_match:
            parsed["address"] = addr_match.group(1).strip()
        elif pb_addr_match:
            parsed["address"] = pb_addr_match.group(1).strip()

        # --- Emergency Phone Extraction ---
        phone_match = re.search(r"(?:phone|emergency phone|emergency|mobile|number is|phone number)\s+(\+?[0-9\-\s]{5,15})", transcript, re.IGNORECASE)
        pb_phone_match = re.search(r"(?:ਫ਼ੋਨ|ਫੋਨ|ਮੋਬਾਈਲ|ਨੰਬਰ)\s+(\+?[0-9\-\s]{5,15})", transcript)

        if phone_match:
            parsed["emergency_phone"] = phone_match.group(1).strip()
        elif pb_phone_match:
            parsed["emergency_phone"] = pb_phone_match.group(1).strip()

        # --- BP Extraction ---
        bp_match = re.search(r"(?:bp|blood pressure|pressure is|pressure)\s+([0-9]{2,3}/[0-9]{2,3})", transcript, re.IGNORECASE)
        pb_bp_match = re.search(r"(?:ਬੀਪੀ|ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ)\s+([0-9]{2,3}/[0-9]{2,3})", transcript)

        if bp_match:
            parsed["bp"] = bp_match.group(1).strip()
        elif pb_bp_match:
            parsed["bp"] = pb_bp_match.group(1).strip()

        # --- Weight Extraction ---
        weight_match = re.search(r"(?:weight|weight is)\s+([0-9]+(?:\.[0-9]+)?\s*(?:kg|lbs|kilograms|kilos))", transcript, re.IGNORECASE)
        pb_weight_match = re.search(r"(?:ਵਜ਼ਨ|ਭਾਰ)\s+([0-9]+(?:\.[0-9]+)?\s*(?:ਕਿਲੋ|ਕਿ.ਗ੍ਰਾ.|ਕਿਲੋਗ੍ਰਾਮ|ਕਿਲੋਗ੍ਰਾਮਸ|kg))", transcript)

        if weight_match:
            parsed["weight"] = weight_match.group(1).strip()
        elif pb_weight_match:
            parsed["weight"] = pb_weight_match.group(1).strip()

        # Try to parse blood parameters if mentioned (e.g. Glucose: 130)
        glucose_match = re.search(r"(?:glucose|sugar|ਗਲੂਕੋਜ਼)\s*(?:is|value|:)?\s*([0-9]+)", transcript, re.IGNORECASE)
        if glucose_match:
            parsed["blood"]["glucose_fasting"] = float(glucose_match.group(1))

        chol_match = re.search(r"(?:cholesterol|ldl|ਕੋਲੈਸਟ੍ਰੋਲ)\s*(?:is|value|:)?\s*([0-9]+)", transcript, re.IGNORECASE)
        if chol_match:
            parsed["blood"]["ldl_cholesterol"] = float(chol_match.group(1))

        # Clean trailing punctuation from values
        for key in ["name", "address", "emergency_phone", "bp", "weight"]:
            if isinstance(parsed[key], str):
                parsed[key] = parsed[key].strip(",. :;")

        return parsed

    def register_patient(self, patient_data: Dict) -> Dict:
        """
        Registers a new patient or updates an existing one by matching patient_id or name.
        """
        patients = self._load_all()

        # Generate a simple unique ID if missing
        patient_id = patient_data.get("id") or patient_data.get("patient_id")
        if not patient_id:
            cleaned_name = re.sub(r"\s+", "_", patient_data.get("name", "patient").lower())
            patient_id = f"P_{cleaned_name}_{len(patients) + 1}"

        # Check if already exists to overwrite/update
        existing_idx = -1
        for i, p in enumerate(patients):
            if p.get("id") == patient_id or (p.get("name").lower() == patient_data.get("name").lower() and p.get("name") != "Unknown Patient"):
                existing_idx = i
                break

        # Auto-compute face vector if face_image is provided
        face_vector = patient_data.get("face_vector")
        face_image = patient_data.get("face_image")
        if face_image and not face_vector:
            from core.medical.face_recall import FaceRecallEngine
            fre = FaceRecallEngine()
            face_vector = fre.generate_face_vector(face_image)

        # Construct unified record
        record = {
            "id": patient_id,
            "name": patient_data.get("name", "Unknown Patient"),
            "address": patient_data.get("address", "Not provided"),
            "emergency_phone": patient_data.get("emergency_phone", "Not provided"),
            "bp": patient_data.get("bp", "Not provided"),
            "weight": patient_data.get("weight", "Not provided"),
            "medical_history": patient_data.get("medical_history", []),
            "blood": patient_data.get("blood", {}),
            "dna_variants": patient_data.get("dna_variants", {}),
            "visual_scans": patient_data.get("visual_scans", []),
            "face_vector": face_vector,
            "registered_at": patient_data.get("registered_at") or datetime.now().isoformat()
        }

        if existing_idx >= 0:
            # Merge fields
            old_record = patients[existing_idx]
            old_record.update(record)
            patients[existing_idx] = old_record
            record = old_record
        else:
            patients.append(record)

        self._save_all(patients)
        return record

    def get_patient(self, patient_id: str) -> Optional[Dict]:
        patients = self._load_all()
        for p in patients:
            if p.get("id") == patient_id:
                return p
        return None

    def list_all_patients(self) -> List[Dict]:
        return self._load_all()
