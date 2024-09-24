"""
02_log_token_usage.py
2024-09-24, Johannes Köppern

Log the token usage of every OpenAI chat completion in sqlite3 database:
Table token_usage:
- id INTEGER PRIMARY KEY AUTOINCREMENT
- timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
- model TEXT
- prompt_tokens INTEGER
- completion_tokens INTEGER
"""
import yaml
from tools.tools import Tools


## Application
tools = Tools()

tools.init_tools()

res = tools.chat_completion(
	messages=[{"role": "user", "content": "Hello! How are you?"}],
	use_cache=False
)

print(res)

tools.print_cummulative_token_usage()
