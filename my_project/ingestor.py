import pandas as pd
import sqlite3

def load_csv_to_db(csv_path, table_name, db_path):
  # read the csv file
  df = pd.read_csv(csv_path)

  # connect to database
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()

  #create the table
  cols = ", ".join([f"{c} TEXT" for c in df.columns])
  cursor.execute(f"CREATE TABLE {table_name} ({cols})")

  #loop and insert
  for index, row in df.iterrows():
    placeholders = ", ".join(["?"] * len(row))
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(row))

  #close
  conn.close()
  print: 'done'
