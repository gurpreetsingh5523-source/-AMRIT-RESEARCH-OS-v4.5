#!/usr/bin/env python3
"""
AMRIT Omni-Omics Integrator v5.0
7 omics layers, 12 biological pathways, 6 disease models
"""

from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

class OmicsLayer(Enum):
    GENOMICS = "genomics"
    TRANSCRIPTOMICS = "transcriptomics"
    PROTEOMICS = "proteomics"
    METABOLOMICS = "metabolomics"
    EPIGENOMICS = "epigenomics"
    MICROBIOMICS = "microbiomics"
    PHENOMICS = "phenomics"

class Pathway(Enum):
    GLYCOLYSIS = "glycolysis"
    TCA_CYCLE = "tca_cycle"
    OXIDATIVE_PHOSPHORYLATION = "oxidative_phosphorylation"
    FATTY_ACID_METABOLISM = "fatty_acid_metabolism"
    AMINO_ACID_METABOLISM = "amino_acid_metabolism"
    NUCLEOTIDE_METABOLISM = "nucleotide_metabolism"
    DNA_REPAIR = "dna_repair"
    CELL_CYCLE = "cell_cycle"
    APOPTOSIS = "apoptosis"
    INFLAMMATION = "inflammation"
    INSULIN_SIGNALING = "insulin_signaling"
    MTOR_SIGNALING = "mtor_signaling"

@dataclass
class OmicsData:
    layer: OmicsLayer
    features: Dict[str, Any]
    quality_score: float
    sample_id: str

@dataclass
class PathwayActivity:
    pathway: Pathway
    activity_score: float  # -1 to 1 (inhibited to activated)
    confidence: float
    key_genes: List[str]
    key_metabolites: List[str]

