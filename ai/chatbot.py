from google import genai
from config import Config

client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


def ask_ai(question):

    question = question.strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "good afternoon"
    ]

    if question.lower() in greetings:
        return "Hello 👋 I'm MediMind AI. How can I help you today?"

    if question.lower() in ["thanks", "thank you", "ok"]:
        return "You're welcome 😊 Stay healthy!"

    detailed_keywords = [
        "explain",
        "detail",
        "detailed",
        "how",
        "why",
        "difference",
        "compare",
        "advantages",
        "disadvantages",
        "benefits",
        "causes",
        "full"
    ]

    detailed = any(
        word in question.lower()
        for word in detailed_keywords
    )

    if detailed:

        instruction = """
You are MediMind AI.

Give a detailed answer.

Use headings.

Use bullet points.

Explain in simple English.

End with one useful health tip.
"""

    else:

        instruction = """
You are MediMind AI.

Answer in SIMPLE English.

Maximum 60 words.

Maximum 3 short sentences.

Do not write long paragraphs.

Be direct.

Be friendly.

Only answer what the user asked.
"""

    prompt = f"""

{instruction}

You are an AI Health Assistant.

Never diagnose diseases.

Never prescribe medicines.

If the user has emergency symptoms,
tell them to consult a doctor.

Question:

{question}

"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error : {e}"