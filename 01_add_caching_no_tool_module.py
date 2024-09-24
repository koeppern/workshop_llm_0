"""
01_add_caching.py
2024-09-24, Johannes Köppern

- adds caching to the chat completion
- uses cache to avoid duplicate calls
"""
import os
import hashlib
import json
import yaml

from dotenv import load_dotenv
from openai import OpenAI
from diskcache import Cache


## Load configuration
with open("config.yaml", "r") as config_file:
	config = yaml.safe_load(config_file)

model = config["model"]
temperature = config["temperature"]
cache_path = config["cache_path"]

## Functions
def chat_completion(
	messages: list[dict],
	cache: Cache,
	client: OpenAI,
	use_cache: bool = True
) -> str:
	# Convert messages to a JSON string and then hash it
	messages_json = json.dumps(messages, sort_keys=True)
	this_hash = hashlib.sha256(messages_json.encode()).hexdigest()

	if use_cache:
		hashed_result = cache.get(this_hash)
		if hashed_result:
			print("Using cached response")
			return hashed_result

	print("Calling OpenAI")

	response = client.chat.completions.create(
		model=model,
		messages=messages,
		temperature=temperature,
	)

	res = response.choices[0].message.content

	if use_cache:
		cache.set(this_hash, res)

	return res

## Application


cache = Cache(cache_path)

# Clear cache
cache.clear()

messages = [
	{"role": "system", "content": "You are a helpful assistant."},
	{"role": "user", "content": "Hello, how are you?"},
]

print(chat_completion(
	messages=messages,
	cache=cache,
	client=client,
	use_cache=False
))

print(chat_completion(
	messages=messages,
	cache=cache,
	client=client,
	use_cache=True
))

print(chat_completion(
	messages=messages,
	cache=cache,
	client=client,
	use_cache=True
))
