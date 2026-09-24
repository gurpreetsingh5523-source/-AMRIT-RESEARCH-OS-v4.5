import sys
import json
sys.path.append("/Users/gurpreetdhillon/Documents/antigravity/sharp-rutherford")
from core.models.router import ModelRouter

router = ModelRouter()
client = router.client_for("deep_reasoning")

prompt = """
Perform a deep, professional clinical research analysis on the following patient case:
- Patient: 70-year-old female
- Presenting Symptoms:
  - Weakness: Cannot walk, cannot use arm to lift anything (suspected acute unilateral motor weakness).
  - Paresthesia: Feet "sleeping always" (numbness/pins and needles).
- Vitals:
  - Blood Pressure: 179/100 mmHg (Severe Stage 2 Hypertension / Hypertensive Urgency bordering on Hypertensive Emergency due to neurological deficit).
  - Heart Rate: 65 bpm (normal bradycardic range).
  - Blood Glucose: Normal (no diabetes).

Perform a structured clinical evaluation as a Senior Neurologist and Critical Care Cardiologist.
Structure the report into:
1. EMERGENCY ALERT & ACTION PLAN (FAST stroke check, emergency response)
2. CLINICAL PROFILE ANALYSIS (Deconstruct the vitals and neurological signs)
3. DIFFERENTIAL DIAGNOSES (Ranked list with pathophysiology: Ischemic Stroke, Hemorrhagic Stroke, Hypertensive Emergency with Encephalopathy, Spinal Cord Compression, Guillain-Barré Syndrome)
4. DIAGNOSTIC WORKUP PATHWAY (Emergency CT, MRI, ECG, Blood Chemistry)
5. SCIENTIFIC EVIDENCE SUMMARY (Cite standard AHA/ASA guidelines for stroke and hypertensive crisis management)

Be extremely detailed, scientific, and professional. Return the response in Markdown.
"""

print("Running deep clinical reasoning via Qwen 3.5...", flush=True)
response = client.chat(prompt)
print("\n=== SYSTEM RESPONSE ===\n")
print(response)

# Save to reports/json and reports/pdf
import os
os.makedirs("reports/json", exist_ok=True)
with open("reports/json/mother_clinical_analysis.json", "w") as f:
    json.dump({"prompt": prompt, "analysis": response}, f, indent=4)
print("\nReport saved successfully to reports/json/mother_clinical_analysis.json")
