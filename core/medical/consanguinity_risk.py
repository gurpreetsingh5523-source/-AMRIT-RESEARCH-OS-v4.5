#!/usr/bin/env python3
"""
AMRIT Consanguinity Risk v5.0
20 diseases, 6 relationship types (South Asian focus)
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class RelationshipType(Enum):
    FIRST_COUSIN = "first_cousin"           # F = 0.0625
    DOUBLE_FIRST_COUSIN = "double_first_cousin"  # F = 0.125
    UNCLE_NIECE = "uncle_niece"             # F = 0.125
    AUNT_NEPHEW = "aunt_nephew"             # F = 0.125
    SECOND_COUSIN = "second_cousin"         # F = 0.0156
    FIRST_COUSIN_ONCE_REMOVED = "first_cousin_once_removed"  # F = 0.0313

@dataclass
class DiseaseRisk:
    disease: str
    carrier_frequency: float  # In general population
    risk_consanguineous: float  # Risk with consanguinity
    severity: str
    actionable: bool

class ConsanguinityRisk:
    """Consanguinity risk calculator for South Asian populations"""

    # Inbreeding coefficients
    F_VALUES = {
        RelationshipType.FIRST_COUSIN: 0.0625,
        RelationshipType.DOUBLE_FIRST_COUSIN: 0.125,
        RelationshipType.UNCLE_NIECE: 0.125,
        RelationshipType.AUNT_NEPHEW: 0.125,
        RelationshipType.SECOND_COUSIN: 0.0156,
        RelationshipType.FIRST_COUSIN_ONCE_REMOVED: 0.0313
    }

    DISEASES = [
        DiseaseRisk("Thalassemia (Alpha)", 0.03, 0.12, "severe", True),
        DiseaseRisk("Thalassemia (Beta)", 0.04, 0.16, "severe", True),
        DiseaseRisk("Sickle Cell Disease", 0.02, 0.08, "severe", True),
        DiseaseRisk("Cystic Fibrosis", 0.025, 0.10, "severe", True),
        DiseaseRisk("Spinal Muscular Atrophy", 0.01, 0.04, "severe", True),
        DiseaseRisk("Congenital Adrenal Hyperplasia", 0.005, 0.02, "moderate", True),
        DiseaseRisk("Gaucher Disease", 0.008, 0.032, "moderate", True),
        DiseaseRisk("Tay-Sachs Disease", 0.003, 0.012, "severe", True),
        DiseaseRisk("Familial Mediterranean Fever", 0.02, 0.08, "moderate", True),
        DiseaseRisk("Wilson Disease", 0.005, 0.02, "moderate", True),
        DiseaseRisk("Phenylketonuria (PKU)", 0.01, 0.04, "severe", True),
        DiseaseRisk("Galactosemia", 0.003, 0.012, "severe", True),
        DiseaseRisk("Homocystinuria", 0.002, 0.008, "severe", True),
        DiseaseRisk("Maple Syrup Urine Disease", 0.001, 0.004, "severe", True),
        DiseaseRisk("Glycogen Storage Disease", 0.002, 0.008, "moderate", True),
        DiseaseRisk("Mucopolysaccharidosis", 0.001, 0.004, "severe", True),
        DiseaseRisk("Niemann-Pick Disease", 0.001, 0.004, "severe", True),
        DiseaseRisk("Fanconi Anemia", 0.0005, 0.002, "severe", True),
        DiseaseRisk("Bloom Syndrome", 0.0003, 0.0012, "severe", True),
        DiseaseRisk("Ataxia Telangiectasia", 0.0005, 0.002, "severe", True)
    ]

    def __init__(self, population: str = "South Asian"):
        self.population = population
        self.risk_multiplier = 2.0 if "South Asian" in population else 1.5

    def calculate_risk(self, 
                      relationship: RelationshipType,
                      known_carriers: List[str] = None) -> Dict:
        """Calculate consanguinity risk"""

        f_value = self.F_VALUES[relationship]
        risks = []

        for disease in self.DISEASES:
            # Base risk calculation
            base_risk = disease.carrier_frequency * f_value * self.risk_multiplier

            # Adjust for known carriers
            if known_carriers and disease.disease in known_carriers:
                base_risk *= 4.0  # 4x if known carrier in family

            risks.append({
                "disease": disease.disease,
                "risk_percentage": round(base_risk * 100, 3),
                "severity": disease.severity,
                "actionable": disease.actionable,
                "recommended_test": f"Carrier screening for {disease.disease}"
            })

        # Sort by risk
        risks.sort(key=lambda x: x["risk_percentage"], reverse=True)

        return {
            "relationship": relationship.value,
            "inbreeding_coefficient": f_value,
            "population": self.population,
            "total_diseases_analyzed": len(self.DISEASES),
            "high_risk_diseases": [r for r in risks if r["risk_percentage"] > 1.0],
            "moderate_risk_diseases": [r for r in risks if 0.1 < r["risk_percentage"] <= 1.0],
            "all_risks": risks,
            "recommendations": self._generate_recommendations(relationship, risks)
        }

    def _generate_recommendations(self, 
                                relationship: RelationshipType,
                                risks: List[Dict]) -> List[str]:
        """Generate recommendations based on risk"""

        recommendations = []

        f_value = self.F_VALUES[relationship]

        if f_value >= 0.125:
            recommendations.append("HIGH RISK: Comprehensive genetic counseling strongly recommended")
            recommendations.append("Preconception carrier screening for all 20 diseases")
            recommendations.append("Consider preimplantation genetic testing (PGT)")
        elif f_value >= 0.0625:
            recommendations.append("MODERATE-HIGH RISK: Genetic counseling recommended")
            recommendations.append("Carrier screening for high-risk diseases (Thalassemia, SMA, CF)")
        elif f_value >= 0.0313:
            recommendations.append("MODERATE RISK: Consider carrier screening")
            recommendations.append("Focus on diseases common in your population")
        else:
            recommendations.append("LOW RISK: Standard prenatal care")
            recommendations.append("Population-based carrier screening as per guidelines")

        # Add specific recommendations
        high_risk = [r for r in risks if r["risk_percentage"] > 1.0]
        if high_risk:
            recommendations.append(f"Priority testing for: {', '.join([r['disease'] for r in high_risk[:3]])}")

        recommendations.append("Discuss results with genetic counselor")
        recommendations.append("Consider extended family screening if positive")

        return recommendations

if __name__ == "__main__":
    cr = ConsanguinityRisk(population="South Asian")

    # Calculate risk for first cousin marriage
    risk = cr.calculate_risk(
        RelationshipType.FIRST_COUSIN,
        known_carriers=["Thalassemia (Beta)"]
    )

    print(f"Relationship: {risk['relationship']}")
    print(f"Inbreeding Coefficient: {risk['inbreeding_coefficient']}")
    print(f"High Risk Diseases: {len(risk['high_risk_diseases'])}")
    print("\nTop 5 Risks:")
    for r in risk['all_risks'][:5]:
        print(f"  {r['disease']}: {r['risk_percentage']}%")

    print("\nRecommendations:")
    for rec in risk['recommendations']:
        print(f"  • {rec}")
