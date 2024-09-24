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
from tools.db_manager import DatabaseManager


## Load configuration
with open("config.yaml", "r") as config_file:
	config = yaml.safe_load(config_file)

db_path = config["db_path"]

## Application
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
	api_key=api_key
)

db_manager = DatabaseManager(db_path)

db_manager.create_table()

res = client.chat.completions.create(
	model=config["model"],
	messages=[{"role": "user", "content": "Hello! How are you?"}],
	temperature=1
)

print(res.choices[0].message.content)

db_manager.log_token_usage(res)

# db_manager.print_token_usages()

db_manager.print_cummulative_token_usage()
