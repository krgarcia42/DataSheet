import sqlite3

DEFAULT_DB = "production.db"

def execute_query(query):
  conn = sqlite3.connect(DEFAULT_DB)
  cursor = conn.cursor()

  print(f"Executing: {query}")
  cursor.execute(query)

  return cursor.fetchall()

if __name__ == "__main__":
  rows = execute_query("SELECT * FROM users")
  print(rows)
