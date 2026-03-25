import os
from my_project/ingestor import load_csv_to_db

def test_database_creation():
    #check if db file exists after running loader
    db_name = "test.db"
    if os.path.exists(db_name):
        os.remove(db_name)
        
    load_csv_to_db("data.csv", "users", db_name)
  
    assert os.path.exists(db_name) == True
