from my_project.query_service import validate_and_execute

def test_validator_blocks_delete():
  #AI mistakenly includes a DELETE statement
  malicious_sql = "SELECT * FROM users; DELETE FROM users"
  result = validate_and_execute(malicious_sql)
  #should fail
  assert "Error" in result

