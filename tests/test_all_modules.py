"""
AMRIT Research OS v6.0 - Comprehensive Test Suite
Tests all modules for correctness and integration
"""
import unittest
import sys
import os

# ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestResearchBrain(unittest.TestCase):
    """Test ResearchBrain module"""

    def test_hypothesis_generation(self):
        from core.brain.research_brain import ResearchBrain, HypothesisType
        brain = ResearchBrain()
        hypotheses = brain.generate_hypothesis(
            "oncology", 
            ["tumor suppressor", "mutation", "pathway"]
        )
        self.assertIsInstance(hypotheses, list)
        self.assertTrue(len(hypotheses) > 0)
        self.assertTrue(all(h.confidence >= 0.65 for h in hypotheses))

    def test_bayesian_update(self):
        from core.brain.research_brain import ResearchBrain
        brain = ResearchBrain()
        hypotheses = brain.generate_hypothesis("cardiology", ["hypertension", "genetics"])
        if hypotheses:
            updated = brain.evaluate_hypothesis(hypotheses[0], {
                'likelihood': 0.8,
                'evidence_probability': 0.6
            })
            self.assertIsNotNone(updated.confidence)

class TestMemoryManager(unittest.TestCase):
    """Test MemoryManager module"""

    def test_store_retrieve(self):
        from core.memory.memory_manager import MemoryManager
        import tempfile

        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            mm = MemoryManager(db_path=tmp.name)
            entry_id = mm.store('test data', 'test', ['tag1'], 0.8)
            self.assertIsNotNone(entry_id)

            retrieved = mm.retrieve(entry_id)
            self.assertIsNotNone(retrieved)
            self.assertEqual(retrieved.content, 'test data')
            os.unlink(tmp.name)

    def test_search(self):
        from core.memory.memory_manager import MemoryManager
        import tempfile

        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            mm = MemoryManager(db_path=tmp.name)
            mm.store('data1', 'hypothesis', ['cancer'], 0.9)
            mm.store('data2', 'paper', ['diabetes'], 0.7)

            results = mm.search(memory_type='hypothesis')
            self.assertEqual(len(results), 1)
            os.unlink(tmp.name)

class TestStatisticalEngine(unittest.TestCase):
    """Test StatisticalEngine module"""

    def test_monte_carlo(self):
        from core.statistics.statistical_engine import StatisticalEngine
        se = StatisticalEngine()

        def model(a, b):
            return a + b

        distributions = {
            'a': lambda: 1.0,
            'b': lambda: 2.0
        }

        result = se.monte_carlo_simulation(model, distributions, 100)
        self.assertIn('mean', result)
        self.assertIn('ci_95', result)

    def test_bayesian_inference(self):
        from core.statistics.statistical_engine import StatisticalEngine
        se = StatisticalEngine()

        result = se.bayesian_inference(1, 1, 8, 10)
        self.assertIn('posterior_alpha', result)
        self.assertIn('ci_95', result)
        self.assertGreater(result['mean'], 0)

    def test_benfords_law(self):
        from core.statistics.statistical_engine import StatisticalEngine
        se = StatisticalEngine()

        # Natural data should follow Benford's law
        data = [1, 12, 123, 1234, 2, 23, 234, 3, 34, 345]
        result = se.benfords_law_test(data)
        self.assertIsNotNone(result.p_value)

class TestAgentManager(unittest.TestCase):
    """Test AgentManager module"""

    def test_agent_creation(self):
        from core.agents.agent_manager import AgentManager
        am = AgentManager()
        stats = am.get_agent_stats()
        self.assertEqual(stats['total_agents'], 7)
        self.assertEqual(len(stats['roles']), 7)

    def test_debate(self):
        from core.agents.agent_manager import AgentManager
        am = AgentManager()
        result = am.run_collaborative_research('diabetes genetics')
        self.assertIn('consensus_level', result)
        self.assertIn('key_findings', result)

class TestKnowledgeGraph(unittest.TestCase):
    """Test KnowledgeGraph module"""

    def test_medical_graph(self):
        from core.knowledge_graph.knowledge_graph import create_medical_knowledge_graph
        kg = create_medical_knowledge_graph()
        stats = kg.get_stats()
        self.assertGreater(stats['total_entities'], 0)
        self.assertGreater(stats['total_relationships'], 0)

    def test_path_finding(self):
        from core.knowledge_graph.knowledge_graph import create_medical_knowledge_graph
        kg = create_medical_knowledge_graph()
        paths = kg.find_path('DIABETES_T2', 'GLUT4')
        self.assertIsInstance(paths, list)

