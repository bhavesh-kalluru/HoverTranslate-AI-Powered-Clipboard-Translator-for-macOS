import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(message, source_lang, target_lang):
    prompt = f"""
You are a professional translator AI fluent in all human languages. Translate the following message from {source_lang} to {target_lang}.
- Preserve meaning, tone, and style (formal/informal).
- Maintain emoji and formatting.
- If the source language is unknown, auto-detect it.
- Provide a natural-sounding translation, not a literal one.

Text:
\"\"\"{message}\"\"\"
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()
