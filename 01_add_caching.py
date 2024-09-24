"""
01_add_caching.py
2024-09-24, Johannes Köppern

- adds caching to the chat completion
- uses cache to avoid duplicate calls
"""
import yaml
from tools.tools import Tools

## Load configuration
with open("config.yaml", "r") as config_file:
	config = yaml.safe_load(config_file)

## Application
tools = Tools(config)

tools.init_tools()

messages = [
	{"role": "system", "content": "You are a helpful assistant."},
	{"role": "user", "content": "Hello, how are you?"},
]

print(tools.chat_completion(
	messages=messages,
	use_cache=False
))

print(tools.chat_completion(
	messages=messages,
	use_cache=True
))

print(tools.chat_completion(
	messages=messages,
	use_cache=True
))
