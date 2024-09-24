"""
0_getting_started.py
2024-09-24, Johannes Köppern

- loads .env file to get OPENAI_API_KEY
- Instanciates OpenAI client
- creates initial chat completion for 
  - system message: you are a helpful assistant
      - user message: Hello, how are you?

Virtual environment:
- python -m venv .venv      
- .venv\Scripts\activate
- pip install -r requirements.txt
"""
import os

from dotenv import load_dotenv
from openai import OpenAI


## Parameters
model = "gpt-3.5-turbo"

temperature = 0.5


## Application
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hello, how are you?"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
)

# Print result
print("Model: ", model)
print("Temperature: ", temperature)

print(f"Prompt {'='*5}: {messages}")

print(f"Response {'='*5}: {response.choices[0].message.content}")

print(f"Token usage {'='*5}: {response.usage}")

