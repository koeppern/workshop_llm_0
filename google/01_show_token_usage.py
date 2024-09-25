"""
01_show_token_usage.py
2024-09-24, Johannes Köppern

- Based on 0_getting_started.py
- Show token usage
"""
import os
from dotenv import load_dotenv

import google.generativeai as genai


## Functions
# Use usage_metadata to get token count
def print_token_usage(response):
	usage = response.usage_metadata

	prompt_tokens = usage.prompt_token_count

	output_tokens = usage.candidates_token_count

	total_tokens = usage.total_token_count

	print(f"Prompt tokens (via usage_metadata): {prompt_tokens}")

	print(f"Completion tokens (via usage_metadata): {output_tokens}")

	print(f"Total tokens (via usage_metadata): {total_tokens}")


## Main
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt
prompt = "Write a story about a magic backpack."

# Count tokens in the input
prompt_token_count = model.count_tokens(prompt)
print(f"Prompt tokens: {prompt_token_count}")

# Generate content with configuration options
response = model.generate_content(
	prompt,
	generation_config = genai.GenerationConfig(
		max_output_tokens=1000,
		temperature=0.1,
	)
)

# Output the generated text
print(f"\n{'-'*100}\n{response.text}\n{'-'*100}")

# Print token usage
print_token_usage(response)