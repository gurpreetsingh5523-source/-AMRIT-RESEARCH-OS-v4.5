#!/usr/bin/env python3
"""
AMRIT Drug Predictor v5.0
13 biomarkers, 10 drug predictions (pharmacogenomics)
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class DrugResponse(Enum):
    NORMAL = "normal"
    SLOW = "slow"
    FAST = "fast"
    ULTRAFAST = "ultrafast"
    POOR = "poor"
    INTERMEDIATE = "intermediate"
    EXTENSIVE = "extensive"
    ULTRARAPID = "ultrarapid"

@dataclass
class DrugPrediction:
    drug_name: str
    gene: str
    predicted_response: DrugResponse
    recommended_dose: str
    alternative_drugs: List[str]
    warning: str
    confidence: float

class DrugPredictor:
    """Pharmacogenomics-based drug prediction"""

    # 13 key pharmacogenomic biomarkers
    BIOMARKERS = {
        "CYP2D6": {
            "drugs": ["codeine", "tramadol", "amitriptyline", "nortriptyline", 
                     "paroxetine", "fluoxetine", "risperidone", "tamoxifen"],
            "phenotypes": {
                "*1/*1": DrugResponse.EXTENSIVE,
                "*1/*2": DrugResponse.EXTENSIVE,
                "*1/*10": DrugResponse.INTERMEDIATE,
                "*10/*10": DrugResponse.POOR,
                "*4/*4": DrugResponse.POOR,
                "*1/*5": DrugResponse.INTERMEDIATE,
                "*5/*5": DrugResponse.POOR
            }
        },
        "CYP2C19": {
            "drugs": ["clopidogrel", "omeprazole", "pantoprazole", "diazepam",
                     "phenytoin", "proguanil", "voriconazole"],
            "phenotypes": {
                "*1/*1": DrugResponse.EXTENSIVE,
                "*1/*2": DrugResponse.INTERMEDIATE,
                "*2/*2": DrugResponse.POOR,
                "*1/*17": DrugResponse.ULTRARAPID,
                "*17/*17": DrugResponse.ULTRARAPID
            }
        },
        "CYP2C9": {
            "drugs": ["warfarin", "phenytoin", "losartan", "celecoxib",
                     "ibuprofen", "sulfonylureas"],
            "phenotypes": {
                "*1/*1": DrugResponse.NORMAL,
                "*1/*2": DrugResponse.INTERMEDIATE,
                "*2/*2": DrugResponse.POOR,
                "*1/*3": DrugResponse.INTERMEDIATE,
                "*3/*3": DrugResponse.POOR
            }
        },
        "CYP3A4": {
            "drugs": ["atorvastatin", "simvastatin", "tacrolimus", "cyclosporine",
                     "midazolam", "fentanyl", "erythromycin"],
            "phenotypes": {
                "*1/*1": DrugResponse.NORMAL,
                "*1/*22": DrugResponse.SLOW,
                "*22/*22": DrugResponse.SLOW
            }
        },
        "SLCO1B1": {
            "drugs": ["atorvastatin", "simvastatin", "pravastatin", "rosuvastatin"],
            "phenotypes": {
                "*1A/*1A": DrugResponse.NORMAL,
                "*1A/*5": DrugResponse.INTERMEDIATE,
                "*5/*5": DrugResponse.POOR
            }
        },
        "VKORC1": {
            "drugs": ["warfarin"],
            "phenotypes": {
                "GG": DrugResponse.NORMAL,
                "GA": DrugResponse.INTERMEDIATE,
                "AA": DrugResponse.POOR
            }
        },
        "TPMT": {
            "drugs": ["azathioprine", "6-mercaptopurine", "thioguanine"],
            "phenotypes": {
                "*1/*1": DrugResponse.NORMAL,
                "*1/*2": DrugResponse.INTERMEDIATE,
                "*2/*2": DrugResponse.POOR,
                "*1/*3A": DrugResponse.INTERMEDIATE,
                "*3A/*3A": DrugResponse.POOR
            }
        },
        "DPYD": {
            "drugs": ["5-fluorouracil", "capecitabine", "tegafur"],
            "phenotypes": {
                "*1/*1": DrugResponse.NORMAL,
                "*1/*2A": DrugResponse.INTERMEDIATE,
                "*2A/*2A": DrugResponse.POOR
            }
        },
        "UGT1A1": {
            "drugs": ["irinotecan", "atazanavir", "nilotinib"],
            "phenotypes": {
                "*1/*1": DrugResponse.NORMAL,
                "*1/*28": DrugResponse.INTERMEDIATE,
                "*28/*28": DrugResponse.POOR
            }
        },
        "HLA-B*57:01": {
            "drugs": ["abacavir"],
            "phenotypes": {
                "negative": DrugResponse.NORMAL,
                "positive": DrugResponse.POOR  # Hypersensitivity
            }
        },
        "HLA-B*15:02": {
            "drugs": ["carbamazepine"],
            "phenotypes": {
                "negative": DrugResponse.NORMAL,
                "positive": DrugResponse.POOR  # SJS/TEN risk
            }
        },
        "G6PD": {
            "drugs": ["primaquine", "dapsone", "nitrofurantoin", "sulfonamides"],
            "phenotypes": {
                "normal": DrugResponse.NORMAL,
                "deficient": DrugResponse.POOR
            }
        },
        "NAT2": {
            "drugs": ["isoniazid", "sulfamethazine", "procainamide", "hydralazine"],
            "phenotypes": {
                "*4/*4": DrugResponse.FAST,
                "*4/*5": DrugResponse.INTERMEDIATE,
                "*5/*5": DrugResponse.SLOW
            }
        }
    }

    def __init__(self, patient_genotype: Dict[str, str] = None):
        self.patient_genotype = patient_genotype or {}
        self.predictions = []

    def predict_drug_response(self, drug_name: str) -> List[DrugPrediction]:
        """Predict response for a specific drug"""

        predictions = []

        for gene, data in self.BIOMARKERS.items():
            if drug_name.lower() in [d.lower() for d in data["drugs"]]:
                genotype = self.patient_genotype.get(gene, "*1/*1")
                phenotype = data["phenotypes"].get(genotype, DrugResponse.NORMAL)

                # Generate recommendation
                recommendation = self._generate_recommendation(
                    drug_name, gene, phenotype, genotype
                )

                predictions.append(recommendation)

        return predictions

    def _generate_recommendation(self, drug: str, gene: str,
                                  phenotype: DrugResponse, genotype: str) -> DrugPrediction:
        """Generate drug recommendation based on phenotype"""

        warnings = {
            DrugResponse.POOR: f"POOR METABOLIZER: High risk of toxicity or lack of efficacy. Consider alternative.",
            DrugResponse.INTERMEDIATE: f"INTERMEDIATE METABOLIZER: May require dose adjustment. Monitor closely.",
            DrugResponse.ULTRARAPID: f"ULTRARAPID METABOLIZER: May require higher dose or alternative. Monitor for efficacy.",
            DrugResponse.SLOW: f"SLOW METABOLIZER: Risk of accumulation. Consider dose reduction.",
            DrugResponse.NORMAL: f"NORMAL METABOLIZER: Standard dosing appropriate.",
            DrugResponse.EXTENSIVE: f"EXTENSIVE METABOLIZER: Standard dosing appropriate.",
            DrugResponse.FAST: f"FAST METABOLIZER: Standard dosing appropriate.",
        }

        dose_adjustments = {
            DrugResponse.POOR: "Consider 25-50% dose reduction or alternative drug",
            DrugResponse.INTERMEDIATE: "Consider 75% standard dose or standard with monitoring",
            DrugResponse.ULTRARAPID: "May need 150% standard dose or alternative",
            DrugResponse.SLOW: "Consider 50% dose reduction",
            DrugResponse.NORMAL: "Standard dose",
            DrugResponse.EXTENSIVE: "Standard dose",
            DrugResponse.FAST: "Standard dose",
        }

        alternatives = self._get_alternatives(drug, gene)

        return DrugPrediction(
            drug_name=drug,
            gene=gene,
            predicted_response=phenotype,
            recommended_dose=dose_adjustments[phenotype],
            alternative_drugs=alternatives,
            warning=warnings[phenotype],
            confidence=0.85 if genotype in self.BIOMARKERS[gene]["phenotypes"] else 0.60
        )

    def _get_alternatives(self, drug: str, gene: str) -> List[str]:
        """Get alternative drugs not affected by same gene"""

        alternatives = {
            "warfarin": ["apixaban", "rivaroxaban", "dabigatran"],
            "codeine": ["morphine", "oxycodone", "tramadol (if CYP2D6 normal)"],
            "clopidogrel": ["prasugrel", "ticagrelor"],
            "carbamazepine": ["lamotrigine", "levetiracetam", "oxcarbazepine"],
            "azathioprine": ["mycophenolate", "tacrolimus"],
            "atorvastatin": ["rosuvastatin", "pravastatin"],
            "abacavir": ["tenofovir", "zidovudine"],
            "irinotecan": ["oxaliplatin", "5-FU (if DPYD normal)"]
        }

        return alternatives.get(drug.lower(), ["Consult pharmacist for alternatives"])

    def full_pharmacogenomic_profile(self) -> Dict:
        """Generate complete pharmacogenomic profile"""

        profile = {
            "patient_genotype": self.patient_genotype,
            "analyzed_genes": len(self.BIOMARKERS),
            "drug_predictions": [],
            "high_risk_alerts": [],
            "recommendations": []
        }

        for gene, data in self.BIOMARKERS.items():
            genotype = self.patient_genotype.get(gene, "*1/*1")
            phenotype = data["phenotypes"].get(genotype, DrugResponse.NORMAL)

            for drug in data["drugs"]:
                prediction = self._generate_recommendation(drug, gene, phenotype, genotype)
                profile["drug_predictions"].append(prediction)

                if phenotype in [DrugResponse.POOR, DrugResponse.ULTRARAPID]:
                    profile["high_risk_alerts"].append({
                        "drug": drug,
                        "gene": gene,
                        "phenotype": phenotype.value,
                        "warning": prediction.warning
                    })

        # Generate summary recommendations
        if profile["high_risk_alerts"]:
            profile["recommendations"].append(
                f"URGENT: {len(profile['high_risk_alerts'])} high-risk drug-gene interactions found. "
                "Consult clinical pharmacologist before prescribing."
            )

        profile["recommendations"].append(
            "Always verify genotype with clinical laboratory before dose adjustment."
        )

        profile["recommendations"].append(
            "Consider pharmacogenomic testing panel for all 13 biomarkers."
        )

        return profile

if __name__ == "__main__":
    # Example patient genotype
    patient = {
        "CYP2D6": "*10/*10",
        "CYP2C19": "*2/*2",
        "CYP2C9": "*1/*2",
        "VKORC1": "AA",
        "TPMT": "*1/*2",
        "HLA-B*57:01": "negative"
    }

    predictor = DrugPredictor(patient)

    # Predict warfarin response
    warfarin_pred = predictor.predict_drug_response("warfarin")
    print("Warfarin Predictions:")
    for pred in warfarin_pred:
        print(f"  Gene: {pred.gene}")
        print(f"  Phenotype: {pred.predicted_response.value}")
        print(f"  Dose: {pred.recommended_dose}")
        print(f"  Warning: {pred.warning}")
        print()

    # Full profile
    profile = predictor.full_pharmacogenomic_profile()
    print(f"Total predictions: {len(profile['drug_predictions'])}")
    print(f"High risk alerts: {len(profile['high_risk_alerts'])}")
