from my_project.query_service import validate_and_execute
from my_project.schema_manager import initialize_db
from my_project.ingestor import ingest_data

def test_validator_blocks_malicious_sql():
  #LLM mistakenly includes a DELETE statement
  malicious_sql = "SELECT * FROM users; DELETE FROM users"
  result = validate_and_execute(malicious_sql)
  #should fail
  assert "Error" in result

def test_validator_blocks_wrong_table():
  #LLM hallucinates a table name such as 'employees'
  hallucinated_sql = "SELECT * FROM employees"
  result = validate_and_execute(hallucinated_sql)
  assert "unknown table" in result.lower()

def test_validator_allows_good_sql():
  initialize_db()
  ingest_data("my_project/data.csv")
  #legitimate LLM-created sql
  good_sql = "SELECT name, age FROM users WHERE age > 25"
  result = validate_and_execute(good_sql)
  #should return data rather than error
  assert isinstance(result, list)
