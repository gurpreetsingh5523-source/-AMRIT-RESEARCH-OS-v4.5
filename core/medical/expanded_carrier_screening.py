#!/usr/bin/env python3
"""
AMRIT Expanded Carrier Screening v5.0
60+ diseases, cost analysis, population-specific frequencies
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class DiseaseProfile:
    name: str
    gene: str
    inheritance: str  # AR, XLR, AD
    carrier_frequency_general: float
    carrier_frequency_south_asian: float
    severity: str  # mild, moderate, severe, profound
    treatable: bool
    newborn_screenable: bool
    test_cost_usd: float
    test_method: str

class ExpandedCarrierScreening:
    """
    Expanded Carrier Screening for 60+ diseases
    Focus on South Asian populations
    """

    DISEASES = [
        # Hemoglobinopathies (High in South Asians)
        DiseaseProfile("Alpha Thalassemia", "HBA1/HBA2", "AR", 0.03, 0.08, "severe", True, True, 150, "MLPA/Sequencing"),
        DiseaseProfile("Beta Thalassemia", "HBB", "AR", 0.04, 0.10, "severe", True, True, 150, "PCR/Sequencing"),
        DiseaseProfile("Sickle Cell Disease", "HBB", "AR", 0.02, 0.03, "severe", True, True, 150, "PCR/Sequencing"),
        DiseaseProfile("HbE Disease", "HBB", "AR", 0.01, 0.05, "moderate", True, True, 150, "PCR/Sequencing"),

        # Lysosomal Storage Disorders
        DiseaseProfile("Gaucher Disease", "GBA", "AR", 0.008, 0.02, "moderate", True, False, 300, "Sequencing"),
        DiseaseProfile("Tay-Sachs Disease", "HEXA", "AR", 0.003, 0.01, "severe", False, True, 300, "Sequencing"),
        DiseaseProfile("Niemann-Pick Type A", "SMPD1", "AR", 0.001, 0.003, "severe", False, True, 300, "Sequencing"),
        DiseaseProfile("Fabry Disease", "GLA", "XLR", 0.001, 0.002, "moderate", True, False, 300, "Sequencing"),
        DiseaseProfile("Pompe Disease", "GAA", "AR", 0.002, 0.005, "severe", True, True, 300, "Sequencing"),

        # Amino Acid Disorders
        DiseaseProfile("Phenylketonuria (PKU)", "PAH", "AR", 0.01, 0.02, "severe", True, True, 200, "Sequencing"),
        DiseaseProfile("Maple Syrup Urine Disease", "BCKDHA/BCKDHB/DBT", "AR", 0.001, 0.003, "severe", True, True, 350, "Sequencing"),
        DiseaseProfile("Homocystinuria", "CBS", "AR", 0.002, 0.005, "severe", True, True, 250, "Sequencing"),
        DiseaseProfile("Tyrosinemia Type I", "FAH", "AR", 0.001, 0.002, "severe", True, True, 250, "Sequencing"),

        # Organic Acid Disorders
        DiseaseProfile("Methylmalonic Acidemia", "MUT/MMACHC", "AR", 0.001, 0.002, "severe", True, True, 300, "Sequencing"),
        DiseaseProfile("Propionic Acidemia", "PCCA/PCCB", "AR", 0.001, 0.002, "severe", True, True, 300, "Sequencing"),
        DiseaseProfile("Isovaleric Acidemia", "IVD", "AR", 0.0005, 0.001, "severe", True, True, 250, "Sequencing"),

        # Fatty Acid Oxidation Disorders
        DiseaseProfile("MCAD Deficiency", "ACADM", "AR", 0.005, 0.01, "severe", True, True, 250, "Sequencing"),
        DiseaseProfile("VLCAD Deficiency", "ACADVL", "AR", 0.001, 0.002, "severe", True, True, 250, "Sequencing"),
        DiseaseProfile("LCHAD Deficiency", "HADHA", "AR", 0.001, 0.002, "severe", True, True, 250, "Sequencing"),

        # Urea Cycle Disorders
        DiseaseProfile("OTC Deficiency", "OTC", "XLR", 0.001, 0.002, "severe", True, False, 250, "Sequencing"),
        DiseaseProfile("CPS1 Deficiency", "CPS1", "AR", 0.0005, 0.001, "severe", True, False, 250, "Sequencing"),
        DiseaseProfile("ASS1 Deficiency", "ASS1", "AR", 0.001, 0.002, "severe", True, False, 250, "Sequencing"),

        # Carbohydrate Disorders
        DiseaseProfile("Galactosemia", "GALT", "AR", 0.003, 0.005, "severe", True, True, 200, "Sequencing"),
        DiseaseProfile("G6PD Deficiency", "G6PD", "XLR", 0.05, 0.10, "mild", True, False, 150, "PCR/Sequencing"),
        DiseaseProfile("Glycogen Storage Disease I", "G6PC", "AR", 0.001, 0.002, "severe", True, False, 250, "Sequencing"),
        DiseaseProfile("Glycogen Storage Disease II", "GAA", "AR", 0.002, 0.005, "severe", True, True, 250, "Sequencing"),

        # Peroxisomal Disorders
        DiseaseProfile("X-ALD", "ABCD1", "XLR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Zellweger Syndrome", "PEX1", "AR", 0.0005, 0.001, "profound", False, True, 350, "Sequencing"),

        # Mitochondrial Disorders
        DiseaseProfile("Leigh Syndrome", "SURF1/NDUFS4", "AR", 0.001, 0.002, "severe", False, False, 400, "Sequencing"),
        DiseaseProfile("MELAS", "MT-TL1", "Mitochondrial", 0.001, 0.002, "severe", False, False, 400, "Sequencing"),
        DiseaseProfile("MERRF", "MT-TK", "Mitochondrial", 0.0005, 0.001, "severe", False, False, 400, "Sequencing"),

        # Immunodeficiencies
        DiseaseProfile("Severe Combined Immunodeficiency", "IL2RG/ADA", "XLR/AR", 0.0005, 0.001, "profound", True, True, 350, "Sequencing"),
        DiseaseProfile("Wiskott-Aldrich Syndrome", "WAS", "XLR", 0.0005, 0.001, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Chronic Granulomatous Disease", "CYBB/CYBA", "XLR/AR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),

        # Hemophilias
        DiseaseProfile("Hemophilia A", "F8", "XLR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Hemophilia B", "F9", "XLR", 0.0005, 0.001, "severe", True, False, 300, "Sequencing"),

        # Neuromuscular Disorders
        DiseaseProfile("Spinal Muscular Atrophy", "SMN1", "AR", 0.01, 0.02, "severe", True, True, 250, "MLPA/Sequencing"),
        DiseaseProfile("Duchenne Muscular Dystrophy", "DMD", "XLR", 0.005, 0.01, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Becker Muscular Dystrophy", "DMD", "XLR", 0.003, 0.005, "moderate", True, False, 300, "Sequencing"),
        DiseaseProfile("Myotonic Dystrophy", "DMPK", "AD", 0.005, 0.01, "moderate", False, False, 250, "PCR"),

        # Neurodegenerative Disorders
        DiseaseProfile("Huntington Disease", "HTT", "AD", 0.005, 0.01, "severe", False, False, 250, "PCR"),
        DiseaseProfile("Fragile X Syndrome", "FMR1", "XLR", 0.005, 0.01, "moderate", False, True, 200, "PCR"),
        DiseaseProfile("Spinocerebellar Ataxia", "ATXN1", "AD", 0.002, 0.005, "moderate", False, False, 250, "PCR"),

        # Cancer Predisposition
        DiseaseProfile("BRCA1 Hereditary Breast/Ovarian Cancer", "BRCA1", "AD", 0.005, 0.01, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("BRCA2 Hereditary Breast/Ovarian Cancer", "BRCA2", "AD", 0.005, 0.01, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Lynch Syndrome", "MLH1/MSH2/MSH6/PMS2", "AD", 0.002, 0.005, "severe", True, False, 400, "Sequencing"),
        DiseaseProfile("Familial Adenomatous Polyposis", "APC", "AD", 0.001, 0.002, "severe", True, False, 250, "Sequencing"),
        DiseaseProfile("Li-Fraumeni Syndrome", "TP53", "AD", 0.0005, 0.001, "severe", False, False, 250, "Sequencing"),

        # Cardiac Disorders
        DiseaseProfile("Hypertrophic Cardiomyopathy", "MYBPC3/MYH7", "AD", 0.005, 0.01, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Long QT Syndrome", "KCNQ1/KCNH2/SCN5A", "AD", 0.002, 0.005, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Brugada Syndrome", "SCN5A", "AD", 0.001, 0.002, "severe", True, False, 250, "Sequencing"),
        DiseaseProfile("Arrhythmogenic Cardiomyopathy", "PKP2/DSP", "AD", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),

        # Cystic Fibrosis
        DiseaseProfile("Cystic Fibrosis", "CFTR", "AR", 0.025, 0.04, "severe", True, True, 200, "Sequencing"),

        # Deafness
        DiseaseProfile("Connexin 26 Deafness", "GJB2", "AR", 0.01, 0.02, "moderate", False, True, 150, "Sequencing"),
        DiseaseProfile("Pendred Syndrome", "SLC26A4", "AR", 0.002, 0.005, "moderate", False, True, 200, "Sequencing"),

        # Eye Disorders
        DiseaseProfile("Retinitis Pigmentosa", "RHO/RPGR", "AD/XLR", 0.002, 0.005, "severe", False, False, 300, "Sequencing"),
        DiseaseProfile("Leber Congenital Amaurosis", "RPE65/CEP290", "AR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Stargardt Disease", "ABCA4", "AR", 0.003, 0.005, "severe", False, False, 250, "Sequencing"),

        # Kidney Disorders
        DiseaseProfile("Polycystic Kidney Disease (ADPKD)", "PKD1/PKD2", "AD", 0.005, 0.01, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Alport Syndrome", "COL4A5/COL4A3/COL4A4", "XLR/AR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),

        # Skin Disorders
        DiseaseProfile("Epidermolysis Bullosa", "KRT5/KRT14/COL7A1", "AD/AR", 0.001, 0.002, "severe", True, False, 300, "Sequencing"),
        DiseaseProfile("Oculocutaneous Albinism", "OCA2/TYR", "AR", 0.005, 0.01, "mild", False, True, 200, "Sequencing"),
    ]

    def __init__(self, population: str = "South Asian"):
        self.population = population
        self.selected_diseases = []

    def get_panel(self, 
                  population_focus: bool = True,
                  severity_filter: List[str] = None,
                  treatable_only: bool = False,
                  max_cost: float = None) -> Dict:
        """Generate customized screening panel"""

        severity_filter = severity_filter or ["severe", "profound"]
        panel = []

        for disease in self.DISEASES:
            # Apply filters
            if population_focus and self.population == "South Asian":
                if disease.carrier_frequency_south_asian < 0.001:
                    continue

            if severity_filter and disease.severity not in severity_filter:
                continue

            if treatable_only and not disease.treatable:
                continue

            if max_cost and disease.test_cost_usd > max_cost:
                continue

            panel.append(disease)

        # Calculate costs
        total_cost = sum(d.test_cost_usd for d in panel)

        # Group by category
        categories = {}
        for disease in panel:
            category = self._categorize_disease(disease)
            if category not in categories:
                categories[category] = []
            categories[category].append(disease)

        return {
            "panel_name": f"AMRIT Expanded Carrier Panel - {self.population}",
            "total_diseases": len(panel),
            "total_cost_usd": total_cost,
            "categories": {cat: len(diseases) for cat, diseases in categories.items()},
            "diseases": panel,
            "high_priority": [d for d in panel if d.severity in ["severe", "profound"]],
            "treatable": [d for d in panel if d.treatable],
            "newborn_screenable": [d for d in panel if d.newborn_screenable]
        }

    def _categorize_disease(self, disease: DiseaseProfile) -> str:
        """Categorize disease by system"""

        name = disease.name.lower()

        if any(x in name for x in ["thalassemia", "sickle", "hemophilia", "g6pd"]):
            return "Hematologic"
        elif any(x in name for x in ["gaucher", "tay-sachs", "niemann-pick", "fabry", "pompe"]):
            return "Lysosomal Storage"
        elif any(x in name for x in ["phenylketonuria", "maple syrup", "homocystinuria", "galactosemia"]):
            return "Metabolic"
        elif any(x in name for x in ["muscular", "dystrophy", "atrophy", "myotonic"]):
            return "Neuromuscular"
        elif any(x in name for x in ["brca", "lynch", "polyposis", "li-fraumeni"]):
            return "Cancer Predisposition"
        elif any(x in name for x in ["cardiomyopathy", "qt syndrome", "brugada", "arrhythmogenic"]):
            return "Cardiac"
        elif any(x in name for x in ["kidney", "polycystic", "alport"]):
            return "Renal"
        elif any(x in name for x in ["deafness", "pendred", "albinism", "epidermolysis"]):
            return "Sensory/Skin"
        elif any(x in name for x in ["immunodeficiency", "wiskott-aldrich", "granulomatous"]):
            return "Immunologic"
        else:
            return "Other"

    def calculate_couple_risk(self, 
                            partner1_results: Dict[str, str],
                            partner2_results: Dict[str, str]) -> Dict:
        """Calculate risk for offspring given both parents' carrier status"""

        risks = []

        for disease in self.DISEASES:
            gene = disease.gene

            p1_status = partner1_results.get(gene, "negative")
            p2_status = partner2_results.get(gene, "negative")

            if disease.inheritance == "AR":
                # Both carriers = 25% affected risk
                if p1_status == "carrier" and p2_status == "carrier":
                    risk = 0.25
                elif p1_status == "carrier" or p2_status == "carrier":
                    risk = 0.0  # 50% carrier, 0% affected
                else:
                    risk = 0.0

            elif disease.inheritance == "XLR":
                # Mother carrier = 50% sons affected
                if p1_status == "carrier":  # Assuming partner1 is mother
                    risk = 0.25  # 50% chance son, 50% chance affected
                else:
                    risk = 0.0

            elif disease.inheritance == "AD":
                # One affected parent = 50% risk
                if p1_status == "affected" or p2_status == "affected":
                    risk = 0.5
                else:
                    risk = 0.0

            else:
                risk = 0.0

            if risk > 0:
                risks.append({
                    "disease": disease.name,
                    "gene": gene,
                    "inheritance": disease.inheritance,
                    "risk_percentage": risk * 100,
                    "risk_level": "HIGH" if risk >= 0.25 else "MODERATE",
                    "severity": disease.severity,
                    "recommendation": f"{disease.name}: {risk*100}% risk for affected child"
                })

        return {
            "total_risks_identified": len(risks),
            "high_risk": [r for r in risks if r["risk_level"] == "HIGH"],
            "moderate_risk": [r for r in risks if r["risk_level"] == "MODERATE"],
            "all_risks": risks,
            "recommendations": self._generate_couple_recommendations(risks)
        }

    def _generate_couple_recommendations(self, risks: List[Dict]) -> List[str]:
        """Generate recommendations for at-risk couples"""

        recommendations = []

        if not risks:
            recommendations.append("No increased genetic risks identified for this couple.")
            recommendations.append("Standard prenatal care recommended.")
            return recommendations

        high_risk = [r for r in risks if r["risk_level"] == "HIGH"]

        if high_risk:
            recommendations.append(f"URGENT: {len(high_risk)} high-risk conditions identified.")
            recommendations.append("Refer to genetic counselor immediately.")
            recommendations.append("Consider preimplantation genetic testing (PGT) if planning pregnancy.")
            recommendations.append("Consider prenatal diagnosis (CVS/amniocentesis) if already pregnant.")

        recommendations.append("Provide genetic counseling for all identified risks.")
        recommendations.append("Discuss reproductive options including:")
        recommendations.append("  - Preimplantation genetic testing (PGT-M)")
        recommendations.append("  - Prenatal diagnosis")
        recommendations.append("  - Donor gametes")
        recommendations.append("  - Adoption")
        recommendations.append("Ensure informed consent for all decisions.")
        recommendations.append("Provide psychological support throughout process.")

        return recommendations

if __name__ == "__main__":
    ecs = ExpandedCarrierScreening(population="South Asian")

    # Get standard panel
    panel = ecs.get_panel(
        population_focus=True,
        severity_filter=["severe", "profound", "moderate"],
        treatable_only=False
    )

    print(f"Panel: {panel['panel_name']}")
    print(f"Total diseases: {panel['total_diseases']}")
    print(f"Total cost: ${panel['total_cost_usd']}")
    print(f"Categories: {panel['categories']}")
    print(f"High priority: {len(panel['high_priority'])}")
    print(f"Treatable: {len(panel['treatable'])}")

    # Calculate couple risk
    partner1 = {"HBB": "carrier", "CFTR": "negative", "SMN1": "carrier"}
    partner2 = {"HBB": "carrier", "CFTR": "carrier", "SMN1": "negative"}

    risk = ecs.calculate_couple_risk(partner1, partner2)
    print(f"Couple Risk Analysis:")
    print(f"Total risks: {risk['total_risks_identified']}")
    for r in risk['all_risks']:
        print(f"  {r['disease']}: {r['risk_percentage']}% risk")
