import json
import re

from ai.medicine_ai import MedicineAI


DEFAULT_MEDICINE = {
    "medicine_name": "",
    "manufacturer": "",
    "generic_name": "",
    "dosage": "",
    "frequency": "",
    "food_instruction": "",
    "pack_size": "",
    "expiry": "",
    "notes": "",
    "confidence": 0
}


def clean_text(text):

    if not text:
        return ""

    text = text.replace("\r", " ")
    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_json(text):

    if not text:
        return None

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:

        try:

            return json.loads(
                text[start:end + 1]
            )

        except:

            pass

    start = text.find("[")
    end = text.rfind("]")

    if start != -1 and end != -1:

        try:

            data = json.loads(
                text[start:end + 1]
            )

            if isinstance(data, list):

                if len(data) > 0:

                    return data[0]

        except:

            pass

    return None


def parse_medicine(ocr_text):

    medicine = DEFAULT_MEDICINE.copy()

    ocr_text = clean_text(ocr_text)

    if ocr_text == "":

        medicine["notes"] = "No text detected."

        return medicine

    prompt = f"""

You are MediMind AI.

Read the following OCR text carefully.

OCR TEXT

{ocr_text}

Extract ONLY ONE medicine.

Return ONLY JSON.

Format

{{
    "medicine_name":"",
    "manufacturer":"",
    "generic_name":"",
    "dosage":"",
    "frequency":"",
    "food_instruction":"",
    "pack_size":"",
    "expiry":"",
    "notes":"",
    "confidence":95
}}

Rules

1 Return ONLY JSON.

2 No markdown.

3 No explanation.

4 Confidence should be between 0 and 100.

5 If information is missing, leave it blank.

"""

    response = MedicineAI._generate(
        prompt
    )

    data = extract_json(
        response
    )

    if data is None:

        medicine["notes"] = "AI could not understand the prescription."

        return medicine

    for key in medicine.keys():

        if key in data:

            medicine[key] = data[key]

    try:

        medicine["confidence"] = int(
            medicine["confidence"]
        )

    except:

        medicine["confidence"] = 0

    return medicine


def parse_multiple_medicines(ocr_text):

    ocr_text = clean_text(ocr_text)

    prompt = f"""

You are MediMind AI.

Extract ALL medicines from this OCR text.

OCR

{ocr_text}

Return ONLY JSON.

Example

[
{{
"medicine_name":"Paracetamol",
"dosage":"650 mg",
"frequency":"Twice Daily",
"food_instruction":"After Food",
"notes":"5 Days"
}},
{{
"medicine_name":"Vitamin D3",
"dosage":"60000 IU",
"frequency":"Weekly",
"food_instruction":"After Food",
"notes":"8 Weeks"
}}
]

Return ONLY JSON.

"""

    response = MedicineAI._generate(
        prompt
    )

    response = response.replace(
        "```json",
        ""
    )

    response = response.replace(
        "```",
        ""
    )

    try:

        medicines = json.loads(
            response
        )

        if isinstance(
            medicines,
            list
        ):

            return medicines

    except:

        pass

    return []


def parser_status():

    return {

        "status": "Running",

        "version": "2.0",

        "parser": "Gemini AI",

        "supports": [

            "EasyOCR",

            "Gemini Vision"

        ]

    }