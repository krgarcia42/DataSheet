from .database_manager import execute_query

def initialize_db():
  #only create structure for SQlite
  create_table_query = """
  CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    );
    """
  execute_query(create_table_query)
  print("Schema Initialized")

if __name__ == "__main__":
  initialize_db()
