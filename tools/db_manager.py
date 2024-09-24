import sqlite3
import yaml

class DatabaseManager:
	def __init__(self, db_path):
		self.connection = sqlite3.connect(db_path)
		self.cursor = self.connection.cursor()

		# Load configuration
		with open("config.yaml", "r") as config_file:
			self._config = yaml.safe_load(config_file)

	def create_table(self):
		self.cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS token_usage (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
				model TEXT,
				prompt_tokens INTEGER,
				completion_tokens INTEGER
			)
			"""
		)
		self.connection.commit()

	def log_token_usage(
		self,
		res
	):
		model = self._config["model"]
		usage = res.usage

		self.cursor.execute(
			"""
			INSERT INTO token_usage (model, prompt_tokens, completion_tokens)
			VALUES (?, ?, ?)
			""",
			(
				model,
				usage.prompt_tokens,
				usage.completion_tokens
			)
		)
		self.connection.commit()

	def get_token_usage(self):
		self.cursor.execute(
			"""
			SELECT * FROM token_usage
			"""
		)
		return self.cursor.fetchall()

	def close(self):
		self.connection.close()

	def print_token_usages(
		self,
		n_last_usages: int = 10
	):
		"""Print the last n token usage entries from the database"""
		try:
			cursor = self.connection.cursor()
			cursor.execute(
				"""
				SELECT * FROM token_usage
				ORDER BY timestamp DESC
				LIMIT ?
				""",
				(n_last_usages,)
			)
			rows = cursor.fetchall()
			print(f"Last {n_last_usages} token usage entries {'='*5}:")
			for row in rows:
				print(f"\tID: {row[0]}")
				print(f"\tTimestamp: {row[1]}")
				print(f"\tModel: {row[2]}")
				print(f"\tPrompt tokens: {row[3]}")
				print(f"\tCompletion tokens: {row[4]}")
				print("-----")
		except sqlite3.Error as e:
			print(f"Error retrieving token usage: {e}")
			
	def print_cummulative_token_usage(self):
		self.cursor.execute(
			"""
			SELECT model, SUM(prompt_tokens) AS total_prompt_tokens, SUM(completion_tokens) AS total_completion_tokens
			FROM token_usage
			GROUP BY model
			"""
		)
		
		rows = self.cursor.fetchall()
		print("Cummulative token usage:")
		for row in rows:
			print(f"\tModel: {row[0]}")
			print(f"\tTotal prompt tokens: {row[1]}")
			print(f"\tTotal completion tokens: {row[2]}")
			print("-----")