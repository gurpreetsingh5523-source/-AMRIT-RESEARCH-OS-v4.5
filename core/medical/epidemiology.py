import os
from typing import Dict, List, Optional
from core.medical.patient_intake import PatientIntake

class EpidemiologyEngine:
    """
    Analyzes aggregated patient profiles to calculate sickness ratios,
    identify population-level health risks, and formulate regional preventive plans.
    """

    def __init__(self, intake_manager: Optional[PatientIntake] = None):
        self.intake = intake_manager or PatientIntake()

    def get_summary(self) -> Dict:
        """
        Processes registered patient profiles to compute statistics.
        """
        patients = self.intake.list_all_patients()
        total = len(patients)

        if total == 0:
            return {
                "total_patients": 0,
                "sickness_rates": {
                    "diabetes": 0.0,
                    "hypertension": 0.0,
                    "hyperlipidemia": 0.0
                },
                "most_prevalent_disease": "None",
                "population_health_plan": "No patient data available to generate a population health plan."
            }

        diabetes_cnt = 0
        hypertension_cnt = 0
        lipid_cnt = 0

        for p in patients:
            # Check diabetes
            blood = p.get("blood", {})
            glucose = blood.get("glucose_fasting") or blood.get("glucose") or 0.0
            hba1c = blood.get("hba1c") or 0.0
            
            # BP
            bp_str = p.get("bp", "Not provided")
            systolic = 0
            diastolic = 0
            if "/" in bp_str:
                try:
                    parts = bp_str.split("/")
                    systolic = int(parts[0].strip())
                    diastolic = int(parts[1].strip())
                except ValueError:
                    pass

            # LDL
            ldl = blood.get("ldl_cholesterol") or blood.get("ldl") or 0.0

            # Counters
            if glucose > 126.0 or hba1c > 6.5:
                diabetes_cnt += 1
            if systolic >= 130 or diastolic >= 80:
                hypertension_cnt += 1
            if ldl > 130.0:
                lipid_cnt += 1

        # Rates
        diabetes_rate = (diabetes_cnt / total) * 100.0
        hypertension_rate = (hypertension_cnt / total) * 100.0
        lipid_rate = (lipid_cnt / total) * 100.0

        # Find most prevalent
        rates = {
            "type_2_diabetes": diabetes_rate,
            "hypertension": hypertension_rate,
            "hyperlipidemia": lipid_rate
        }
        most_prevalent = max(rates, key=rates.get)
        max_rate = rates[most_prevalent]

        # Formulate health plan
        plan = f"Population Health Plan based on {total} registered patients:\n"
        if max_rate == 0.0:
            plan += "All evaluated sickness metrics are within normal ranges. Recommend general diet and physical activity monitoring."
            most_prevalent = "None"
        elif most_prevalent == "type_2_diabetes":
            plan += "Priority Level: High. Prevalent condition is Type 2 Diabetes ({}% of population). Actions: Recommend regional low-glycemic dietary interventions, community glucose screening, and folate supplement recommendations.".format(round(diabetes_rate, 1))
        elif most_prevalent == "hypertension":
            plan += "Priority Level: High. Prevalent condition is Hypertension ({}% of population). Actions: Implement local blood pressure checks, advocate for low-sodium salt alternatives, and coordinate active lifestyle classes.".format(round(hypertension_rate, 1))
        elif most_prevalent == "hyperlipidemia":
            plan += "Priority Level: Moderate. Prevalent condition is Hyperlipidemia ({}% of population). Actions: Promote Mediterranean cardioprotective dietary habits, active statin screening, and regular lipid panel checks.".format(round(lipid_rate, 1))

        return {
            "total_patients": total,
            "sickness_rates": {
                "diabetes_pct": round(diabetes_rate, 1),
                "hypertension_pct": round(hypertension_rate, 1),
                "hyperlipidemia_pct": round(lipid_rate, 1)
            },
            "most_prevalent_disease": most_prevalent,
            "population_health_plan": plan
        }

    def trigger_epidemiological_research(self) -> Dict:
        """
        Finds the most prevalent disease marker in the population and triggers
        an autonomous literature mining research run using the UnifiedAgent.
        """
        summary = self.get_summary()
        disease = summary["most_prevalent_disease"]

        if disease == "None":
            return {
                "status": "skipped",
                "message": "No prevalent population disease found to initiate research."
            }

        # Format disease name for medical literature search
        search_topic = disease.replace("_", " ")

        from core.autonomous.unified_agent import UnifiedAgent
        ua = UnifiedAgent()
        
        # Trigger autonomous research loop
        # Run research synchronously/asynchronously. Since this is locally run, we will trigger it
        # and write the preliminary hypothesis outcome.
        research_status = ua.run_autonomous_research(search_topic, duration_hours=1)

        return {
            "status": "triggered",
            "disease_target": search_topic,
            "research_outcome": research_status
        }
