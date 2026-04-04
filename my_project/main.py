from .schema_manager import initialize_db
from .ingestor import ingest_data
from .query_service import validate_and_execute, get_table_schema
from .llm_adaptor import ask_gemini_to_sql

def run_pipeline():
  #set up SQLite
  print("1. Initializing Database")
  initialize_db()

  #ingest with pandas
  print("2. Ingesting Data")
  ingest_data("data.csv")

  while True:
    print("\nOptions: [1] Run SQL  [2] Ask AI  [3] Exit")
    choice = input("Select an option: ")

    if choice == "1":
      sql = input("Enter SQL query: ")
      results = validate_and_execute(sql)
      print(f"Results: {results}")

    elif choice == "2":
      user_prompt = input("What do you want to know? ")
      #LLM Adaptor translates prompt to SQL
      schema = get_table_schema()
      generated_sql = ask_gemini_to_sql(user_prompt, schema)
      print(f"AI suggested SQL: {generated_sql}")

      #LLM output must be validated
      results = validate_and_execute(generated_sql)
      print(f"AI Results: {results}")

    elif choice == "3":
      break

if __name__ == "__main__":
  run_pipeline()
