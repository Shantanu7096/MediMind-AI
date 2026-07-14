import json
import os
from PIL import Image
from google import genai
from config import Config

client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


class GeminiVision:

    @staticmethod
    def extract_prescription(image_path):

        try:

            image = Image.open(image_path)

            prompt = """
You are an expert medical prescription reader.

Read the prescription image carefully.

Extract ALL medicines.

Return ONLY valid JSON.

Example:

[
{
    "medicine_name":"Paracetamol",
    "dosage":"650 mg",
    "frequency":"Twice Daily",
    "food_instruction":"After Food",
    "notes":"5 Days"
},
{
    "medicine_name":"Vitamin D3",
    "dosage":"60000 IU",
    "frequency":"Once Weekly",
    "food_instruction":"After Food",
    "notes":"8 Weeks"
}
]

Rules:

1. Return ONLY JSON.
2. No markdown.
3. No explanation.
4. Leave missing values empty.
5. Ignore doctor's name and clinic details.
6. Ignore patient information.
7. Ignore signatures.
8. Extract medicines only.
"""

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=[
                    prompt,
                    image
                ]

            )

            text = response.text.strip()

            text = text.replace("```json", "")
            text = text.replace("```", "")

            return json.loads(text)

        except Exception:

            return []