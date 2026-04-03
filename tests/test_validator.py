from my_project.query_service import validate_and_execute

def test_validator_blocks_delete():
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