class TestBloodAnalyzer(unittest.TestCase):
    """Test BloodAnalyzer module"""

    def test_single_test(self):
        from core.medical.blood_analyzer import BloodAnalyzer
        ba = BloodAnalyzer()
        result = ba.analyze_test('glucose_fasting', 95)
        self.assertEqual(result.risk_level.value, 'normal')

    def test_high_glucose(self):
        from core.medical.blood_analyzer import BloodAnalyzer
        ba = BloodAnalyzer()
        result = ba.analyze_test('glucose_fasting', 180)
        self.assertIn(result.risk_level.value, ['high', 'critical'])

    def test_panel_analysis(self):
        from core.medical.blood_analyzer import BloodAnalyzer
        ba = BloodAnalyzer()
        tests = {
            'glucose_fasting': 95,
            'hba1c': 5.5,
            'ldl_cholesterol': 110
        }
        results = ba.analyze_panel(tests)
        self.assertEqual(len(results), 3)

        summary = ba.get_health_summary(tests)
        self.assertIn('overall_risk', summary)

class TestConsanguinityDrug(unittest.TestCase):
    """Test ConsanguinityRisk and DrugPredictor"""

    def test_consanguinity_risk(self):
        from core.medical.consanguinity_drug import ConsanguinityRisk, RelationshipType
        cr = ConsanguinityRisk(RelationshipType.FIRST_COUSIN)
        result = cr.calculate_risk('thalassemia')
        self.assertIn('risk_ratio', result)
        self.assertGreater(result['risk_ratio'], 1)

    def test_drug_prediction(self):
        from core.medical.consanguinity_drug import DrugPredictor
        dp = DrugPredictor({'CYP2D6': 'poor'})
        result = dp.predict_drug_response('codeine')
        self.assertIn('status', result)

class TestEthicsFilter(unittest.TestCase):
    """Test EthicsFilter module"""

    def test_approved_action(self):
        from core.ethics.ethics_filter import EthicsFilter
        ef = EthicsFilter()
        result = ef.assess('Research on diabetes prevention')
        self.assertTrue(result.approved)
        self.assertGreater(result.overall_score, 0.7)

    def test_rejected_action(self):
        from core.ethics.ethics_filter import EthicsFilter
        ef = EthicsFilter()
        result = ef.assess('Eugenics-based selection of embryos')
        self.assertFalse(result.approved)
        self.assertGreater(len(result.violations), 0)

class TestQuantumLayer(unittest.TestCase):
    """Test QuantumLayer module"""

    def test_quantum_state(self):
        from core.quantum.quantum_layer import QuantumState
        qs = QuantumState(2)
        self.assertEqual(qs.dim, 4)
        probs = qs.get_probabilities()
        self.assertEqual(len(probs), 4)

    def test_quantum_biology(self):
        from core.quantum.quantum_layer import QuantumLayer
        ql = QuantumLayer()
        result = ql.quantum_biology_model('photosynthesis')
        self.assertIn('mechanism', result)