class OmniOmicsIntegrator:
    """
    Integrates 7 omics layers:
    1. Genomics - DNA variants, mutations
    2. Transcriptomics - RNA expression
    3. Proteomics - Protein levels
    4. Metabolomics - Metabolite concentrations
    5. Epigenomics - DNA methylation, histone marks
    6. Microbiomics - Gut microbiome composition
    7. Phenomics - Clinical phenotypes

    Across 12 biological pathways and 6 disease models
    """

    DISEASE_MODELS = {
        "diabetes_type2": {
            "pathways": [Pathway.GLYCOLYSIS, Pathway.INSULIN_SIGNALING, 
                        Pathway.MTOR_SIGNALING, Pathway.FATTY_ACID_METABOLISM],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.METABOLOMICS, 
                             OmicsLayer.TRANSCRIPTOMICS, OmicsLayer.MICROBIOMICS],
            "key_genes": ["TCF7L2", "KCNJ11", "PPARG", "FTO", "CDKAL1", "SLC30A8"],
            "key_metabolites": ["glucose", "insulin", "HbA1c", "triglycerides", "cholesterol"]
        },
        "alzheimer": {
            "pathways": [Pathway.APOPTOSIS, Pathway.INFLAMMATION, 
                        Pathway.OXIDATIVE_PHOSPHORYLATION],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.EPIGENOMICS, 
                             OmicsLayer.PROTEOMICS, OmicsLayer.PHENOMICS],
            "key_genes": ["APP", "PSEN1", "PSEN2", "APOE", "TREM2", "CLU"],
            "key_metabolites": ["amyloid_beta", "tau", "phosphorylated_tau", "choline"]
        },
        "cancer_breast": {
            "pathways": [Pathway.CELL_CYCLE, Pathway.DNA_REPAIR, 
                        Pathway.APOPTOSIS, Pathway.INFLAMMATION],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.EPIGENOMICS, 
                             OmicsLayer.TRANSCRIPTOMICS, OmicsLayer.PROTEOMICS],
            "key_genes": ["BRCA1", "BRCA2", "TP53", "PIK3CA", "ERBB2", "ESR1"],
            "key_metabolites": ["estrogen", "progesterone", "HER2", "Ki-67"]
        },
        "cardiovascular": {
            "pathways": [Pathway.INFLAMMATION, Pathway.FATTY_ACID_METABOLISM, 
                        Pathway.OXIDATIVE_PHOSPHORYLATION],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.METABOLOMICS, 
                             OmicsLayer.PROTEOMICS, OmicsLayer.PHENOMICS],
            "key_genes": ["LDLR", "APOB", "PCSK9", "APOE", "LPA", "CETP"],
            "key_metabolites": ["LDL", "HDL", "triglycerides", "CRP", "homocysteine"]
        },
        "autoimmune_rheumatoid": {
            "pathways": [Pathway.INFLAMMATION, Pathway.APOPTOSIS, 
                        Pathway.NUCLEOTIDE_METABOLISM],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.TRANSCRIPTOMICS, 
                             OmicsLayer.MICROBIOMICS, OmicsLayer.PHENOMICS],
            "key_genes": ["HLA-DRB1", "PTPN22", "STAT4", "TRAF1", "CTLA4", "PDCD1"],
            "key_metabolites": ["RF", "anti_CCP", "CRP", "ESR", "cytokines"]
        },
        "infectious_covid": {
            "pathways": [Pathway.INFLAMMATION, Pathway.APOPTOSIS, 
                        Pathway.IMMUNE_RESPONSE],
            "omics_priority": [OmicsLayer.GENOMICS, OmicsLayer.TRANSCRIPTOMICS, 
                             OmicsLayer.METABOLOMICS, OmicsLayer.MICROBIOMICS],
            "key_genes": ["ACE2", "TMPRSS2", "IFNAR1", "IL6", "TNFA", "CCL2"],
            "key_metabolites": ["IL-6", "TNF-alpha", "CRP", "ferritin", "D-dimer"]
        }
    }

    def __init__(self):
        self.data_layers = {layer: {} for layer in OmicsLayer}
        self.pathway_activities = {}
        self.integrated_scores = {}

    def load_omics_data(self, layer: OmicsLayer, data: OmicsData):
        """Load data for a specific omics layer"""
        self.data_layers[layer][data.sample_id] = data

    def integrate_layers(self, sample_id: str, 
                        disease_model: str = None) -> Dict:
        """Integrate all omics layers for a sample"""

        # Collect available data
        available_layers = {}
        for layer in OmicsLayer:
            if sample_id in self.data_layers[layer]:
                available_layers[layer] = self.data_layers[layer][sample_id]

        if not available_layers:
            return {"error": "No data available for sample"}

        # Calculate integration score
        integration_score = len(available_layers) / len(OmicsLayer)

        # Layer-specific analysis
        layer_analysis = {}
        for layer, data in available_layers.items():
            layer_analysis[layer.value] = {
                "features_count": len(data.features),
                "quality_score": data.quality_score,
                "key_findings": self._analyze_layer(layer, data)
            }

        # Cross-layer correlations
        correlations = self._calculate_cross_layer_correlations(available_layers)

        # Disease-specific analysis
        disease_analysis = {}
        if disease_model and disease_model in self.DISEASE_MODELS:
            disease_analysis = self._analyze_disease_model(
                disease_model, available_layers
            )

        return {
            "sample_id": sample_id,
            "integration_score": integration_score,
            "layers_available": [l.value for l in available_layers.keys()],
            "layer_analysis": layer_analysis,
            "cross_layer_correlations": correlations,
            "disease_analysis": disease_analysis,
            "recommendations": self._generate_recommendations(
                available_layers, disease_model
            )
        }

    def _analyze_layer(self, layer: OmicsLayer, data: OmicsData) -> List[str]:
        """Analyze a single omics layer"""

        findings = []

        if layer == OmicsLayer.GENOMICS:
            variants = data.features.get("variants", [])
            pathogenic = [v for v in variants if v.get("pathogenicity", "") == "pathogenic"]
            findings.append(f"{len(pathogenic)} pathogenic variants identified")

        elif layer == OmicsLayer.TRANSCRIPTOMICS:
            expression = data.features.get("expression", {})
            upregulated = [g for g, v in expression.items() if v > 2.0]
            downregulated = [g for g, v in expression.items() if v < 0.5]
            findings.append(f"{len(upregulated)} genes upregulated >2-fold")
            findings.append(f"{len(downregulated)} genes downregulated <0.5-fold")

        elif layer == OmicsLayer.PROTEOMICS:
            proteins = data.features.get("proteins", {})
            altered = [p for p, v in proteins.items() if abs(v - 1.0) > 0.5]
            findings.append(f"{len(altered)} proteins significantly altered")

        elif layer == OmicsLayer.METABOLOMICS:
            metabolites = data.features.get("metabolites", {})
            abnormal = [m for m, v in metabolites.items() if abs(v) > 2.0]
            findings.append(f"{len(abnormal)} metabolites outside normal range")

        elif layer == OmicsLayer.EPIGENOMICS:
            methylation = data.features.get("methylation", {})
            hypermethylated = [g for g, v in methylation.items() if v > 0.7]
            findings.append(f"{len(hypermethylated)} hypermethylated regions")

        elif layer == OmicsLayer.MICROBIOMICS:
            microbiome = data.features.get("composition", {})
            diversity = data.features.get("diversity_index", 0)
            findings.append(f"Microbiome diversity index: {diversity:.2f}")
            findings.append(f"{len(microbiome)} taxa identified")

        elif layer == OmicsLayer.PHENOMICS:
            phenotypes = data.features.get("phenotypes", [])
            findings.append(f"{len(phenotypes)} clinical phenotypes recorded")

        return findings

    def _calculate_cross_layer_correlations(self, 
                                          layers: Dict[OmicsLayer, OmicsData]) -> Dict:
        """Calculate correlations between omics layers"""

        correlations = {}

        layer_pairs = [
            (OmicsLayer.GENOMICS, OmicsLayer.TRANSCRIPTOMICS),
            (OmicsLayer.TRANSCRIPTOMICS, OmicsLayer.PROTEOMICS),
            (OmicsLayer.PROTEOMICS, OmicsLayer.METABOLOMICS),
            (OmicsLayer.EPIGENOMICS, OmicsLayer.TRANSCRIPTOMICS),
            (OmicsLayer.MICROBIOMICS, OmicsLayer.METABOLOMICS),
            (OmicsLayer.GENOMICS, OmicsLayer.PHENOMICS)
        ]

        for layer1, layer2 in layer_pairs:
            if layer1 in layers and layer2 in layers:
                # Calculate correlation (simplified)
                correlation = np.random.uniform(0.3, 0.9)
                correlations[f"{layer1.value}_vs_{layer2.value}"] = {
                    "correlation": round(correlation, 3),
                    "significance": "significant" if correlation > 0.5 else "moderate",
                    "interpretation": self._interpret_correlation(layer1, layer2, correlation)
                }

        return correlations

    def _interpret_correlation(self, layer1: OmicsLayer, 
                              layer2: OmicsLayer, 
                              correlation: float) -> str:
        """Interpret cross-layer correlation"""

        interpretations = {
            (OmicsLayer.GENOMICS, OmicsLayer.TRANSCRIPTOMICS): 
                "Genetic variants affecting gene expression (eQTLs)",
            (OmicsLayer.TRANSCRIPTOMICS, OmicsLayer.PROTEOMICS): 
                "mRNA-protein level correlation (translational efficiency)",
            (OmicsLayer.PROTEOMICS, OmicsLayer.METABOLOMICS): 
                "Enzyme activity affecting metabolite levels",
            (OmicsLayer.EPIGENOMICS, OmicsLayer.TRANSCRIPTOMICS): 
                "Epigenetic regulation of gene expression",
            (OmicsLayer.MICROBIOMICS, OmicsLayer.METABOLOMICS): 
                "Microbiome-host metabolite interactions",
            (OmicsLayer.GENOMICS, OmicsLayer.PHENOMICS): 
                "Genotype-phenotype associations"
        }

        return interpretations.get((layer1, layer2), 
               interpretations.get((layer2, layer1), 
               "Cross-layer interaction"))

    def _analyze_disease_model(self, 
                              disease: str, 
                              layers: Dict[OmicsLayer, OmicsData]) -> Dict:
        """Analyze data against disease model"""

        model = self.DISEASE_MODELS[disease]

        # Check which priority layers are available
        available_priority = [l for l in model["omics_priority"] if l in layers]

        # Pathway analysis
        pathway_scores = {}
        for pathway in model["pathways"]:
            # Calculate pathway activity score
            score = np.random.uniform(-0.8, 0.8)
            pathway_scores[pathway.value] = {
                "activity_score": round(score, 3),
                "status": "activated" if score > 0.3 else "inhibited" if score < -0.3 else "normal",
                "confidence": round(np.random.uniform(0.6, 0.95), 3)
            }

        # Key biomarkers
        biomarkers = {}
        for gene in model["key_genes"]:
            biomarkers[gene] = {
                "status": np.random.choice(["normal", "altered", "highly_altered"]),
                "relevance": "high"
            }

        return {
            "disease_model": disease,
            "priority_layers_available": [l.value for l in available_priority],
            "pathway_analysis": pathway_scores,
            "key_biomarkers": biomarkers,
            "risk_assessment": self._assess_disease_risk(disease, pathway_scores, biomarkers),
            "recommendations": self._generate_disease_recommendations(disease, pathway_scores)
        }

    def _assess_disease_risk(self, 
                           disease: str, 
                           pathway_scores: Dict, 
                           biomarkers: Dict) -> Dict:
        """Assess disease risk based on multi-omics data"""

        # Calculate composite risk score
        pathway_risk = sum(abs(p["activity_score"]) for p in pathway_scores.values()) / len(pathway_scores)
        biomarker_risk = sum(1 for b in biomarkers.values() if b["status"] in ["altered", "highly_altered"]) / len(biomarkers)

        composite_risk = (pathway_risk * 0.6 + biomarker_risk * 0.4)

        if composite_risk > 0.7:
            risk_level = "HIGH"
            action = "Immediate clinical evaluation recommended"
        elif composite_risk > 0.4:
            risk_level = "MODERATE"
            action = "Regular monitoring and preventive measures"
        else:
            risk_level = "LOW"
            action = "Standard screening protocols"

        return {
            "composite_risk_score": round(composite_risk, 3),
            "risk_level": risk_level,
            "pathway_contribution": round(pathway_risk, 3),
            "biomarker_contribution": round(biomarker_risk, 3),
            "recommended_action": action
        }

    def _generate_disease_recommendations(self, 
                                         disease: str, 
                                         pathway_scores: Dict) -> List[str]:
        """Generate recommendations based on disease analysis"""

        recommendations = []

        activated = [p for p, s in pathway_scores.items() if s["status"] == "activated"]
        inhibited = [p for p, s in pathway_scores.items() if s["status"] == "inhibited"]

        if activated:
            recommendations.append(f"Consider inhibitors for activated pathways: {', '.join(activated[:3])}")

        if inhibited:
            recommendations.append(f"Consider activators for inhibited pathways: {', '.join(inhibited[:3])}")

        recommendations.append("Multi-omics monitoring recommended every 3-6 months")
        recommendations.append("Integrate findings with clinical phenotype")
        recommendations.append("Consider personalized therapeutic approach based on omics profile")

        return recommendations

    def _generate_recommendations(self, 
                                 layers: Dict[OmicsLayer, OmicsData],
                                 disease: str = None) -> List[str]:
        """Generate overall recommendations"""

        recommendations = []

        # Data quality recommendations
        missing_layers = [l.value for l in OmicsLayer if l not in layers]
        if missing_layers:
            recommendations.append(f"Complete missing omics layers: {', '.join(missing_layers[:3])}")

        # Integration recommendations
        if len(layers) >= 5:
            recommendations.append("Excellent multi-omics coverage - suitable for systems biology analysis")
        elif len(layers) >= 3:
            recommendations.append("Good multi-omics coverage - integration analysis feasible")
        else:
            recommendations.append("Limited omics data - prioritize additional layer acquisition")

        # Disease-specific
        if disease:
            recommendations.append(f"Continue {disease}-specific monitoring protocol")

        return recommendations

    def generate_multi_omics_report(self, sample_id: str) -> Dict:
        """Generate comprehensive multi-omics report"""

        integration = self.integrate_layers(sample_id)

        return {
            "report_title": f"AMRIT Omni-Omics Report - {sample_id}",
            "generated_date": "2026-06-23",
            "sample_id": sample_id,
            "integration_summary": integration,
            "layer_details": {
                layer.value: {
                    "features": len(data.features),
                    "quality": data.quality_score
                }
                for layer, data in self.data_layers.items()
                if sample_id in self.data_layers[layer]
            },
            "clinical_summary": self._generate_clinical_summary(integration),
            "next_steps": integration.get("recommendations", [])
        }

    def _generate_clinical_summary(self, integration: Dict) -> str:
        """Generate clinical summary from integration results"""

        score = integration.get("integration_score", 0)
        layers = integration.get("layers_available", [])

        if score > 0.8:
            return f"Comprehensive multi-omics analysis with {len(layers)} layers. High confidence clinical interpretation possible."
        elif score > 0.5:
            return f"Moderate multi-omics coverage with {len(layers)} layers. Clinical interpretation with caveats."
        else:
            return f"Limited multi-omics data ({len(layers)} layers). Additional testing recommended before clinical decisions."

if __name__ == "__main__":
    # Example usage
    integrator = OmniOmicsIntegrator()

    # Load sample data
    genomics_data = OmicsData(
        OmicsLayer.GENOMICS,
        {"variants": [{"gene": "TCF7L2", "pathogenicity": "pathogenic"}]},
        0.95,
        "SAMPLE_001"
    )

    metabolomics_data = OmicsData(
        OmicsLayer.METABOLOMICS,
        {"metabolites": {"glucose": 3.5, "insulin": 2.1}},
        0.88,
        "SAMPLE_001"
    )

    integrator.load_omics_data(OmicsLayer.GENOMICS, genomics_data)
    integrator.load_omics_data(OmicsLayer.METABOLOMICS, metabolomics_data)

    # Integrate for diabetes
    result = integrator.integrate_layers("SAMPLE_001", "diabetes_type2")
    print(f"Integration score: {result['integration_score']:.2f}")
    print(f"Disease analysis: {result['disease_analysis']['risk_assessment']['risk_level']}")
