import pandas as pd
from my_project.database_manager import execute_query

def ingest_data(file_path):
  print("Ingesting data from {file_path}")

  execute_query("DELETE FROM users")

  try:
    #read external CSV
    df = pd.read_csv(file_path)
    #iterate through df
    for index, row in df.iterrows():
      query = f"INSERT INTO users (name, age, city) VALUES ('{row['name']}', {row['age']}, '{row['city']}')"
      execute_query(query)
    print("Succesfully ingested {len(df)} rows")

  except Exception as e:
    print("Error during ingestion: {e}")

if __name__ = "__main__":
  #test
  ingest_data("my_project/data.csv")
