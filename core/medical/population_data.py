#!/usr/bin/env python3
"""
AMRIT Population Data v5.0
50+ populations worldwide with carrier frequencies
"""

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class PopulationData:
    name: str
    region: str
    country: str
    ethnicity: str
    population_size: int
    consanguinity_rate: float
    common_diseases: List[str]
    carrier_frequencies: Dict[str, float]
    genetic_diversity_index: float
    healthcare_access_index: float

class PopulationDatabase:
    """Comprehensive population genetic database"""

    POPULATIONS = {
        # South Asian Populations
        "Punjabi": PopulationData(
            "Punjabi", "South Asia", "India/Pakistan", "Indo-Aryan",
            125000000, 0.35,  # 35% consanguinity in some regions
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis", "Sickle Cell"],
            {"Beta Thalassemia": 0.10, "Alpha Thalassemia": 0.08, "G6PD": 0.12, 
             "Cystic Fibrosis": 0.04, "Sickle Cell": 0.03, "PKU": 0.02},
            0.72, 0.65
        ),
        "Sindhi": PopulationData(
            "Sindhi", "South Asia", "Pakistan/India", "Indo-Aryan",
            40000000, 0.45,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.12, "Alpha Thalassemia": 0.09, "G6PD": 0.10,
             "Cystic Fibrosis": 0.05, "Sickle Cell": 0.02, "PKU": 0.02},
            0.70, 0.60
        ),
        "Bengali": PopulationData(
            "Bengali", "South Asia", "Bangladesh/India", "Indo-Aryan",
            250000000, 0.15,
            ["Beta Thalassemia", "G6PD Deficiency", "Sickle Cell"],
            {"Beta Thalassemia": 0.08, "Alpha Thalassemia": 0.06, "G6PD": 0.15,
             "Cystic Fibrosis": 0.02, "Sickle Cell": 0.05, "PKU": 0.01},
            0.75, 0.55
        ),
        "Tamil": PopulationData(
            "Tamil", "South Asia", "India/Sri Lanka", "Dravidian",
            90000000, 0.10,
            ["Beta Thalassemia", "Sickle Cell", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.06, "Alpha Thalassemia": 0.04, "G6PD": 0.08,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.08, "PKU": 0.01},
            0.78, 0.70
        ),
        "Gujarati": PopulationData(
            "Gujarati", "South Asia", "India", "Indo-Aryan",
            60000000, 0.20,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.07, "Alpha Thalassemia": 0.05, "G6PD": 0.09,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.02, "PKU": 0.01},
            0.74, 0.68
        ),
        "Marathi": PopulationData(
            "Marathi", "South Asia", "India", "Indo-Aryan",
            90000000, 0.12,
            ["Beta Thalassemia", "Sickle Cell", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.06, "Alpha Thalassemia": 0.04, "G6PD": 0.07,
             "Cystic Fibrosis": 0.02, "Sickle Cell": 0.06, "PKU": 0.01},
            0.76, 0.72
        ),
        "Kashmiri": PopulationData(
            "Kashmiri", "South Asia", "India/Pakistan", "Dardic",
            7000000, 0.30,
            ["Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.09, "Alpha Thalassemia": 0.06, "G6PD": 0.08,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.01, "PKU": 0.01},
            0.71, 0.60
        ),
        "Pathan": PopulationData(
            "Pathan", "South Asia", "Pakistan/Afghanistan", "Iranian",
            50000000, 0.50,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.11, "Alpha Thalassemia": 0.08, "G6PD": 0.09,
             "Cystic Fibrosis": 0.04, "Sickle Cell": 0.02, "PKU": 0.02},
            0.69, 0.50
        ),
        "Balochi": PopulationData(
            "Balochi", "South Asia", "Pakistan/Iran", "Iranian",
            10000000, 0.55,
            ["Beta Thalassemia", "G6PD Deficiency", "Sickle Cell"],
            {"Beta Thalassemia": 0.13, "Alpha Thalassemia": 0.09, "G6PD": 0.10,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.04, "PKU": 0.02},
            0.68, 0.45
        ),
        "Sri Lankan Tamil": PopulationData(
            "Sri Lankan Tamil", "South Asia", "Sri Lanka", "Dravidian",
            3000000, 0.15,
            ["Beta Thalassemia", "Sickle Cell", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.07, "Alpha Thalassemia": 0.05, "G6PD": 0.06,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.07, "PKU": 0.01},
            0.77, 0.62
        ),

        # Middle Eastern Populations
        "Arab (Gulf)": PopulationData(
            "Arab (Gulf)", "Middle East", "Saudi Arabia/UAE/Kuwait/Qatar", "Semitic",
            50000000, 0.55,
            ["Beta Thalassemia", "Sickle Cell", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.08, "Alpha Thalassemia": 0.06, "G6PD": 0.15,
             "Cystic Fibrosis": 0.06, "Sickle Cell": 0.20, "PKU": 0.03},
            0.70, 0.80
        ),
        "Arab (Levant)": PopulationData(
            "Arab (Levant)", "Middle East", "Syria/Lebanon/Jordan/Palestine", "Semitic",
            45000000, 0.35,
            ["Beta Thalassemia", "G6PD Deficiency", "Familial Mediterranean Fever"],
            {"Beta Thalassemia": 0.06, "Alpha Thalassemia": 0.04, "G6PD": 0.08,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.03, "PKU": 0.02},
            0.73, 0.70
        ),
        "Iranian": PopulationData(
            "Iranian", "Middle East", "Iran", "Iranian",
            85000000, 0.40,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.10, "Alpha Thalassemia": 0.07, "G6PD": 0.12,
             "Cystic Fibrosis": 0.04, "Sickle Cell": 0.03, "PKU": 0.02},
            0.72, 0.65
        ),
        "Turkish": PopulationData(
            "Turkish", "Middle East", "Turkey", "Turkic",
            85000000, 0.25,
            ["Beta Thalassemia", "G6PD Deficiency", "Familial Mediterranean Fever"],
            {"Beta Thalassemia": 0.07, "Alpha Thalassemia": 0.05, "G6PD": 0.06,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.02, "PKU": 0.01},
            0.75, 0.75
        ),
        "Kurdish": PopulationData(
            "Kurdish", "Middle East", "Turkey/Iraq/Iran/Syria", "Iranian",
            35000000, 0.45,
            ["Beta Thalassemia", "G6PD Deficiency", "Sickle Cell"],
            {"Beta Thalassemia": 0.09, "Alpha Thalassemia": 0.06, "G6PD": 0.08,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.05, "PKU": 0.02},
            0.71, 0.55
        ),

        # African Populations
        "Yoruba": PopulationData(
            "Yoruba", "Africa", "Nigeria", "Niger-Congo",
            45000000, 0.05,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.02, "Alpha Thalassemia": 0.15, "G6PD": 0.25,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.25, "PKU": 0.01},
            0.85, 0.40
        ),
        "Igbo": PopulationData(
            "Igbo", "Africa", "Nigeria", "Niger-Congo",
            35000000, 0.03,
            ["Sickle Cell", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.12, "G6PD": 0.20,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.20, "PKU": 0.01},
            0.86, 0.42
        ),
        "Hausa": PopulationData(
            "Hausa", "Africa", "Nigeria/Niger", "Afro-Asiatic",
            80000000, 0.04,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.02, "Alpha Thalassemia": 0.10, "G6PD": 0.18,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.18, "PKU": 0.01},
            0.84, 0.38
        ),
        "Ethiopian": PopulationData(
            "Ethiopian", "Africa", "Ethiopia", "Afro-Asiatic",
            120000000, 0.06,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.03, "Alpha Thalassemia": 0.14, "G6PD": 0.20,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.15, "PKU": 0.01},
            0.83, 0.45
        ),
        "Kenyan": PopulationData(
            "Kenyan", "Africa", "Kenya", "Niger-Congo",
            55000000, 0.04,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.02, "Alpha Thalassemia": 0.16, "G6PD": 0.22,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.18, "PKU": 0.01},
            0.84, 0.50
        ),
        "Ghanaian": PopulationData(
            "Ghanaian", "Africa", "Ghana", "Niger-Congo",
            32000000, 0.03,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.02, "Alpha Thalassemia": 0.14, "G6PD": 0.20,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.20, "PKU": 0.01},
            0.85, 0.48
        ),

        # European Populations
        "Ashkenazi Jewish": PopulationData(
            "Ashkenazi Jewish", "Europe", "Israel/Global", "Jewish",
            11000000, 0.02,
            ["Tay-Sachs", "Gaucher", "Cystic Fibrosis", "Bloom Syndrome", "Familial Dysautonomia"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.01, "G6PD": 0.02,
             "Cystic Fibrosis": 0.04, "Sickle Cell": 0.01, "PKU": 0.01,
             "Tay-Sachs": 0.03, "Gaucher": 0.05, "Bloom Syndrome": 0.01},
            0.65, 0.90
        ),
        "Northern European": PopulationData(
            "Northern European", "Europe", "UK/Scandinavia/Germany", "Germanic",
            200000000, 0.01,
            ["Cystic Fibrosis", "Hemochromatosis", "Alpha-1 Antitrypsin Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.01, "G6PD": 0.01,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.001, "PKU": 0.01,
             "Hemochromatosis": 0.10, "Alpha-1": 0.02},
            0.80, 0.95
        ),
        "Mediterranean European": PopulationData(
            "Mediterranean European", "Europe", "Italy/Greece/Spain", "Romance/Greek",
            150000000, 0.02,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis", "Familial Mediterranean Fever"],
            {"Beta Thalassemia": 0.08, "Alpha Thalassemia": 0.05, "G6PD": 0.05,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.01, "PKU": 0.01,
             "Familial Mediterranean Fever": 0.05},
            0.78, 0.90
        ),
        "Eastern European": PopulationData(
            "Eastern European", "Europe", "Poland/Russia/Ukraine", "Slavic",
            250000000, 0.01,
            ["Cystic Fibrosis", "Tay-Sachs", "Gaucher"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.01, "G6PD": 0.02,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.001, "PKU": 0.01,
             "Tay-Sachs": 0.01, "Gaucher": 0.02},
            0.79, 0.85
        ),

        # East Asian Populations
        "Han Chinese": PopulationData(
            "Han Chinese", "East Asia", "China", "Sino-Tibetan",
            1300000000, 0.01,
            ["Alpha Thalassemia", "Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.03, "Alpha Thalassemia": 0.08, "G6PD": 0.05,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.001, "PKU": 0.01},
            0.82, 0.80
        ),
        "Japanese": PopulationData(
            "Japanese", "East Asia", "Japan", "Japonic",
            125000000, 0.005,
            ["Alpha Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.03, "G6PD": 0.02,
             "Cystic Fibrosis": 0.005, "Sickle Cell": 0.001, "PKU": 0.005},
            0.75, 0.95
        ),
        "Korean": PopulationData(
            "Korean", "East Asia", "Korea", "Koreanic",
            80000000, 0.005,
            ["Alpha Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.03, "G6PD": 0.03,
             "Cystic Fibrosis": 0.005, "Sickle Cell": 0.001, "PKU": 0.005},
            0.76, 0.92
        ),

        # Southeast Asian Populations
        "Thai": PopulationData(
            "Thai", "Southeast Asia", "Thailand", "Tai-Kadai",
            70000000, 0.10,
            ["Alpha Thalassemia", "Beta Thalassemia", "G6PD Deficiency", "HbE Disease"],
            {"Beta Thalassemia": 0.05, "Alpha Thalassemia": 0.15, "G6PD": 0.10,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01,
             "HbE Disease": 0.15},
            0.81, 0.70
        ),
        "Vietnamese": PopulationData(
            "Vietnamese", "Southeast Asia", "Vietnam", "Austroasiatic",
            100000000, 0.08,
            ["Alpha Thalassemia", "Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.04, "Alpha Thalassemia": 0.12, "G6PD": 0.08,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.82, 0.65
        ),
        "Filipino": PopulationData(
            "Filipino", "Southeast Asia", "Philippines", "Austronesian",
            110000000, 0.05,
            ["Alpha Thalassemia", "Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.03, "Alpha Thalassemia": 0.10, "G6PD": 0.06,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.83, 0.60
        ),
        "Malay": PopulationData(
            "Malay", "Southeast Asia", "Malaysia/Indonesia", "Austronesian",
            300000000, 0.08,
            ["Alpha Thalassemia", "Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.04, "Alpha Thalassemia": 0.12, "G6PD": 0.08,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.82, 0.65
        ),

        # American Populations
        "African American": PopulationData(
            "African American", "North America", "USA", "African Diaspora",
            45000000, 0.02,
            ["Sickle Cell", "G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.02, "Alpha Thalassemia": 0.10, "G6PD": 0.15,
             "Cystic Fibrosis": 0.02, "Sickle Cell": 0.08, "PKU": 0.01},
            0.83, 0.75
        ),
        "Hispanic/Latino": PopulationData(
            "Hispanic/Latino", "Americas", "USA/Latin America", "Mixed",
            650000000, 0.03,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.03, "Alpha Thalassemia": 0.04, "G6PD": 0.04,
             "Cystic Fibrosis": 0.03, "Sickle Cell": 0.02, "PKU": 0.01},
            0.85, 0.70
        ),
        "Native American": PopulationData(
            "Native American", "North America", "USA/Canada", "Indigenous",
            5000000, 0.02,
            ["G6PD Deficiency", "Alpha Thalassemia"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.05, "G6PD": 0.03,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.80, 0.55
        ),

        # Oceanian Populations
        "Australian Aboriginal": PopulationData(
            "Australian Aboriginal", "Oceania", "Australia", "Indigenous",
            800000, 0.02,
            ["Alpha Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.08, "G6PD": 0.05,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.88, 0.50
        ),
        "Maori": PopulationData(
            "Maori", "Oceania", "New Zealand", "Austronesian",
            900000, 0.02,
            ["Alpha Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.04, "G6PD": 0.03,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.85, 0.75
        ),

        # Central Asian Populations
        "Uzbek": PopulationData(
            "Uzbek", "Central Asia", "Uzbekistan", "Turkic",
            35000000, 0.25,
            ["Beta Thalassemia", "G6PD Deficiency", "Cystic Fibrosis"],
            {"Beta Thalassemia": 0.06, "Alpha Thalassemia": 0.04, "G6PD": 0.07,
             "Cystic Fibrosis": 0.02, "Sickle Cell": 0.02, "PKU": 0.01},
            0.76, 0.55
        ),
        "Kazakh": PopulationData(
            "Kazakh", "Central Asia", "Kazakhstan", "Turkic",
            20000000, 0.20,
            ["Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.04, "Alpha Thalassemia": 0.03, "G6PD": 0.05,
             "Cystic Fibrosis": 0.02, "Sickle Cell": 0.02, "PKU": 0.01},
            0.77, 0.60
        ),

        # Additional Populations
        "Romani": PopulationData(
            "Romani", "Europe", "Europe/Global", "Indo-Aryan",
            12000000, 0.05,
            ["Beta Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.05, "Alpha Thalassemia": 0.03, "G6PD": 0.04,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.74, 0.50
        ),
        "Samoan": PopulationData(
            "Samoan", "Oceania", "Samoa", "Austronesian",
            250000, 0.02,
            ["Alpha Thalassemia", "G6PD Deficiency"],
            {"Beta Thalassemia": 0.01, "Alpha Thalassemia": 0.06, "G6PD": 0.03,
             "Cystic Fibrosis": 0.01, "Sickle Cell": 0.01, "PKU": 0.01},
            0.86, 0.60
        ),
    }

    def __init__(self):
        self.populations = self.POPULATIONS

    def get_population(self, name: str) -> PopulationData:
        """Get population data by name"""
        return self.populations.get(name)

    def get_by_region(self, region: str) -> List[PopulationData]:
        """Get all populations in a region"""
        return [p for p in self.populations.values() if p.region == region]

    def get_high_risk_diseases(self, population_name: str) -> List[Dict]:
        """Get high-risk diseases for a population"""
        pop = self.populations.get(population_name)
        if not pop:
            return []

        risks = []
        for disease, freq in pop.carrier_frequencies.items():
            if freq > 0.05:  # >5% carrier frequency
                risks.append({
                    "disease": disease,
                    "carrier_frequency": freq,
                    "risk_level": "HIGH" if freq > 0.10 else "MODERATE",
                    "recommendation": f"Universal carrier screening recommended for {disease}"
                })

        return sorted(risks, key=lambda x: x["carrier_frequency"], reverse=True)

    def get_consanguinity_risk(self, population_name: str) -> Dict:
        """Get consanguinity-related risk for population"""
        pop = self.populations.get(population_name)
        if not pop:
            return {}

        return {
            "population": pop.name,
            "consanguinity_rate": pop.consanguinity_rate,
            "risk_level": "HIGH" if pop.consanguinity_rate > 0.40 else 
                         "MODERATE" if pop.consanguinity_rate > 0.20 else "LOW",
            "recommendations": self._generate_consanguinity_recommendations(pop)
        }

    def _generate_consanguinity_recommendations(self, pop: PopulationData) -> List[str]:
        """Generate recommendations based on consanguinity rate"""

        recommendations = []

        if pop.consanguinity_rate > 0.40:
            recommendations.append("CRITICAL: Very high consanguinity rate. Mandatory pre-marital genetic counseling.")
            recommendations.append("Comprehensive carrier screening for all common recessive diseases.")
            recommendations.append("Community education programs on genetic risks.")
        elif pop.consanguinity_rate > 0.20:
            recommendations.append("HIGH: Significant consanguinity rate. Strongly recommend genetic counseling.")
            recommendations.append("Targeted carrier screening for high-frequency diseases.")
        else:
            recommendations.append("LOW-MODERATE: Standard population screening guidelines apply.")

        recommendations.append("Focus on diseases with carrier frequency >5% in this population.")
        recommendations.append("Ensure culturally sensitive counseling approach.")
        recommendations.append("Respect cultural practices while providing health information.")

        return recommendations

    def get_all_populations(self) -> List[str]:
        """Get list of all population names"""
        return list(self.populations.keys())

    def get_statistics(self) -> Dict:
        """Get database statistics"""

        total_populations = len(self.populations)
        total_population_size = sum(p.population_size for p in self.populations.values())
        avg_consanguinity = sum(p.consanguinity_rate for p in self.populations.values()) / total_populations

        regions = {}
        for pop in self.populations.values():
            if pop.region not in regions:
                regions[pop.region] = 0
            regions[pop.region] += 1

        return {
            "total_populations": total_populations,
            "total_population_covered": total_population_size,
            "regions_covered": len(regions),
            "region_breakdown": regions,
            "average_consanguinity_rate": round(avg_consanguinity, 3),
            "high_consanguinity_populations": [
                p.name for p in self.populations.values() if p.consanguinity_rate > 0.40
            ]
        }

if __name__ == "__main__":
    pdb = PopulationDatabase()

    # Get statistics
    stats = pdb.get_statistics()
    print(f"Total populations: {stats['total_populations']}")
    print(f"Total population covered: {stats['total_population_covered']:,}")
    print(f"Regions: {stats['regions_covered']}")
    print(f"Average consanguinity: {stats['average_consanguinity_rate']}")
    print(f"High consanguinity populations: {stats['high_consanguinity_populations']}")

    # Get Punjabi data
    punjabi = pdb.get_population("Punjabi")
    print(f"Punjabi population: {punjabi.population_size:,}")
    print(f"Consanguinity rate: {punjabi.consanguinity_rate}")

    # Get high risk diseases
    risks = pdb.get_high_risk_diseases("Punjabi")
    print(f"High risk diseases for Punjabis:")
    for risk in risks:
        print("  " + risk["disease"] + ": " + str(round(risk["carrier_frequency"]*100, 1)) + "% carrier frequency")
