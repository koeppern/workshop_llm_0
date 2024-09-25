"""
0_getting_started.py
2024-09-24, Johannes Köppern

A simple script to get started with OpenAI API.
"""
import os
import yaml

from openai import OpenAI
from dotenv import load_dotenv

## Load configuration
with open("config.yaml", "r") as config_file:
	config = yaml.safe_load(config_file)

model = config["model"]

## Application
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
	api_key=api_key
)

response = client.chat.completions.create(
	model=model,
	messages=[{"role": "user", "content": "Hello! How are you?"}],
	temperature=1
)

print(response.choices[0].message.content)

