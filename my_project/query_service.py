from my_project.database_manager import execute_query

def validate_and_execute(sql_query):
  if not sql_query.strip().upper().startswith("SELECT"):
    return "Error: Only SELECT queries allowed for security"

  if "users" not in sql_query.lower():
    return "Error: Query references an unknown table"

  try:
    rows = execute_query(sql_query)
    return rows
  except Exception as e:
    return f"SQL Error: {e}"

def get_table_schema():
  #needed for the LLM Adapter
  return "Table: users (columns: name, age, city)"
