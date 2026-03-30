import schema_manager
import ingestor

def run_pipeline():
  csv_file = "data.csv"
  db_name = "production.db"

  print("begin...")

  create_user_table(db_name)

  ingestor.load_csv_to_db(csv_file, "users", db_name)

if __name__ == "__main__":
  run_pipeline()
