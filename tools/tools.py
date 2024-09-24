"""
Various tools for chat completion workshop
2024-09-24, Johannes Köppern
"""
# NEVER add newlines between imports, but group by python, installed packages, own packages
import os
import json
import hashlib
import yaml

from openai import OpenAI
from dotenv import load_dotenv
from diskcache import Cache

from tools.db_manager import DatabaseManager


## Functions and classes
class Tools:

	def __init__(
		self,
		config
	):
		self._config = config

		load_dotenv()

		self._db_path = self._config["db_path"]

		self._cache_path = self._config["cache_path"]

	def init_tools(self):
		self._openai_api_key = os.getenv("OPENAI_API_KEY")

		self._client = OpenAI(
			api_key=self._openai_api_key
		)

		self._cache = Cache(self._cache_path)

		self._db_manager = DatabaseManager(self._db_path, self._config)

	def chat_completion(
		self,
		messages,
		use_cache=True
	):
		model = self._config["model"]
		temperature = self._config["temperature"]

		# hash messages converting to json string and using hashlib
		messages_str = json.dumps(messages)

		this_hash = hashlib.sha256(messages_str.encode()).hexdigest()

		if use_cache:
			cached_response = self._cache.get(this_hash)

			if cached_response:
				return cached_response

		response = self._client.chat.completions.create(
			messages=messages,
			model=model,
			temperature=temperature
		)

		# log token usage
		self._db_manager.log_token_usage(response)

		response_str = response.choices[0].message.content
		# if use_cache is True, cache the response
		if use_cache:
			self._cache.set(this_hash, response_str)

		return response_str

	def print_token_usage(self):
		self._db_manager.print_token_usage()

	def print_cummulative_token_usage(self):
		self._db_manager.print_cummulative_token_usage()


if __name__ == "__main__":
	with open("config.yaml", "r") as config_file:
		config = yaml.safe_load(config_file)

	tools = Tools(config)

	tools.init_tools()

	tools.print_cummulative_token_usage()

	res = tools.chat_completion(
		messages=[{"role": "user", "content": "Hello! How are you?"}]
	)

	print(res)

	tools.print_cummulative_token_usage()
