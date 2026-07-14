import json
import time
import re

from google import genai

from config import Config


# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


# ==========================================================
# AI Engine
# ==========================================================

class MedicineAI:

    MODEL = "gemini-2.5-flash"

    # ------------------------------------------------------
    # Internal Gemini Request
    # ------------------------------------------------------

    @staticmethod
    def _generate(prompt, retries=3):

        for attempt in range(retries):

            try:

                response = client.models.generate_content(

                    model=MedicineAI.MODEL,

                    contents=prompt

                )

                return response.text.strip()

            except Exception as e:

                error = str(e)

                if "503" in error and attempt < retries - 1:

                    time.sleep(2)

                    continue

                return f"AI Error : {error}"

        return "AI Service Busy."

    # ------------------------------------------------------
    # Clean JSON
    # ------------------------------------------------------

    @staticmethod
    def _clean_json(text):

        text = text.replace("```json", "")

        text = text.replace("```", "")

        text = text.strip()

        return text

    # ------------------------------------------------------
    # General Chat
    # ------------------------------------------------------

    @staticmethod
    def chat(message, detailed=False):

        if detailed:

            style = """
Provide a detailed explanation.

Use headings and bullet points.

Maximum 300 words.
"""

        else:

            style = """
Give a short answer.

Maximum 70 words.

Simple English.

Only explain what is asked.
"""

        prompt = f"""

You are MediMind AI.

You are an educational healthcare assistant.

Do not diagnose diseases.

Do not prescribe medicines.

If the question is medical,
recommend consulting a doctor.

{style}

Question:

{message}

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Medicine Explanation
    # ------------------------------------------------------

    @staticmethod
    def explain_medicine(

        medicine_name,

        dosage="",

        food_instruction=""

    ):

        prompt = f"""

You are MediMind AI.

Explain the medicine.

Medicine

{medicine_name}

Dosage

{dosage}

Food Instruction

{food_instruction}

Rules

Keep answer short.

Use headings.

Purpose

How to Take

Common Side Effects

Precautions

Missed Dose

Storage

Maximum 200 words.

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Medicine Interaction
    # ------------------------------------------------------

    @staticmethod
    def medicine_interaction(

        medicine1,

        medicine2

    ):

        prompt = f"""

Can these medicines be taken together?

Medicine 1

{medicine1}

Medicine 2

{medicine2}

Return

Interaction

Risk

Recommendation

Maximum 120 words.

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Health Tips
    # ------------------------------------------------------

    @staticmethod
    def health_tips(

        water,

        sleep,

        bmi,

        score

    ):

        prompt = f"""

Generate health tips.

Water

{water}

Sleep

{sleep}

BMI

{bmi}

Health Score

{score}

Give only 5 bullets.

Simple English.

"""

        return MedicineAI._generate(prompt)
    # ------------------------------------------------------
    # Prescription Extraction
    # ------------------------------------------------------

    @staticmethod
    def extract_prescription(text):

        prompt = f"""

You are MediMind AI.

The following text was extracted from a prescription.

{text}

Extract ALL medicines.

Return ONLY valid JSON.

Example

[
{{
"medicine_name":"Paracetamol",
"dosage":"650 mg",
"frequency":"Twice Daily",
"food_instruction":"After Food",
"notes":"5 Days"
}}
]

Rules

Return ONLY JSON.

No explanation.

Leave missing values blank.

"""

        response = MedicineAI._generate(prompt)

        response = MedicineAI._clean_json(response)

        try:

            return json.loads(response)

        except Exception:

            return []

    # ------------------------------------------------------
    # Medicine Summary
    # ------------------------------------------------------

    @staticmethod
    def medicine_summary(medicine):

        prompt = f"""

Summarize

{medicine}

Very simple English.

Maximum 50 words.

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Side Effects
    # ------------------------------------------------------

    @staticmethod
    def side_effects(medicine):

        prompt = f"""

List common side effects of

{medicine}

Use bullets.

Maximum 6 bullets.

Do not include rare side effects.

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Food Interaction
    # ------------------------------------------------------

    @staticmethod
    def food_interaction(medicine):

        prompt = f"""

Medicine

{medicine}

Can it be taken

Before Food

After Food

With Milk

With Alcohol

Return as a small table.

Maximum 120 words.

"""

        return MedicineAI._generate(prompt)

    # ------------------------------------------------------
    # Reminder Message
    # ------------------------------------------------------

    @staticmethod
    def reminder_message(medicine):

        return f"""

💊 Medicine Reminder

It's time to take

{medicine}

Stay healthy ❤️

"""

    # ------------------------------------------------------
    # Health Score Interpretation
    # ------------------------------------------------------

    @staticmethod
    def health_score(score):

        if score >= 90:

            return "Excellent health adherence."

        elif score >= 75:

            return "Very good. Keep it up."

        elif score >= 60:

            return "Fair. Improve your routine."

        elif score >= 40:

            return "Below average. Follow your schedule carefully."

        return "Poor adherence. Please take care of your health."

    # ------------------------------------------------------
    # Clean OCR Text
    # ------------------------------------------------------

    @staticmethod
    def clean_ocr_text(text):

        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"[^\w\s\.,:/()-]", "", text)

        return text.strip()

    # ------------------------------------------------------
    # Validate Medicine JSON
    # ------------------------------------------------------

    @staticmethod
    def validate_medicine(data):

        if isinstance(data, list):

            return data

        if isinstance(data, dict):

            return [data]

        return []

    # ------------------------------------------------------
    # AI Status
    # ------------------------------------------------------

    @staticmethod
    def status():

        return {

            "model": MedicineAI.MODEL,

            "provider": "Google Gemini",

            "status": "Running"

        }