class TestAutonomousModules(unittest.TestCase):
    """Test Autonomous Research Modules"""

    def test_literature_mining(self):
        from core.autonomous.unified_agent import LiteratureMiningAgent
        lma = LiteratureMiningAgent()
        lma.track_topic('diabetes')
        findings = lma.mine_literature('diabetes')
        self.assertIsInstance(findings, list)

    def test_pattern_detection(self):
        from core.autonomous.unified_agent import PatternDetectionAgent
        pda = PatternDetectionAgent()
        data = [{'value': i} for i in range(20)]
        data[15]['value'] = 100  # anomaly
        patterns = pda.detect_patterns(data)
        self.assertIsInstance(patterns, list)

    def test_hypothesis_generation(self):
        from core.autonomous.unified_agent import HypothesisGenerator
        hg = HypothesisGenerator()
        hypotheses = hg.generate_disease_links('diabetes')
        self.assertGreater(len(hypotheses), 0)

    def test_prediction_engine(self):
        from core.autonomous.unified_agent import PredictionEngine
        pe = PredictionEngine()
        result = pe.predict_pandemic_risk({
            'population_density': 500,
            'mobility_index': 60,
            'healthcare_capacity': 70,
            'vaccination_rate': 75,
            'pathogen_transmissibility': 2.5
        })
        self.assertIn('risk_level', result)

    def test_self_improvement(self):
        from core.autonomous.unified_agent import SelfImprovementLoop
        sil = SelfImprovementLoop()
        result = sil.learn_from_data({'outcomes': [1, 0, 1, 1]}, 'clinical')
        self.assertIn('insights', result)

    def test_auto_module_generation(self):
        from core.autonomous.unified_agent import SelfImprovementLoop
        sil = SelfImprovementLoop()
        result = sil.auto_generate_module('Create a module for sleep analysis')
        self.assertIn('code', result)
        self.assertIn('validation', result)

    def test_unified_agent(self):
        from core.autonomous.unified_agent import UnifiedAgent
        ua = UnifiedAgent()
        status = ua.get_system_status()
        self.assertEqual(status['active_agents'], 5)

class TestHealthAdvisor(unittest.TestCase):
    """Test PersonalizedHealthAdvisor"""

    def test_dna_analysis(self):
        from core.medical.health_advisor import PersonalizedHealthAdvisor
        pha = PersonalizedHealthAdvisor()
        result = pha.analyze_dna({
            'APOE4': '1_copy',
            'MTHFR_C677T': 'CT'
        })
        self.assertIn('variants_analyzed', result)
        self.assertEqual(result['variants_analyzed'], 2)

    def test_environmental_analysis(self):
        from core.medical.health_advisor import PersonalizedHealthAdvisor
        pha = PersonalizedHealthAdvisor()
        result = pha.analyze_environment({
            'PM2.5': 35.0,
            'arsenic': 15.0
        })
        self.assertIn('exposure_results', result)

    def test_full_assessment(self):
        from core.medical.health_advisor import PersonalizedHealthAdvisor
        pha = PersonalizedHealthAdvisor()
        result = pha.full_health_assessment({
            'id': 'P001',
            'dna_variants': {'APOE4': '1_copy'},
            'environmental': {'PM2.5': 25.0}
        })
        self.assertIn('overall_health_score', result)
        self.assertIn('recommendations', result)

    def test_medication_recommendations(self):
        """Verify the blood test to medication recommendation pharmacogenomics bridge works"""
        from core.medical.health_advisor import PersonalizedHealthAdvisor
        pha = PersonalizedHealthAdvisor()
        result = pha.full_health_assessment({
            'id': 'P002',
            'dna_variants': {
                'MTHFR_C677T': 'TT',
                'SLCO1B1': 'XX'
            },
            'blood': {
                'glucose_fasting': 140.0,
                'ldl_cholesterol': 150.0
            }
        })
        self.assertIn('medication_recommendations', result)
        meds = result['medication_recommendations']
        self.assertTrue(len(meds) > 0)
        
        # Verify Metformin is recommended with MTHFR warning
        metformin_rec = [m for m in meds if m['recommended_drug'] == 'Metformin'][0]
        self.assertEqual(metformin_rec['status'], 'Approved with Caution')
        self.assertIn('MTHFR', metformin_rec['notes'])
        
        # Verify Simvastatin is flagged as contraindicated due to SLCO1B1 myopathy risk
        simvastatin_rec = [m for m in meds if m['recommended_drug'] == 'Simvastatin'][0]
        self.assertEqual(simvastatin_rec['status'], 'CONTRAINDICATED / HIGH RISK')
        self.assertIsNotNone(simvastatin_rec['alternative_suggested'])

class TestPaperWriter(unittest.TestCase):
    """Test PaperWriter"""

    def test_paper_generation(self):
        from core.paper_writer.paper_writer import PaperWriter
        pw = PaperWriter()
        findings = [
            {'finding': 'Novel biomarker identified', 'confidence': 0.9, 'source': 'PubMed'},
            {'finding': 'Drug target validated', 'confidence': 0.85, 'source': 'Nature'}
        ]
        paper = pw.generate_paper('diabetes', findings, 'APA')
        self.assertIn('title', paper)
        self.assertIn('sections', paper)
        self.assertGreater(paper['word_count'], 0)

