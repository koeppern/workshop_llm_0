"""
0_getting_started.py
2024-09-24, Johannes Köppern

- Get Google API Key: https://ai.google.dev/gemini-api/docs/quickstart?hl=de&lang=python
- Google chat completion: 
"""
import os
from dotenv import load_dotenv

import google.generativeai as genai


load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Write a story about a magic backpack.",
    generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1,
    )
)

print(response.text)
