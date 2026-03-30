import sqlite3

DB_PATH = "production.db"

def execute_query(query):
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  print(f"Executing: {query}")
  cursor.execute(query)
  conn.commit()

  results = cursor.fetchall()
  conn.close()
  return results

if __name__ == "__main__":
  data = execute_query("SELECT * FROM users")
  print(f"Manager found: {data}")
