from database_manager import execute_query

def get_all_users():
  query = "SELECT * from users"

  #1. execute query
  rows = execute_query(query)

  if rows:
    print(f"--- Query Service: Found {len(rows)} users ---")
  else:
    print("--- Query Service: No users found in database ---")

  #2. return rows to main.py
  return rows
  
if __name__ == "__main__":
  data = get_all_users()
  print(data)
