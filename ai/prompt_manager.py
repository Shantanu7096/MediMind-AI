class PromptManager:

    @staticmethod
    def medicine_parser(ocr_text):

        return f"""
You are an AI Medicine Information Extractor.

You will receive OCR text extracted from
medicine strips or doctor's prescriptions.

Your task is:

1. Ignore meaningless OCR words.
2. Correct OCR spelling mistakes.
3. Detect medicine names.
4. Detect dosage.
5. Detect manufacturer.
6. Detect pack size.
7. Detect frequency if available.
8. Detect food instruction.
9. Detect expiry if available.
10. Return ONLY JSON.

If information is unavailable,
return an empty string.

OCR TEXT:

{ocr_text}

Return exactly this JSON format:

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
    "confidence":0
}}

Do not return markdown.
Do not explain anything.
Return only JSON.
"""