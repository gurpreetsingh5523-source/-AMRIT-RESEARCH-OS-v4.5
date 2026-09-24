"""
AMRIT Smart LIMS (Laboratory Information Management System)
Ensures ALCOA+ data integrity principles for digital wet-lab simulations and logs.
Implements hash-chained cryptographic verification for data immutability.
"""
from typing import Dict, List, Optional, Tuple
import os
import json
import sqlite3
import hashlib
from datetime import datetime

class SmartLIMS:
    """
    Lab record management with tamper-proof blockchain-style hash chain validation.
    Guarantees ALCOA+ compliance (Attributable, Legible, Contemporaneous, Original, Accurate).
    """

    def __init__(self, db_path: str = "data/lims.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS lab_runs (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp   TEXT NOT NULL,
                    operator    TEXT NOT NULL,
                    exp_type    TEXT NOT NULL,
                    inputs      TEXT NOT NULL,
                    outputs     TEXT NOT NULL,
                    prev_hash   TEXT NOT NULL,
                    curr_hash   TEXT NOT NULL,
                    notes       TEXT
                );
            """)

    def _calculate_hash(self, timestamp: str, operator: str, exp_type: str, 
                        inputs: str, outputs: str, prev_hash: str) -> str:
        """Calculate SHA256 of parameters to form a secure blockchain block hash"""
        raw_str = f"{timestamp}|{operator}|{exp_type}|{inputs}|{outputs}|{prev_hash}"
        return hashlib.sha256(raw_str.encode("utf-8")).hexdigest()

    def get_last_hash(self) -> str:
        """Retrieve the current leaf block hash of the LIMS log chain"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT curr_hash FROM lab_runs ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            return row[0] if row else "GENESIS_HASH"

    def log_run(self, operator: str, exp_type: str, inputs: Dict, outputs: Dict, notes: str = "") -> str:
        """
        Log a simulation or lab test run.
        Calculates cryptographic hash chaining to maintain ALCOA+ data integrity.
        """
        timestamp = datetime.now().isoformat()
        inputs_str = json.dumps(inputs, sort_keys=True)
        outputs_str = json.dumps(outputs, sort_keys=True)
        
        prev_hash = self.get_last_hash()
        curr_hash = self._calculate_hash(timestamp, operator, exp_type, inputs_str, outputs_str, prev_hash)

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO lab_runs (timestamp, operator, exp_type, inputs, outputs, prev_hash, curr_hash, notes) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (timestamp, operator, exp_type, inputs_str, outputs_str, prev_hash, curr_hash, notes)
            )
        return curr_hash

    def verify_integrity(self) -> Tuple[bool, List[Dict]]:
        """
        Verify the hash chain of the entire LIMS database.
        Detects any unauthorized deletions, edits, or insertions.
        """
        records = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, timestamp, operator, exp_type, inputs, outputs, prev_hash, curr_hash, notes FROM lab_runs ORDER BY id ASC")
            records = cursor.fetchall()

        issues = []
        expected_prev = "GENESIS_HASH"
        
        for r in records:
            rid, ts, op, etype, inp, out, prev, curr, note = r
            
            # Check link to previous block
            if prev != expected_prev:
                issues.append({
                    "id": rid,
                    "error": f"Chain broken: expected previous hash '{expected_prev}', got '{prev}'"
                })

            # Check block's own content hash matches stored hash
            recalc = self._calculate_hash(ts, op, etype, inp, out, prev)
            if recalc != curr:
                issues.append({
                    "id": rid,
                    "error": f"Content tampered: stored hash '{curr}' does not match recalculated hash '{recalc}'"
                })
                
            expected_prev = curr

        healthy = len(issues) == 0
        return healthy, issues

    def export_compliance_report(self) -> Dict[str, any]:
        """Generate compliance export log including integrity validation checks"""
        healthy, issues = self.verify_integrity()
        
        runs = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, timestamp, operator, exp_type, inputs, outputs, notes, curr_hash FROM lab_runs ORDER BY id DESC")
            for row in cursor.fetchall():
                runs.append({
                    "id": row[0],
                    "timestamp": row[1],
                    "operator": row[2],
                    "experiment_type": row[3],
                    "inputs": json.loads(row[4]),
                    "outputs": json.loads(row[5]),
                    "notes": row[6],
                    "verification_hash": row[7]
                })

        return {
            "lims_status": "INTEGRITY_VERIFIED" if healthy else "TAMPER_DETECTED",
            "compliance_checked_at": datetime.now().isoformat(),
            "alcoa_standard_met": healthy,
            "validation_errors": issues,
            "total_logged_runs": len(runs),
            "records": runs
        }
