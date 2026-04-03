from schema_manager import initialize_db
from query_service import get_all_users
from llm_adaptor import ask_gemini_to_summarize

def run_pipeline():
  print("1. Initializing Database")
  initialize_db()

  print("2. Fetching User Data")
  users = get_all_users()

  if not users:
    print("No users found. Pipeline stopping")
    return

  print("3. Sending to Gemini")
  summary = ask_gemini_to_summarize(users)

  print("Final Summary")
  print(summary)

if __name__ == "__main__":
  run_pipeline()
