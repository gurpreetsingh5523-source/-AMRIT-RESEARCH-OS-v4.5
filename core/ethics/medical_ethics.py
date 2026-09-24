#!/usr/bin/env python3
"""
AMRIT Ethics Filter v5.0
Gurmat (Sikh ethics) + Medical ethics integration
Eugenics blocking, cultural sensitivity framework
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class EthicalStatus(Enum):
    APPROVED = "approved"
    WARNING = "warning"
    REJECTED = "rejected"
    NEEDS_REVIEW = "needs_review"

@dataclass
class EthicalAssessment:
    action: str
    status: EthicalStatus
    gurmat_principle: str
    medical_ethics_principle: str
    reasoning: str
    recommendation: str

class EthicsFilter:
    """
    Gurmat Ethics + Medical Ethics Integration

    Gurmat Principles:
    - Kirat Karo (Earn by honest labor)
    - Vand Chhako (Share with others)
    - Naam Japo (Meditate on God's name)
    - Sarbat da Bhala (Welfare of all humanity)
    - Seva (Selfless service)
    - Daya (Compassion)
    - Santokh (Contentment)
    - Pyare (Love)
    - Sat (Truth)
    - Nirmal (Purity)

    Medical Ethics Principles:
    - Autonomy (Respect for persons)
    - Beneficence (Do good)
    - Non-maleficence (Do no harm)
    - Justice (Fairness)
    - Dignity (Human worth)
    - Integrity (Honesty)
    - Accountability (Responsibility)
    """

    # Eugenics-related terms and concepts to block
    EUGENICS_TERMS = [
        "racial purity", "genetic superiority", "inferior genes",
        "breeding better humans", "genetic cleansing", "racial hygiene",
        "selective breeding", "genetic improvement of population",
        "undesirable traits", "genetic defect elimination",
        "racial betterment", "hereditary improvement",
        "genetic worth", "fitness for reproduction",
        "genetic quality control", "population genetic quality",
        "genetic hygiene", "racial biology", "hereditary health",
        "genetic selection for enhancement", "designer babies for superiority",
        "genetic discrimination", "genetic determinism",
        "inferior races", "superior races", "genetic hierarchy"
    ]

    # Cultural sensitivity guidelines
    CULTURAL_GUIDELINES = {
        "South Asian": {
            "consanguinity": "Respect cultural practices while providing genetic counseling",
            "gender_selection": "Strongly oppose - violates Sarbat da Bhala",
            "dowry_related": "Oppose - violates dignity and justice",
            "caste_based": "Oppose - violates equality and Sarbat da Bhala"
        },
        "African": {
            "sickle_cell_focus": "Provide culturally sensitive carrier screening",
            "tribal_medicine": "Respect traditional knowledge, integrate with evidence",
            "community_consent": "Emphasize community-level consent for research"
        },
        "Indigenous": {
            "bioprospecting": "Require free prior informed consent (FPIC)",
            "data_sovereignty": "Respect tribal data governance",
            "traditional_knowledge": "Protect and acknowledge traditional medicine"
        },
        "Global": {
            "exploitation": "Prevent exploitation of vulnerable populations",
            "access_equity": "Ensure equitable access to benefits",
            "capacity_building": "Build local research capacity",
            "benefit_sharing": "Share benefits with communities"
        }
    }

    def __init__(self, population: str = "Global"):
        self.population = population
        self.assessment_history = []

    def assess_action(self, action_description: str, 
                     context: Dict = None) -> EthicalAssessment:
        """Assess ethical status of an action"""

        context = context or {}
        action_lower = action_description.lower()

        # Check for eugenics
        eugenics_detected = any(term in action_lower for term in self.EUGENICS_TERMS)

        if eugenics_detected:
            return EthicalAssessment(
                action=action_description,
                status=EthicalStatus.REJECTED,
                gurmat_principle="Sarbat da Bhala (Welfare of All) - Every human has equal divine worth",
                medical_ethics_principle="Justice and Human Dignity - All humans have equal inherent worth",
                reasoning="Eugenics violates the fundamental principle that all humans are equal creations of the Divine. "
                         "It has historically led to genocide, forced sterilization, and discrimination. "
                         "Gurmat teaches 'Avval Allah Noor Upaya' - God created light in all beings equally.",
                recommendation="REJECTED: This action promotes eugenics concepts. "
                              "Focus on therapeutic interventions that respect human dignity. "
                              "All genetic interventions must be for health, not for 'improvement' of populations."
            )

        # Check for cultural sensitivity issues
        cultural_issues = self._check_cultural_sensitivity(action_description, context)

        if cultural_issues:
            return EthicalAssessment(
                action=action_description,
                status=EthicalStatus.WARNING,
                gurmat_principle="Daya (Compassion) - Respect all cultures and traditions",
                medical_ethics_principle="Autonomy and Cultural Sensitivity - Respect cultural values",
                reasoning=f"Cultural sensitivity concerns detected: {cultural_issues}",
                recommendation="NEEDS REVIEW: Ensure cultural sensitivity. Consult community leaders. "
                              "Provide culturally appropriate counseling. Respect traditional knowledge."
            )

        # Check for exploitation
        if self._is_exploitative(action_description, context):
            return EthicalAssessment(
                action=action_description,
                status=EthicalStatus.REJECTED,
                gurmat_principle="Kirat Karo (Honest Labor) - No exploitation of vulnerable",
                medical_ethics_principle="Justice - Fair distribution of benefits and burdens",
                reasoning="This action appears to exploit vulnerable populations for research benefit.",
                recommendation="REJECTED: Ensure fair benefit sharing. Build local capacity. "
                              "Provide equitable access to research outcomes. No exploitation."
            )

        # Default: approved with monitoring
        return EthicalAssessment(
            action=action_description,
            status=EthicalStatus.APPROVED,
            gurmat_principle="Seva (Selfless Service) - Serve humanity with pure intentions",
            medical_ethics_principle="Beneficence - Act in the best interest of patients",
            reasoning="Action aligns with Gurmat and medical ethics principles.",
            recommendation="APPROVED: Proceed with ethical monitoring. Ensure informed consent. "
                          "Maintain transparency. Document all actions."
        )

    def _check_cultural_sensitivity(self, action: str, context: Dict) -> List[str]:
        """Check for cultural sensitivity issues"""

        issues = []
        action_lower = action.lower()
        population = context.get("population", "Global")

        guidelines = self.CULTURAL_GUIDELINES.get(population, self.CULTURAL_GUIDELINES["Global"])

        for key, guideline in guidelines.items():
            if key in action_lower:
                issues.append(guideline)

        return issues

    def _is_exploitative(self, action: str, context: Dict) -> bool:
        """Check if action is exploitative"""

        exploitative_indicators = [
            "without consent", "without compensation", "without benefit sharing",
            "samples taken without", "data taken without", "no local capacity building",
            "no training provided", "no technology transfer"
        ]

        action_lower = action.lower()
        return any(indicator in action_lower for indicator in exploitative_indicators)

    def assess_genetic_screening(self, 
                                purpose: str,
                                population: str,
                                consent_type: str) -> EthicalAssessment:
        """Assess genetic screening program"""

        # Check for population-level eugenics
        if "population" in purpose.lower() and "improve" in purpose.lower():
            return self.assess_action(
                f"Population genetic screening for: {purpose}",
                {"population": population, "consent": consent_type}
            )

        # Check for individual benefit
        if "individual" in purpose.lower() or "family" in purpose.lower() or "health" in purpose.lower():
            return EthicalAssessment(
                action=f"Genetic screening for {purpose}",
                status=EthicalStatus.APPROVED,
                gurmat_principle="Seva (Selfless Service) - Help individuals and families",
                medical_ethics_principle="Beneficence and Autonomy - Help while respecting choice",
                reasoning="Individual and family health-focused screening aligns with ethical principles.",
                recommendation="APPROVED: Ensure informed consent. Provide genetic counseling. "
                              "Protect privacy. Allow opt-out. Focus on health benefits, not selection."
            )

        return EthicalAssessment(
            action=f"Genetic screening for {purpose}",
            status=EthicalStatus.NEEDS_REVIEW,
            gurmat_principle="Sat (Truth) - Be transparent about purpose",
            medical_ethics_principle="Transparency and Honesty - Clear communication of purpose",
            reasoning="Purpose unclear. Need to verify intent is health-focused, not eugenic.",
            recommendation="NEEDS REVIEW: Clarify purpose. Ensure health focus. "
                          "Verify no eugenic intent. Community consultation recommended."
        )

    def get_ethical_guidelines(self) -> Dict:
        """Get complete ethical guidelines"""

        return {
            "gurmat_principles": {
                "Sarbat da Bhala": "Welfare of all humanity - no discrimination",
                "Seva": "Selfless service - serve without expectation",
                "Daya": "Compassion - care for the vulnerable",
                "Kirat Karo": "Honest labor - earn through righteous means",
                "Sat": "Truth - be honest in all dealings",
                "Nirmal": "Purity - maintain ethical purity",
                "Santokh": "Contentment - do not seek to 'improve' God's creation"
            },
            "medical_ethics_principles": {
                "Autonomy": "Respect for persons and their choices",
                "Beneficence": "Act to benefit patients and society",
                "Non-maleficence": "Do no harm - first, do no harm",
                "Justice": "Fair distribution of benefits and burdens",
                "Dignity": "Respect inherent worth of every human"
            },
            "prohibited_actions": [
                "Eugenics-based selection",
                "Racial or ethnic discrimination",
                "Gender selection for non-medical reasons",
                "Exploitation of vulnerable populations",
                "Research without informed consent",
                "Genetic enhancement for non-therapeutic purposes",
                "Creation of genetic hierarchies"
            ],
            "required_actions": [
                "Informed consent for all interventions",
                "Genetic counseling for all screening",
                "Privacy protection for genetic data",
                "Cultural sensitivity in all programs",
                "Benefit sharing with communities",
                "Capacity building in resource-limited settings",
                "Equitable access to all benefits"
            ]
        }

if __name__ == "__main__":
    ethics = EthicsFilter(population="South Asian")

    # Test eugenics blocking
    result = ethics.assess_action("Implement genetic screening to improve population genetic quality")
    print(f"Action: {result.action}")
    print(f"Status: {result.status.value}")
    print(f"Reasoning: {result.reasoning}")
    print(f"Recommendation: {result.recommendation}")
    print()

    # Test approved action
    result2 = ethics.assess_action("Provide genetic counseling for thalassemia carrier screening")
    print(f"Action: {result2.action}")
    print(f"Status: {result2.status.value}")
    print(f"Recommendation: {result2.recommendation}")
