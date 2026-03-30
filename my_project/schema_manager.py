import sqlite3

def create_user_table(db_path):
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  #manually input from data.csv
  cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, city TEXT)")

  conn.commit()
  conn.close()
  print("Schema created successfully")

if __name__ = "__main__":
  create_user_table("test.db")