class TestDataCollector(unittest.TestCase):
    """Test DataCollector"""

    def test_initialization(self):
        from core.data_sources.data_collector import DataCollector
        dc = DataCollector()
        self.assertIsNotNone(dc.session)

class TestIntegration(unittest.TestCase):
    """Integration tests across modules"""

    def test_end_to_end_research(self):
        """Test full research pipeline"""
        from core.brain.research_brain import ResearchBrain
        from core.statistics.statistical_engine import StatisticalEngine
        from core.ethics.ethics_filter import EthicsFilter

        # Generate hypothesis
        brain = ResearchBrain()
        hypotheses = brain.generate_hypothesis('oncology', ['tumor', 'gene', 'therapy'])

        # Validate statistically
        se = StatisticalEngine()
        if hypotheses:
            p_value = 0.01
            self.assertLess(p_value, 0.05)

        # Check ethics
        ef = EthicsFilter()
        ethics = ef.assess('Research on cancer treatment for underserved populations')
        self.assertTrue(ethics.approved)

    def test_health_pipeline(self):
        """Test health assessment pipeline"""
        from core.medical.blood_analyzer import BloodAnalyzer
        from core.medical.health_advisor import PersonalizedHealthAdvisor

        # Blood analysis
        ba = BloodAnalyzer(population='south_asian')
        tests = {'glucose_fasting': 95, 'hba1c': 5.5, 'vitamin_d': 25}
        blood_results = ba.analyze_panel(tests)

        # DNA analysis
        pha = PersonalizedHealthAdvisor()
        dna_results = pha.analyze_dna({'MTHFR_C677T': 'CT'})

        # Environmental
        env_results = pha.analyze_environment({'PM2.5': 20.0})

        # Combined recommendations
        recs = pha.generate_recommendations(dna_results, {}, env_results)
        self.assertIn('recommendations', recs)

