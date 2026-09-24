"""
AMRIT Digital Twin Engine
Simulates virtual patient physiological profiles and response to drug interventions over time.
"""
from typing import Dict, List, Tuple, Optional
import numpy as np

class DigitalTwin:
    """
    Virtual Physiological Patient Model (Digital Twin).
    Simulates clinical trajectories of blood markers in response to drugs and lifestyle changes.
    """

    def __init__(self, blood_profile: Dict[str, float], dna_profile: Dict[str, str], environment: Dict[str, any]):
        self.initial_blood = dict(blood_profile)
        self.dna_profile = dict(dna_profile)
        self.environment = dict(environment)

    def simulate_clinical_trial(self, drug_name: str, dose: float, days: int) -> Dict[str, any]:
        """
        Simulate drug treatment and lifestyle changes day-by-day.
        Returns a time-series trajectory of clinical markers and side-effect risks.
        """
        drug = drug_name.lower()
        
        # Extract initial values or set defaults
        glucose = self.initial_blood.get("glucose_fasting", 100.0)
        hba1c = self.initial_blood.get("hba1c", 5.5)
        cholesterol = self.initial_blood.get("total_cholesterol", 200.0)
        ldl = self.initial_blood.get("ldl_cholesterol", 120.0)
        creatinine = self.initial_blood.get("creatinine", 0.9)
        alt = self.initial_blood.get("alt", 25.0)

        # Environment factors
        diet = self.environment.get("diet", "balanced").lower()
        exercise = self.environment.get("exercise", "moderate").lower()

        # Pharmacogenomics modifiers
        slco1b1 = self.dna_profile.get("SLCO1B1", "normal").lower()
        cyp2c19 = self.dna_profile.get("CYP2C19", "normal").lower()

        trajectory = []
        side_effect_prob = 0.0

        for day in range(1, days + 1):
            # 1. Base metabolism drifts & environmental influences
            if diet == "high-carb":
                glucose += 0.05
                hba1c += 0.001
            elif diet == "keto" or diet == "low-carb":
                glucose -= 0.08
                hba1c -= 0.002
                
            if exercise == "low":
                ldl += 0.03
                cholesterol += 0.05
            elif exercise == "high":
                ldl -= 0.05
                cholesterol -= 0.08
                glucose -= 0.03

            # 2. Drug Pharmacodynamics & Pharmacokinetics
            if "metformin" in drug:
                # Metformin lowers blood glucose and HbA1c
                efficacy = 0.15 + (dose / 1000.0) * 0.2
                glucose -= efficacy
                hba1c -= efficacy * 0.015
                # Side effect: GI distress
                side_effect_prob = min(0.3, side_effect_prob + 0.005)
            
            elif "statin" in drug or "atorvastatin" in drug or "simvastatin" in drug:
                # Statins lower LDL and total cholesterol
                efficacy = 0.8 + (dose / 40.0) * 0.5
                ldl -= efficacy
                cholesterol -= efficacy * 1.2
                
                # Side effect: Statin-induced myopathy (muscle pain) modulated by SLCO1B1 variant
                # SLCO1B1 poor metabolizer leads to high systemic concentration of statins
                multiplier = 1.0
                if "poor" in slco1b1 or "xx" in slco1b1:
                    multiplier = 4.0
                elif "intermediate" in slco1b1:
                    multiplier = 2.0
                
                # Probability of myopathy grows with dose, duration and SLCO1B1 risk multiplier
                myopathy_risk = (dose / 80.0) * (day / 90.0) * 0.05 * multiplier
                side_effect_prob = min(0.95, side_effect_prob + myopathy_risk)
                
                # Check liver enzymes (ALT increase with statins)
                if dose > 40:
                    alt += 0.15 * multiplier

            elif "clopidogrel" in drug:
                # Anti-platelet efficacy reduced if CYP2C19 poor metabolizer
                platelet_inhibition = 0.4
                if "poor" in cyp2c19:
                    platelet_inhibition = 0.1
                elif "intermediate" in cyp2c19:
                    platelet_inhibition = 0.25
                
                # Clopidogrel doesn't directly affect standard blood lipids/glucose, but we track efficacy
                side_effect_prob = min(0.15, side_effect_prob + 0.002) # Bleeding risk

            # Clamp physiological limits
            glucose = max(55.0, min(350.0, glucose))
            hba1c = max(4.0, min(14.0, hba1c))
            ldl = max(30.0, min(300.0, ldl))
            cholesterol = max(80.0, min(450.0, cholesterol))
            alt = max(5.0, min(300.0, alt))

            trajectory.append({
                "day": day,
                "glucose_fasting": round(glucose, 2),
                "hba1c": round(hba1c, 3),
                "total_cholesterol": round(cholesterol, 2),
                "ldl_cholesterol": round(ldl, 2),
                "alt": round(alt, 2),
                "side_effect_probability": round(side_effect_prob, 4)
            })

        # Calculate final verdict
        final = trajectory[-1]
        improvement_score = 0.0
        
        # Calculate reduction in risk markers
        gl_diff = self.initial_blood.get("glucose_fasting", 100.0) - final["glucose_fasting"]
        chol_diff = self.initial_blood.get("total_cholesterol", 200.0) - final["total_cholesterol"]
        
        if gl_diff > 0:
            improvement_score += gl_diff * 0.4
        if chol_diff > 0:
            improvement_score += chol_diff * 0.3
            
        verdict = "STABLE"
        if improvement_score > 15.0 and final["side_effect_probability"] < 0.3:
            verdict = "OPTIMAL_RESPONSE"
        elif final["side_effect_probability"] >= 0.5:
            verdict = "ADVERSE_RISK"
        elif improvement_score < 0:
            verdict = "DETERIORATING"

        return {
            "drug": drug_name,
            "dose": dose,
            "duration_days": days,
            "verdict": verdict,
            "improvement_score": round(improvement_score, 2),
            "final_metrics": final,
            "trajectory": trajectory
        }
