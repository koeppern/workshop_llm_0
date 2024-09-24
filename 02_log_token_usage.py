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
import os

from openai import OpenAI
from dotenv import load_dotenv
from db_manager import DatabaseManager


## Parameters
model = "gpt-3.5-turbo"

## Application
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
	api_key=api_key
)

db_manager = DatabaseManager("token_usage.db")

db_manager.create_table()

res = client.chat.completions.create(
	model=model,
	messages=[{"role": "user", "content": "Hello! How are you?"}],
	temperature=1
)

print(res.choices[0].message.content)

db_manager.log_token_usage(res)

# db_manager.print_token_usages()

db_manager.print_cummulative_token_usage()
