import os
import json
import requests
import google.generativeai as genai
from faker import Faker


def generate_ai_article_data():
    fake = Faker()

    try:
        wiki_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        wiki_response = requests.get(wiki_url, timeout=5)
        wiki_response.raise_for_status()
        wiki_data = wiki_response.json()

        title = wiki_data.get("title", fake.sentence())
        body = wiki_data.get("extract", fake.paragraph())

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        Analyze this text and generate a short, one-sentence summary for an 'about' field, 
        and exactly 3 single-word tags relevant to the text.

        Text: {body}

        You must respond ONLY with a valid JSON object matching this exact schema:
        {{
            "about": "string",
            "tags": ["string", "string", "string"]
        }}
        """

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                temperature=0.2
            )
        )

        gemini_data = json.loads(response.text)

        return {
            "title": title,
            "about": gemini_data.get("about"),
            "body": body,
            "tags": gemini_data.get("tags")
        }

    except Exception as e:
        print(f"API pipeline failed: {e}. Falling back to Faker.")
        return {
            "title": fake.sentence(),
            "about": fake.sentence(nb_words=6),
            "body": fake.paragraph(nb_sentences=5),
            "tags": [fake.word(), fake.word(), fake.word()]
        }