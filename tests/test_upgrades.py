"""
Unit tests for AMRIT v5.0 upgrades (Digital Twin, Molecular Optimizer, and Smart LIMS).
"""
import unittest
import os
import json
import sqlite3
from core.medical.digital_twin import DigitalTwin
from core.chemistry.molecular_optimizer import MolecularOptimizer
from core.laboratory.lims import SmartLIMS

class TestDigitalTwin(unittest.TestCase):

    def test_digital_twin_metformin(self):
        blood = {"glucose_fasting": 150.0, "hba1c": 7.5}
        dna = {"SLCO1B1": "normal", "CYP2C19": "normal"}
        env = {"diet": "balanced", "exercise": "moderate"}

        twin = DigitalTwin(blood, dna, env)
        res = twin.simulate_clinical_trial("Metformin", 1000.0, 10)
        
        self.assertEqual(res["drug"], "Metformin")
        self.assertEqual(res["dose"], 1000.0)
        self.assertEqual(res["duration_days"], 10)
        self.assertLess(res["final_metrics"]["glucose_fasting"], 150.0)
        self.assertLess(res["final_metrics"]["hba1c"], 7.5)

    def test_digital_twin_statin_myopathy_risk(self):
        blood = {"ldl_cholesterol": 180.0, "total_cholesterol": 260.0}
        # Poor SLCO1B1 metabolizer should have a higher side_effect_probability (statin myopathy)
        twin_poor = DigitalTwin(blood, {"SLCO1B1": "poor"}, {})
        twin_normal = DigitalTwin(blood, {"SLCO1B1": "normal"}, {})

        res_poor = twin_poor.simulate_clinical_trial("Atorvastatin", 80.0, 30)
        res_normal = twin_normal.simulate_clinical_trial("Atorvastatin", 80.0, 30)

        self.assertLess(res_poor["final_metrics"]["ldl_cholesterol"], 180.0)
        self.assertGreater(res_poor["final_metrics"]["side_effect_probability"], 
                           res_normal["final_metrics"]["side_effect_probability"])


class TestMolecularOptimizer(unittest.TestCase):

    def test_calculate_metrics(self):
        opt = MolecularOptimizer()
        metrics = opt.calculate_metrics("CC(=O)OC1=CC=CC=C1C(=O)O", "HMG-CoA")
        
        self.assertIn("binding_affinity", metrics)
        self.assertIn("toxicity", metrics)
        self.assertIn("log_p", metrics)
        self.assertIn("synthesizability", metrics)
        
        # Check nitro group toxicity increase
        toxic_metrics = opt.calculate_metrics("C1=CC(=CC=C1[N+](=O)[O-])C(=O)O", "HMG-CoA")
        self.assertGreater(toxic_metrics["toxicity"], metrics["toxicity"])

    def test_optimize_candidate(self):
        opt = MolecularOptimizer()
        res = opt.optimize_candidate("CC", "HMG-CoA", iterations=3)
        
        self.assertEqual(res["initial_smiles"], "CC")
        self.assertEqual(len(res["trajectory"]), 4) # 0, 1, 2, 3 steps
        self.assertGreaterEqual(res["best_score"], res["trajectory"][0]["score"])


class TestSmartLIMS(unittest.TestCase):
    
    def setUp(self):
        self.db_path = "data/test_lims.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.lims = SmartLIMS(db_path=self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_lims_integrity_and_chaining(self):
        # 1. Log two runs
        h1 = self.lims.log_run("Dr. Amrit", "BloodSimulation", {"sample": "CBC_001"}, {"glucose": 95.0}, "Initial test")
        h2 = self.lims.log_run("Dr. Amrit", "DNAScreening", {"subject": "IND_002"}, {"variant": "SLCO1B1_poor"}, "Genomics run")

        # Check last hash is h2
        self.assertEqual(self.lims.get_last_hash(), h2)

        # Verify integrity
        healthy, issues = self.lims.verify_integrity()
        self.assertTrue(healthy)
        self.assertEqual(len(issues), 0)

        # 2. Tamper database to test integrity verification failure
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE lab_runs SET operator = 'Tampered Operator' WHERE id = 1")

        # Verify integrity should detect tampering
        healthy_after, issues_after = self.lims.verify_integrity()
        self.assertFalse(healthy_after)
        self.assertGreater(len(issues_after), 0)

        # Test compliance report
        report = self.lims.export_compliance_report()
        self.assertEqual(report["lims_status"], "TAMPER_DETECTED")
        self.assertFalse(report["alcoa_standard_met"])
        self.assertEqual(report["total_logged_runs"], 2)

if __name__ == "__main__":
    unittest.main()