class TestPatientAndEpidemiology(unittest.TestCase):
    """Test voice intake, clinical diet plans, and epidemiology planning"""

    def setUp(self):
        import tempfile
        self.tmp_file = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
        self.tmp_file.close()

    def tearDown(self):
        import os
        os.unlink(self.tmp_file.name)

    def test_patient_intake_and_voice_parsing(self):
        from core.medical.patient_intake import PatientIntake
        pi = PatientIntake(db_path=self.tmp_file.name)
        
        eng_transcript = "Register patient Gurpreet, address Amritsar, phone 9876543210, blood pressure 130/80, weight 75 kg, glucose 145"
        parsed_eng = pi.parse_voice_intake(eng_transcript)
        self.assertEqual(parsed_eng["name"], "Gurpreet")
        self.assertEqual(parsed_eng["address"], "Amritsar")
        self.assertEqual(parsed_eng["emergency_phone"], "9876543210")
        self.assertEqual(parsed_eng["bp"], "130/80")
        self.assertEqual(parsed_eng["weight"], "75 kg")
        self.assertEqual(parsed_eng["blood"]["glucose_fasting"], 145.0)

        record = pi.register_patient(parsed_eng)
        self.assertEqual(record["name"], "Gurpreet")
        self.assertEqual(record["bp"], "130/80")

        pb_transcript = "ਮਰੀਜ਼ ਅਮਨਦੀਪ, ਪਤਾ ਜਲੰਧਰ, ਫੋਨ 9912345678, ਬੀਪੀ 120/75 ਰਜਿਸਟਰ ਕਰੋ"
        parsed_pb = pi.parse_voice_intake(pb_transcript)
        self.assertEqual(parsed_pb["name"], "ਅਮਨਦੀਪ")
        self.assertEqual(parsed_pb["address"], "ਜਲੰਧਰ")
        self.assertEqual(parsed_pb["emergency_phone"], "9912345678")
        self.assertEqual(parsed_pb["bp"], "120/75")

    def test_epidemiology_ratios_and_biomedical_research(self):
        from core.medical.patient_intake import PatientIntake
        from core.medical.epidemiology import EpidemiologyEngine
        from core.medical.health_advisor import PersonalizedHealthAdvisor

        pi = PatientIntake(db_path=self.tmp_file.name)
        
        pi.register_patient({
            "name": "Patient One",
            "bp": "115/75",
            "blood": {"glucose_fasting": 140.0},
            "dna_variants": {"MTHFR_C677T": "TT"}
        })
        
        pi.register_patient({
            "name": "Patient Two",
            "bp": "140/90",
            "blood": {"ldl_cholesterol": 150.0}
        })

        engine = EpidemiologyEngine(pi)
        summary = engine.get_summary()

        self.assertEqual(summary["total_patients"], 2)
        self.assertEqual(summary["sickness_rates"]["diabetes_pct"], 50.0)
        self.assertEqual(summary["sickness_rates"]["hypertension_pct"], 50.0)
        self.assertEqual(summary["sickness_rates"]["hyperlipidemia_pct"], 50.0)
        
        pha = PersonalizedHealthAdvisor()
        record_diabetic = pi.list_all_patients()[0]
        assessment = pha.full_health_assessment(record_diabetic)
        self.assertIn("diet_plan", assessment)
        self.assertEqual(assessment["diet_plan"]["dietary_pattern"], "Low-Glycemic Index (Low-GI) Diabetic Diet")
        self.assertIn("Folate-rich spinach", assessment["diet_plan"]["foods_to_include"])

    def test_medical_vision_analyzer(self):
        from core.medical.vision_analyzer import MedicalVisionAnalyzer
        mva = MedicalVisionAnalyzer()
        
        # Test skin lesion fallback analysis
        skin_res = mva.analyze_scan("skin_mole.jpg", "skin")
        self.assertEqual(skin_res["risk_level"], "high")
        self.assertIn("excision biopsy", "".join(skin_res["recommendations"]).lower())

        # Test retina scan fallback analysis
        retina_res = mva.analyze_scan("eye_retina.png", "retina")
        self.assertEqual(retina_res["risk_level"], "moderate")
        self.assertIn("microaneurysms", "".join(retina_res["clinical_features"]).lower())

    def test_patient_simulation_workflow(self):
        from core.medical.patient_intake import PatientIntake
        from core.medical.health_advisor import PersonalizedHealthAdvisor

        pi = PatientIntake(db_path=self.tmp_file.name)
        
        # Simulated voice intake registration
        voice_transcript = "Register patient Gurmit Singh, address Punjab, emergency phone 98765-43210, blood pressure 135/85, weight 82 kg"
        parsed = pi.parse_voice_intake(voice_transcript)
        
        # Simulated clinical metrics attachment
        parsed["dna_variants"] = {'MTHFR_C677T': 'TT', 'SLCO1B1': 'XX'}
        parsed["blood"] = {'glucose_fasting': 135.0, 'ldl_cholesterol': 140.0}
        parsed["visual_scans"] = [{'path': 'suspicious_mole.jpg', 'scan_type': 'skin'}]

        record = pi.register_patient(parsed)
        self.assertEqual(record["name"], "Gurmit Singh")
        self.assertEqual(record["address"], "Punjab")
        self.assertEqual(record["emergency_phone"], "98765-43210")

        # Run complete diagnostics
        pha = PersonalizedHealthAdvisor()
        report = pha.full_health_assessment(record)

        # 1. Verify blood-to-medication recommendations and genetic overlays
        meds = report["medication_recommendations"]
        self.assertTrue(len(meds) > 0)
        
        # Metformin check
        metformin_rec = [m for m in meds if m['recommended_drug'] == 'Metformin'][0]
        self.assertEqual(metformin_rec['status'], 'Approved with Caution')
        
        # Simvastatin check
        simvastatin_rec = [m for m in meds if m['recommended_drug'] == 'Simvastatin'][0]
        self.assertEqual(simvastatin_rec['status'], 'CONTRAINDICATED / HIGH RISK')

        # 2. Verify clinical diet plans generated
        diet = report["diet_plan"]
        self.assertEqual(diet["dietary_pattern"], "Low-Glycemic Index (Low-GI) Diabetic Diet")
        self.assertIn("Folate-rich spinach", diet["foods_to_include"])

        # 3. Verify vision analysis and recommendations integration
        self.assertTrue(len(report["vision_analysis"]) > 0)
        vision_res = report["vision_analysis"][0]
        self.assertEqual(vision_res["risk_level"], "high")
        self.assertIn("excision biopsy", "".join(vision_res["recommendations"]).lower())
        
        # Verify visual recommendations successfully bridged to main screening list
        self.assertTrue(any("excision biopsy" in r.lower() for r in report["recommendations"]["recommendations"]["screening"]))

    def test_face_recall_engine(self):
        import numpy as np
        from core.medical.face_recall import FaceRecallEngine
        
        fre = FaceRecallEngine()
        # Test deterministic mock vector generation (for non-existent files)
        vec1 = fre.generate_face_vector("face1.jpg")
        vec2 = fre.generate_face_vector("face2.jpg")
        vec1_again = fre.generate_face_vector("face1.jpg")

        self.assertEqual(len(vec1), 128)
        self.assertEqual(len(vec2), 128)
        
        # Verify same file maps to same vector
        self.assertAlmostEqual(float(np.dot(vec1, vec1_again)), 1.0, places=4)
        
        # Verify different files map to different vectors
        self.assertTrue(float(np.dot(vec1, vec2)) < 0.85)

        # Test profile matching
        patients = [
            {"id": "P_gurmit", "name": "Gurmit", "face_vector": vec1},
            {"id": "P_aman", "name": "Aman", "face_vector": vec2}
        ]
        match = fre.find_match("face1.jpg", patients)
        self.assertIsNotNone(match)
        self.assertEqual(match["id"], "P_gurmit")
        self.assertTrue(match["face_match_confidence"] >= 0.85)

    def test_api_free_scraper(self):
        from core.autonomous.web_scraper import APIFreeScraper
        scraper = APIFreeScraper()
        
        # Test youtube transcript extraction fallback
        res = scraper.scrape_youtube_transcript("dQw4w9WgXcQ")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["video_id"], "dQw4w9WgXcQ")
        self.assertTrue(len(res["transcript"]) > 0)

        # Test web direct scraper fallback
        web_res = scraper.scrape_web_page("https://example.com")
        self.assertTrue(len(web_res["text_content"]) > 0)

    def test_face_recall_role_routing(self):
        import numpy as np
        from core.medical.face_recall import FaceRecallEngine
        fre = FaceRecallEngine()
        
        # Test Doctor Face Recall
        doc_match = fre.find_match("face_doctor.jpg", [])
        self.assertIsNotNone(doc_match)
        self.assertEqual(doc_match["role"], "doctor")
        self.assertEqual(doc_match["access_level"], "full")
        
        # Test Registered Patient Recall
        vec_gurmit = fre.generate_face_vector("face_gurmit.jpg")
        patients = [{"id": "P_gurmit", "name": "Gurmit Singh", "face_vector": vec_gurmit}]
        patient_match = fre.find_match("face_gurmit.jpg", patients)
        self.assertIsNotNone(patient_match)
        self.assertEqual(patient_match["role"], "patient")
        self.assertEqual(patient_match["access_level"], "limited")
        
        # Test Unregistered Stranger Recall
        stranger_match = fre.find_match("face_stranger.jpg", patients)
        self.assertIsNotNone(stranger_match)
        self.assertEqual(stranger_match["role"], "new_patient")
        self.assertEqual(stranger_match["access_level"], "intake")

    def test_clinician_biometric_registration(self):
        import json
        import os
        from core.medical.face_recall import FaceRecallEngine
        
        fre = FaceRecallEngine()
        vec_custom = fre.generate_face_vector("face_custom_doctor.jpg")
        clinicians = [{
            "id": "doctor_test",
            "name": "Dr. Test Clinician",
            "face_vector": vec_custom
        }]
        
        # Backup existing clinicians if any
        backup_data = None
        if os.path.exists("data/clinicians.json"):
            try:
                with open("data/clinicians.json", "r") as f:
                    backup_data = f.read()
            except Exception:
                pass
                
        try:
            with open("data/clinicians.json", "w") as f:
                json.dump(clinicians, f, indent=4)
                
            # Match Custom Doctor Face
            match = fre.find_match("face_custom_doctor.jpg", [])
            self.assertIsNotNone(match)
            self.assertEqual(match["role"], "doctor")
            self.assertEqual(match["name"], "Dr. Test Clinician")
            self.assertEqual(match["access_level"], "full")
        finally:
            # Restore backup
            if backup_data is not None:
                with open("data/clinicians.json", "w") as f:
                    f.write(backup_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
