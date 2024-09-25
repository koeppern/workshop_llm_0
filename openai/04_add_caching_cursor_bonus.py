"""
04_add_caching_cursor_bonus.py
2024-09-24, Johannes Köppern

- adds caching to the chat completion
- uses cache to avoid duplicate calls
"""
from tools.tools import Tools

## Application
tools = Tools()

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
