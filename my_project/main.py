from schema_manager import initialize_db
from ingestor import ingest_data
from query_service import get_all_users
from llm_adaptor import ask_gemini_to_summarize

def run_pipeline():
  #set up SQLite
  print("1. Initializing Database")
  initialize_db()

  #ingest with pandas
  print("2. Ingesting Data")
  ingest_data("my_project/data.csv")

  print("3. Fetching User Data")
  users = get_all_users()

  if not users:
    print("No users found. Pipeline stopping")
    return

  print("4. Sending to Gemini")
  summary = ask_gemini_to_summarize(users)

  print("Final Summary")
  print(summary)

if __name__ == "__main__":
  run_pipeline()
