import os
import sqlite3
from ingestor import load_csv_to_db
from schema_manager import create_user_table

def test_database_creation():
    #check if db file exists after running loader
    db_name = "test.db"
    #delete old db if exists
    if os.path.exists(db_name):
        os.remove(db_name)
        
    create_user_table(db_name)
    load_csv_to_db("data.csv", "users", db_name)

    #check if file exists
    assert os.path.exists(db_name) == True

    #check if data is inside file
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()

    assert count > 0
