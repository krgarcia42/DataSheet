import pandas as pd
import sqlite3

def load_csv_to_db(csv_path, table_name, db_path):
  # read the csv file
  df = pd.read_csv(csv_path)
