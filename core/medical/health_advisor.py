
"""
AMRIT Personalized Health Advisor v6.0
DNA Analysis + Blood Analysis + Environment + Recommendations
"""
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class RiskCategory(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

@dataclass
class HealthRecommendation:
    category: str
    recommendation: str
    priority: str
    evidence_level: str
    action_items: List[str]

class PersonalizedHealthAdvisor:
    """
    Comprehensive personalized health advisor
    Integrates DNA, blood, and environmental data
    """

    # DNA variant database
    DNA_VARIANTS = {
        'SLCO1B1': {
            'gene': 'SLCO1B1',
            'variant': 'rs4149056',
            'risk_disease': 'Statin-Induced Myopathy',
            'risk_multiplier': {'normal': 1.0, 'intermediate': 2.0, 'poor': 4.0, 'XX': 4.0, 'intermediate_metabolizer': 2.0, 'poor_metabolizer': 4.0},
            'recommendations': {
                'diet': ['Coenzyme Q10 rich foods'],
                'lifestyle': ['Monitor for muscle pain during statin therapy'],
                'supplements': ['CoQ10'],
                'screening': ['CK (Creatine Kinase) levels']
            }
        },
        'CYP2C19': {
            'gene': 'CYP2C19',
            'variant': 'rs4244285',
            'risk_disease': 'Clopidogrel Resistance',
            'risk_multiplier': {'normal': 1.0, 'intermediate': 1.5, 'poor': 3.0, 'intermediate_metabolizer': 1.5, 'poor_metabolizer': 3.0},
            'recommendations': {
                'diet': [],
                'lifestyle': ['Cardiovascular risk counseling'],
                'supplements': [],
                'screening': ['Platelet function testing']
            }
        },
        'CYP2D6': {
            'gene': 'CYP2D6',
            'variant': 'rs3892097',
            'risk_disease': 'Altered Drug Metabolism',
            'risk_multiplier': {'normal': 1.0, 'intermediate': 1.2, 'poor': 2.0, 'ultrarapid': 3.0, 'intermediate_metabolizer': 1.2, 'poor_metabolizer': 2.0, 'ultrarapid_metabolizer': 3.0},
            'recommendations': {
                'diet': [],
                'lifestyle': ['Caution with prodrugs (e.g. codeine, tramadol)'],
                'supplements': [],
                'screening': ['CYP2D6 genotyping']
            }
        },
        'APOE4': {
            'gene': 'APOE',
            'variant': 'rs429358',
            'risk_disease': "Alzheimer's Disease",
            'risk_multiplier': {'0_copies': 1.0, '1_copy': 3.0, '2_copies': 15.0},
            'recommendations': {
                'diet': ['Mediterranean diet', 'Omega-3 fatty acids', 'Limit saturated fat'],
                'lifestyle': ['Regular exercise', 'Cognitive training', 'Social engagement'],
                'supplements': ['DHA', 'Vitamin E', 'Curcumin'],
                'screening': ['Annual cognitive assessment', 'MRI at 50+']
            }
        },
        'MTHFR_C677T': {
            'gene': 'MTHFR',
            'variant': 'rs1801133',
            'risk_disease': 'Cardiovascular Disease, Neural Tube Defects',
            'risk_multiplier': {'CC': 1.0, 'CT': 1.5, 'TT': 2.0},
            'recommendations': {
                'diet': ['Folate-rich foods', 'Leafy greens', 'Legumes'],
                'lifestyle': ['Limit alcohol', 'Avoid smoking'],
                'supplements': ['Methylfolate (5-MTHF)', 'B12', 'B6'],
                'screening': ['Homocysteine levels', 'Cardiovascular risk assessment']
            }
        },
        'FTO': {
            'gene': 'FTO',
            'variant': 'rs9939609',
            'risk_disease': 'Obesity, Type 2 Diabetes',
            'risk_multiplier': {'TT': 1.7, 'AT': 1.3, 'AA': 1.0},
            'recommendations': {
                'diet': ['Portion control', 'High protein breakfast', 'Low glycemic index foods'],
                'lifestyle': ['60 min daily exercise', 'Sleep 7-8 hours', 'Stress management'],
                'supplements': ['Chromium', 'Green tea extract'],
                'screening': ['BMI monitoring', 'Glucose tolerance test', 'HbA1c']
            }
        },
        'LCT': {
            'gene': 'LCT',
            'variant': 'rs4988235',
            'risk_disease': 'Lactose Intolerance',
            'risk_multiplier': {'CC': 1.0, 'CT': 0.5, 'TT': 0.0},
            'recommendations': {
                'diet': ['Lactose-free dairy', 'Fermented dairy', 'Plant-based alternatives'],
                'lifestyle': ['Read food labels', 'Dining awareness'],
                'supplements': ['Calcium', 'Vitamin D', 'Probiotics'],
                'screening': ['Lactose tolerance test']
            }
        },
        'ALDH2': {
            'gene': 'ALDH2',
            'variant': 'rs671',
            'risk_disease': 'Alcohol Flush, Esophageal Cancer',
            'risk_multiplier': {'GG': 1.0, 'AG': 3.0, 'AA': 10.0},
            'recommendations': {
                'diet': ['Alcohol avoidance', 'Antioxidant-rich foods'],
                'lifestyle': ['Complete alcohol abstinence', 'Cancer screening'],
                'supplements': ['NAC', 'Vitamin C', 'Selenium'],
                'screening': ['Esophageal endoscopy', 'Regular cancer screening']
            }
        },
        'ACTN3': {
            'gene': 'ACTN3',
            'variant': 'rs1815739',
            'risk_disease': 'Muscle Performance',
            'risk_multiplier': {'RR': 1.0, 'RX': 0.8, 'XX': 0.6},
            'recommendations': {
                'diet': ['High protein', 'Creatine supplementation'],
                'lifestyle': ['Endurance training for XX', 'Power training for RR'],
                'supplements': ['Creatine', 'Beta-alanine', 'Protein powder'],
                'screening': ['Muscle performance testing']
            }
        },
        'CYP1A2': {
            'gene': 'CYP1A2',
            'variant': 'rs762551',
            'risk_disease': 'Caffeine Metabolism, Drug Response',
            'risk_multiplier': {'AA': 1.0, 'AC': 0.7, 'CC': 0.5},
            'recommendations': {
                'diet': ['Limit caffeine for slow metabolizers', 'Timing of medication'],
                'lifestyle': ['Morning exercise for slow metabolizers'],
                'supplements': ['Adjust caffeine intake based on genotype'],
                'screening': ['Caffeine metabolism test']
            }
        },
        'HFE': {
            'gene': 'HFE',
            'variant': 'rs1800562',
            'risk_disease': 'Hereditary Hemochromatosis',
            'risk_multiplier': {'CC': 1.0, 'CG': 10.0, 'GG': 100.0},
            'recommendations': {
                'diet': ['Avoid iron supplements', 'Limit red meat', 'Vitamin C with meals'],
                'lifestyle': ['Regular blood donation', 'Avoid alcohol'],
                'supplements': ['Avoid iron', 'Tea with meals to reduce absorption'],
                'screening': ['Ferritin levels', 'Transferrin saturation', 'Liver function']
            }
        },
        'BRCA1': {
            'gene': 'BRCA1',
            'variant': 'rs80357906',
            'risk_disease': 'Breast/Ovarian Cancer',
            'risk_multiplier': {'negative': 1.0, 'positive': 12.0},
            'recommendations': {
                'diet': ['Mediterranean diet', 'Cruciferous vegetables', 'Limit alcohol'],
                'lifestyle': ['Maintain healthy weight', 'Regular exercise', 'Breastfeeding if applicable'],
                'supplements': ['Vitamin D', 'Calcium', 'Omega-3'],
                'screening': ['Mammography starting at 25', 'MRI alternating', 'CA-125', 'Transvaginal ultrasound']
            }
        },
        'BRCA2': {
            'gene': 'BRCA2',
            'variant': 'rs80359706',
            'risk_disease': 'Breast/Prostate/Pancreatic Cancer',
            'risk_multiplier': {'negative': 1.0, 'positive': 10.0},
            'recommendations': {
                'diet': ['High fiber', 'Limit red meat', 'Antioxidant-rich foods'],
                'lifestyle': ['Regular exercise', 'Maintain healthy weight', 'No smoking'],
                'supplements': ['Vitamin D', 'Selenium', 'Lycopene'],
                'screening': ['Mammography', 'Prostate screening', 'Pancreatic screening if family history']
            }
        }
    }

    # Environmental factors
    ENVIRONMENTAL_FACTORS = {
        'PM2.5': {
            'safe_level': 12.0,  # µg/m³
            'unit': 'µg/m³',
            'health_effects': ['Respiratory disease', 'Cardiovascular disease', 'Lung cancer'],
            'mitigation': ['Air purifier', 'Mask outdoors', 'Indoor plants', 'Avoid outdoor exercise on high pollution days']
        },
        'arsenic': {
            'safe_level': 10.0,  # µg/L
            'unit': 'µg/L',
            'health_effects': ['Skin lesions', 'Cancer', 'Cardiovascular disease', 'Diabetes'],
            'mitigation': ['Water filtration', 'Reverse osmosis', 'Regular water testing', 'Dietary selenium']
        },
        'lead': {
            'safe_level': 5.0,  # µg/dL
            'unit': 'µg/dL',
            'health_effects': ['Neurodevelopmental delay', 'Hypertension', 'Kidney damage'],
            'mitigation': ['Lead abatement', 'Calcium/iron rich diet', 'Chelation if severe', 'Regular screening']
        },
        'ozone': {
            'safe_level': 70.0,  # ppb
            'unit': 'ppb',
            'health_effects': ['Asthma exacerbation', 'Lung function decline'],
            'mitigation': ['Limit outdoor activity', 'Air conditioning', 'Check AQI daily']
        }
    }

    def __init__(self):
        self.patient_data = {}
        self.recommendations_history = []

    def analyze_dna(self, dna_variants: Dict[str, str]) -> Dict:
        """Analyze DNA variants and generate risk profile"""
        results = {}
        overall_risk = 0

        for variant, genotype in dna_variants.items():
            if variant in self.DNA_VARIANTS:
                variant_info = self.DNA_VARIANTS[variant]

                # Calculate risk
                risk_mult = variant_info['risk_multiplier'].get(genotype, 1.0)

                # Determine risk category
                if risk_mult >= 10:
                    risk_cat = RiskCategory.VERY_HIGH
                elif risk_mult >= 3:
                    risk_cat = RiskCategory.HIGH
                elif risk_mult >= 1.5:
                    risk_cat = RiskCategory.MODERATE
                else:
                    risk_cat = RiskCategory.LOW

                results[variant] = {
                    'gene': variant_info['gene'],
                    'variant': variant_info['variant'],
                    'genotype': genotype,
                    'risk_disease': variant_info['risk_disease'],
                    'risk_multiplier': risk_mult,
                    'risk_category': risk_cat.value,
                    'recommendations': variant_info['recommendations']
                }

                overall_risk += risk_mult

        return {
            'variants_analyzed': len(results),
            'variant_results': results,
            'overall_risk_score': overall_risk / max(len(results), 1),
            'highest_risk_variants': self._get_highest_risk(results)
        }

    def _get_highest_risk(self, results: Dict) -> List[str]:
        """Get variants with highest risk"""
        sorted_variants = sorted(
            results.items(),
            key=lambda x: x[1]['risk_multiplier'],
            reverse=True
        )
        return [v[0] for v in sorted_variants[:3]]

    def analyze_environment(self, environmental_data: Dict[str, float]) -> Dict:
        """Analyze environmental exposures"""
        results = {}

        for factor, level in environmental_data.items():
            if factor in self.ENVIRONMENTAL_FACTORS:
                factor_info = self.ENVIRONMENTAL_FACTORS[factor]

                # Calculate risk ratio
                risk_ratio = level / factor_info['safe_level']

                if risk_ratio > 3:
                    risk_level = 'critical'
                elif risk_ratio > 1.5:
                    risk_level = 'high'
                elif risk_ratio > 1:
                    risk_level = 'moderate'
                else:
                    risk_level = 'low'

                results[factor] = {
                    'level': level,
                    'unit': factor_info['unit'],
                    'safe_level': factor_info['safe_level'],
                    'risk_ratio': risk_ratio,
                    'risk_level': risk_level,
                    'health_effects': factor_info['health_effects'],
                    'mitigation': factor_info['mitigation']
                }

        return {
            'factors_analyzed': len(results),
            'exposure_results': results,
            'critical_exposures': [k for k, v in results.items() if v['risk_level'] == 'critical'],
            'high_exposures': [k for k, v in results.items() if v['risk_level'] == 'high']
        }

    def generate_recommendations(self, dna_results: Dict, 
                               blood_results: Dict,
                               environmental_results: Dict) -> Dict:
        """Generate comprehensive personalized recommendations"""
        recommendations = {
            'diet': [],
            'lifestyle': [],
            'supplements': [],
            'exercise': [],
            'screening': [],
            'mitigation': []
        }

        # DNA-based recommendations
        for variant, result in dna_results.get('variant_results', {}).items():
            recs = result.get('recommendations', {})
            recommendations['diet'].extend(recs.get('diet', []))
            recommendations['lifestyle'].extend(recs.get('lifestyle', []))
            recommendations['supplements'].extend(recs.get('supplements', []))
            recommendations['screening'].extend(recs.get('screening', []))

        # Blood-based recommendations
        blood_analyzed = {}
        if isinstance(blood_results, dict):
            if 'analyzed' in blood_results:
                blood_analyzed = blood_results['analyzed']
            else:
                blood_analyzed = blood_results
        
        for test, result in blood_analyzed.items():
            if hasattr(result, 'risk_level'):
                risk = result.risk_level.value if hasattr(result.risk_level, 'value') else str(result.risk_level)
                diet_recs = result.diet_recommendations if hasattr(result, 'diet_recommendations') else []
                life_recs = result.lifestyle_recommendations if hasattr(result, 'lifestyle_recommendations') else []
                supp_recs = result.supplement_recommendations if hasattr(result, 'supplement_recommendations') else []
            else:
                risk = result.get('risk_level', 'normal')
                diet_recs = result.get('diet_recommendations', [])
                life_recs = result.get('lifestyle_recommendations', [])
                supp_recs = result.get('supplement_recommendations', [])

            if str(risk).lower() in ['high', 'critical']:
                recommendations['diet'].extend(diet_recs)
                recommendations['lifestyle'].extend(life_recs)
                recommendations['supplements'].extend(supp_recs)

        # Environmental recommendations
        for factor, result in environmental_results.get('exposure_results', {}).items():
            recommendations['mitigation'].extend(result.get('mitigation', []))

        # Deduplicate
        for category in recommendations:
            recommendations[category] = list(set(recommendations[category]))

        # Add exercise recommendations based on DNA
        if 'ACTN3' in dna_results.get('variant_results', {}):
            genotype = dna_results['variant_results']['ACTN3']['genotype']
            if genotype == 'RR':
                recommendations['exercise'].append('Power/sprint training optimal')
            elif genotype == 'XX':
                recommendations['exercise'].append('Endurance training optimal')
            else:
                recommendations['exercise'].append('Mixed training program')

        # Add general recommendations
        recommendations['exercise'].extend([
            '150 minutes moderate aerobic activity per week',
            '2 days strength training per week',
            'Daily flexibility exercises'
        ])

        return {
            'recommendations': recommendations,
            'priority_actions': self._prioritize_actions(recommendations),
            'follow_up_schedule': self._generate_follow_up(dna_results, blood_results)
        }

    def _prioritize_actions(self, recommendations: Dict) -> List[str]:
        """Prioritize actions based on urgency"""
        priorities = []

        # Critical items first
        if recommendations['mitigation']:
            priorities.append(f"URGENT: Address environmental exposures: {', '.join(recommendations['mitigation'][:3])}")

        if recommendations['screening']:
            priorities.append(f"Schedule screenings: {', '.join(recommendations['screening'][:3])}")

        if recommendations['supplements']:
            priorities.append(f"Start supplements: {', '.join(recommendations['supplements'][:3])}")

        if recommendations['diet']:
            priorities.append(f"Dietary changes: {', '.join(recommendations['diet'][:3])}")

        if recommendations['lifestyle']:
            priorities.append(f"Lifestyle modifications: {', '.join(recommendations['lifestyle'][:3])}")

        return priorities

    def _generate_follow_up(self, dna_results: Dict, blood_results: Dict) -> Dict:
        """Generate follow-up schedule"""
        schedule = {
            'immediate': [],
            '3_months': [],
            '6_months': [],
            '1_year': []
        }

        # Immediate actions
        if dna_results.get('highest_risk_variants'):
            schedule['immediate'].append('Genetic counseling consultation')

        # 3-month follow-up
        schedule['3_months'].append('Repeat blood panel')
        schedule['3_months'].append('Lifestyle adherence check')

        # 6-month follow-up
        schedule['6_months'].append('Comprehensive health review')
        schedule['6_months'].append('Environmental re-assessment')

        # 1-year follow-up
        schedule['1_year'].append('Annual physical examination')
        schedule['1_year'].append('Genetic risk re-evaluation')
        schedule['1_year'].append('Long-term outcome assessment')

        return schedule

    def generate_medications(self, dna_results: Dict, blood_results: Dict) -> List[Dict]:
        """
        Clinical Drug Recommendation & Pharmacogenomics Alignment Engine
        Bridges Blood Test results -> Standard Medications -> DNA Variant safety check
        """
        med_recommendations = []
        variant_results = dna_results.get('variant_results', {})
        
        # Robustly extract analyzed blood test data
        analyzed_data = {}
        if isinstance(blood_results, dict):
            if 'analyzed' in blood_results:
                analyzed_data = blood_results['analyzed']
            else:
                analyzed_data = blood_results

        # Helper to get value and risk level regardless of object or dict format
        def get_test_info(test_name):
            res = analyzed_data.get(test_name)
            if res is None:
                return None, None
            # If it is a BloodTestResult object
            if hasattr(res, 'value') and hasattr(res, 'risk_level'):
                rl = res.risk_level.value if hasattr(res.risk_level, 'value') else str(res.risk_level)
                return res.value, rl.lower()
            # If it is a dict
            if isinstance(res, dict):
                rl = res.get('risk_level', 'normal')
                if isinstance(rl, dict):
                    rl = rl.get('value', 'normal')
                return res.get('value', 0.0), str(rl).lower()
            return None, None

        # 1. Check Diabetes (Glucose / HbA1c)
        glucose_val, glucose_risk = get_test_info('glucose_fasting')
        hba1c_val, hba1c_risk = get_test_info('hba1c')
        
        # fallback to general checks
        if glucose_val is None:
            for k in analyzed_data.keys():
                if 'glucose' in k.lower():
                    glucose_val, glucose_risk = get_test_info(k)
        if hba1c_val is None:
            for k in analyzed_data.keys():
                if 'hba1c' in k.lower():
                    hba1c_val, hba1c_risk = get_test_info(k)

        glucose_val = glucose_val or 0.0
        hba1c_val = hba1c_val or 0.0

        if glucose_val > 126.0 or hba1c_val > 6.5 or glucose_risk in ['high', 'critical'] or hba1c_risk in ['high', 'critical']:
            rec = {
                'disease': 'Type 2 Diabetes Mellitus',
                'marker_trigger': f'Glucose: {glucose_val} mg/dL, HbA1c: {hba1c_val}%',
                'recommended_drug': 'Metformin',
                'status': 'Approved',
                'notes': 'Standard first-line pharmacotherapy for glycemic control.',
                'alternative_suggested': None
            }
            mthfr_gen = variant_results.get('MTHFR_C677T', {}).get('genotype', '')
            if 'T' in mthfr_gen:
                rec['status'] = 'Approved with Caution'
                rec['notes'] += f" Warning: Patient has MTHFR {mthfr_gen} genotype. Metformin can exacerbate vitamin B12/folate depletion. Recommend co-supplementation with active Methylfolate (5-MTHF) and B12."
            med_recommendations.append(rec)

        # 2. Check Hyperlipidemia (LDL / Total Cholesterol)
        ldl_val, ldl_risk = get_test_info('ldl_cholesterol')
        if ldl_val is None:
            for k in analyzed_data.keys():
                if 'ldl' in k.lower():
                    ldl_val, ldl_risk = get_test_info(k)
                    
        ldl_val = ldl_val or 0.0

        if ldl_val > 130.0 or ldl_risk in ['high', 'critical']:
            rec = {
                'disease': 'Hyperlipidemia',
                'marker_trigger': f'LDL Cholesterol: {ldl_val} mg/dL',
                'recommended_drug': 'Simvastatin',
                'status': 'Approved',
                'notes': 'HMG-CoA reductase inhibitor for lipid-lowering therapy.',
                'alternative_suggested': None
            }
            slco1b1_val = variant_results.get('SLCO1B1', {})
            slco_gen = slco1b1_val.get('genotype', '').lower()
            if 'poor' in slco_gen or 'intermediate' in slco_gen or 'xx' in slco_gen:
                rec['status'] = 'CONTRAINDICATED / HIGH RISK'
                rec['notes'] = f"Contraindicated due to SLCO1B1 poor/intermediate transporter phenotype ({slco_gen}). High risk of statin-induced myopathy/rhabdomyolysis."
                rec['alternative_suggested'] = 'Pravastatin or Rosuvastatin (lower dependency on SLCO1B1)'
            med_recommendations.append(rec)

        # 3. Check Cardiovascular Clot Risk
        if ldl_val > 160.0 or ldl_risk == 'critical':
            rec = {
                'disease': 'Cardiovascular Risk Prevention',
                'marker_trigger': f'LDL Cholesterol: {ldl_val} mg/dL (Critical Hyperlipidemia)',
                'recommended_drug': 'Clopidogrel',
                'status': 'Approved',
                'notes': 'Antiplatelet therapy for thrombotic risk reduction.',
                'alternative_suggested': None
            }
            cyp2c19_gen = variant_results.get('CYP2C19', {}).get('genotype', '').lower()
            if 'poor' in cyp2c19_gen or 'intermediate' in cyp2c19_gen:
                rec['status'] = 'HIGH RISK / INEFFECTIVE'
                rec['notes'] = f"Reduced activation of clopidogrel due to CYP2C19 loss-of-function phenotype ({cyp2c19_gen}). Increased risk of major adverse cardiovascular events."
                rec['alternative_suggested'] = 'Prasugrel or Ticagrelor (CYP2C19-independent antiplatelets)'
            med_recommendations.append(rec)

        # 4. Check Pain Management (General screening for CYP2D6 codeine response)
        cyp2d6_gen = variant_results.get('CYP2D6', {}).get('genotype', '').lower()
        if cyp2d6_gen:
            rec = {
                'disease': 'Pain Management (Analgesic Screening)',
                'marker_trigger': 'CYP2D6 Genetic Variant Screening',
                'recommended_drug': 'Codeine',
                'status': 'Approved',
                'notes': 'Standard opioid prodrug for moderate pain management.',
                'alternative_suggested': None
            }
            if 'poor' in cyp2d6_gen:
                rec['status'] = 'CONTRAINDICATED / INEFFECTIVE'
                rec['notes'] = "Ineffective analgesic. CYP2D6 poor metabolizers cannot convert codeine to its active form (morphine)."
                rec['alternative_suggested'] = 'NSAIDs (e.g. Ibuprofen) or non-CYP2D6 opioids (e.g. Morphine)'
            elif 'ultra' in cyp2d6_gen:
                rec['status'] = 'CONTRAINDICATED / TOXICITY RISK'
                rec['notes'] = "High risk of life-threatening respiratory depression due to rapid conversion to morphine in CYP2D6 ultrarapid metabolizers."
                rec['alternative_suggested'] = 'NSAIDs or non-CYP2D6 opioids'
            med_recommendations.append(rec)

        return med_recommendations

    def generate_diet_plan(self, dna_results: Dict, blood_results: Dict, environmental_results: Dict) -> Dict:
        """
        Generates a personalized clinical diet plan based on genetic and blood panel risks.
        """
        diet_plan = {
            'dietary_pattern': 'General Balanced Diet',
            'macronutrients': {'carbohydrates': '50%', 'protein': '20%', 'fats': '30%'},
            'foods_to_include': ['Whole grains', 'Lean proteins (poultry, fish)', 'Leafy greens', 'Cruciferous vegetables', 'Water (2.5L/day)'],
            'foods_to_avoid': ['Processed sugars', 'Trans fats', 'Excess caffeine', 'Refined flour'],
            'clinical_rationale': 'Standard nutritional profiling for maintenance of normal metabolic function.'
        }

        variant_results = dna_results.get('variant_results', {})
        
        analyzed_data = {}
        if isinstance(blood_results, dict):
            if 'analyzed' in blood_results:
                analyzed_data = blood_results['analyzed']
            else:
                analyzed_data = blood_results

        def get_test_info(test_name):
            res = analyzed_data.get(test_name)
            if res is None:
                return None, None
            if hasattr(res, 'value') and hasattr(res, 'risk_level'):
                rl = res.risk_level.value if hasattr(res.risk_level, 'value') else str(res.risk_level)
                return res.value, rl.lower()
            if isinstance(res, dict):
                rl = res.get('risk_level', 'normal')
                if isinstance(rl, dict):
                    rl = rl.get('value', 'normal')
                return res.get('value', 0.0), str(rl).lower()
            return None, None

        glucose_val, glucose_risk = get_test_info('glucose_fasting')
        hba1c_val, hba1c_risk = get_test_info('hba1c')
        ldl_val, ldl_risk = get_test_info('ldl_cholesterol')

        has_diabetes = (glucose_val is not None and glucose_val > 126.0) or (hba1c_val is not None and hba1c_val > 6.5) or glucose_risk in ['high', 'critical'] or hba1c_risk in ['high', 'critical']
        has_hyperlipidemia = (ldl_val is not None and ldl_val > 130.0) or ldl_risk in ['high', 'critical']

        if has_diabetes:
            diet_plan['dietary_pattern'] = 'Low-Glycemic Index (Low-GI) Diabetic Diet'
            diet_plan['macronutrients'] = {'carbohydrates': '35%', 'protein': '30%', 'fats': '35%'}
            diet_plan['foods_to_include'].extend(['High-fiber legumes', 'Avocados', 'Berries', 'Chia seeds', 'Cinnamon'])
            diet_plan['foods_to_avoid'].extend(['Fruit juices', 'White bread/rice', 'Sodas', 'Sweets'])
            diet_plan['clinical_rationale'] = 'Optimized macronutrient ratios to prevent postprandial glucose spikes and improve insulin sensitivity.'

        elif has_hyperlipidemia:
            diet_plan['dietary_pattern'] = 'Cardioprotective Mediterranean Diet'
            diet_plan['macronutrients'] = {'carbohydrates': '45%', 'protein': '20%', 'fats': '35% (primarily unsaturated)'}
            diet_plan['foods_to_include'].extend(['Extra virgin olive oil', 'Walnuts/Almonds', 'Wild-caught salmon', 'Oats', 'Garlic'])
            diet_plan['foods_to_avoid'].extend(['Butter/Lard', 'Red meat', 'Full-fat dairy', 'Fried foods'])
            diet_plan['clinical_rationale'] = 'Rich in monounsaturated fatty acids and soluble fiber to accelerate LDL clearance and reduce plaque formation.'

        if 'MTHFR_C677T' in variant_results:
            genotype = variant_results['MTHFR_C677T'].get('genotype', '')
            if 'T' in genotype:
                diet_plan['foods_to_include'].extend(['Folate-rich spinach', 'Asparagus', 'Broccoli', 'Lentils'])
                diet_plan['foods_to_avoid'].extend(['Synthetic folic acid-fortified grains'])
                diet_plan['clinical_rationale'] += ' Plus genetic adjustments for MTHFR variant: prioritize natural L-methylfolate dietary sources.'

        if 'LCT' in variant_results:
            genotype = variant_results['LCT'].get('genotype', '')
            if genotype == 'CC':
                diet_plan['dietary_pattern'] = 'Lactose-Free ' + diet_plan['dietary_pattern']
                diet_plan['foods_to_include'].extend(['Lactose-free almond/coconut milk', 'Fermented kefir', 'Hard cheeses'])
                diet_plan['foods_to_avoid'].extend(['Milk', 'Ice cream', 'Soft cheeses'])
                diet_plan['clinical_rationale'] += ' Lactose-intolerant genotype (LCT rs4988235-CC) alignment.'

        diet_plan['foods_to_include'] = list(set(diet_plan['foods_to_include']))
        diet_plan['foods_to_avoid'] = list(set(diet_plan['foods_to_avoid']))

        return diet_plan

    def full_health_assessment(self, patient_data: Dict) -> Dict:
        """Run complete health assessment"""
        dna_results = self.analyze_dna(patient_data.get('dna_variants', {}))
        env_results = self.analyze_environment(patient_data.get('environmental', {}))

        # Real integration of BloodAnalyzer
        blood_results = patient_data.get('blood_results', {})
        blood_data = patient_data.get('blood', {})
        if blood_data and not blood_results:
            from core.medical.blood_analyzer import BloodAnalyzer
            ba = BloodAnalyzer()
            blood_results = ba.analyze_panel(blood_data)

        recommendations = self.generate_recommendations(dna_results, blood_results, env_results)
        medication_recommendations = self.generate_medications(dna_results, blood_results)
        diet_plan = self.generate_diet_plan(dna_results, blood_results, env_results)

        # Real integration of MedicalVisionAnalyzer
        vision_results = []
        visual_scans = patient_data.get('visual_scans', [])
        if visual_scans:
            from core.medical.vision_analyzer import MedicalVisionAnalyzer
            mva = MedicalVisionAnalyzer()
            inner_recs = recommendations.get('recommendations', {})
            for scan in visual_scans:
                path_or_b64 = ""
                stype = "general"
                if isinstance(scan, dict):
                    path_or_b64 = scan.get('path') or scan.get('image_path_or_base64') or ""
                    stype = scan.get('scan_type', 'general')
                elif isinstance(scan, str):
                    path_or_b64 = scan
                
                if path_or_b64:
                    scan_analysis = mva.analyze_scan(path_or_b64, stype)
                    vision_results.append(scan_analysis)

                    if 'recommendations' in scan_analysis and 'screening' in inner_recs:
                        inner_recs['screening'].extend(scan_analysis['recommendations'])
            
            if 'screening' in inner_recs:
                inner_recs['screening'] = list(set(inner_recs['screening']))

        return {
            'patient_id': patient_data.get('id', 'unknown'),
            'assessment_date': datetime.now().isoformat(),
            'dna_analysis': dna_results,
            'blood_analysis': blood_results,
            'environmental_analysis': env_results,
            'recommendations': recommendations,
            'medication_recommendations': medication_recommendations,
            'diet_plan': diet_plan,
            'vision_analysis': vision_results,
            'overall_health_score': self._calculate_health_score(dna_results, blood_results, env_results)
        }

    def _calculate_health_score(self, dna: Dict, blood: Dict, env: Dict) -> float:
        """Calculate overall health score"""
        score = 100.0

        # DNA risk deduction
        dna_risk = dna.get('overall_risk_score', 1.0)
        score -= (dna_risk - 1.0) * 5

        # Environmental deduction
        for factor, result in env.get('exposure_results', {}).items():
            if result['risk_level'] == 'critical':
                score -= 20
            elif result['risk_level'] == 'high':
                score -= 10
            elif result['risk_level'] == 'moderate':
                score -= 5

        # Blood test deduction
        for test, result in blood.get('analyzed', {}).items():
            if result.get('risk_level') == 'critical':
                score -= 15
            elif result.get('risk_level') == 'high':
                score -= 10

        return max(0, min(100, score))
