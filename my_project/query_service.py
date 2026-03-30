import sqlite3

def get_all_users(db_path):
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()

  #query to grab everything
  cursor.execute("SELECT * FROM users")
  rows = cursor.fetchall()

  print(f"Found {len(rows)} users")
  for row in rows:
    name, age, city = row
    print(f"User: {name} | Age: {age} | City: {city}")

  conn.close()

if __name__ == "__main__":
  get_all_users("production.db")
