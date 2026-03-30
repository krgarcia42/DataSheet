import os
from schema_manager import create_user_table
from ingestor import load_csv_to_db

def run_pipeline():
  db_name = "production.db"
  csv_file = "data.csv"

  print("starting pipeline")
  
  #create the structure
  print("1. setting up schema")
  create_user_table(db_name)

  #load data
  print("2. ingesting csv data")
  load_csv_to_db(csv_file, "users", db_name)

  print("pipeline completed")

if __name__ == "__main__":
  run_pipeline()
