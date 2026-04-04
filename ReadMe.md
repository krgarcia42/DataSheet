# DataSheet: AI-Powered SQL Query Interface

## System Overview
DataSheet is a secure, modular Python application that allows users to query structured CSV data using natural language or raw SQL. The system is decoupled, ensuring the LLM acts only as a translation layer, while the core system maintains strict control over database execution.

### Key Components:
* **Ingestion & Schema:** `ingestor.py` uses Pandas to load `data.csv` into a SQLite database, while `schema_manager.py` defines the table structure.
* **LLM Adaptor:** `llm_adaptor.py` utilizes Google Gemini API to translate user prompts into SQL. It uses prompt engineering to provide the AI with schema context, ensuring more accurate code generation.
* **Query Service (Security Validator):** `query_service.py` treats all LLM output as an untrusted input. It performs a two-step validation:
    1.  **Command Restriction:** Only `SELECT` queries are permitted.
    2.  **Table Whitelisting:** Queries are strictly limited to the `users` table to prevent hallucinations or unauthorized data access.
* **Database Manager:** `database_manager.py` handles the final connection and execution of validated SQL queries.

---

## How to Run the Project

### 1. Installation
Ensure you have Python 3.10+ installed. Install the necessary libraries:
```bash
pip install pandas google-generativeai pytest
```

### 2. API Configuration
1.  Obtain a Gemini API Key from [Google AI Studio](https://aistudio.google.com/) or use the current one.
2.  Replace the value of `API_KEY` on Line 3 of `my_project/llm_adaptor.py` with your actual key if needed.

### 3. Running the Application
Launch the program from the root directory using the module flag:
```bash
python -m my_project.main
```
* **Option 1 (Run SQL):** Directly execute SQL statements against the `users` table.
* **Option 2 (Ask AI):** Type a natural language question (e.g., *"Who lives in New York?"*). The system will show you the AI-suggested SQL before displaying the validated results.
* * **Option 3 (Exit)**

---

## How to Run Tests
The project uses `pytest` to ensure that the security validator cannot be bypassed by incorrect or malicious LLM output.

### Run Local Tests
From the root directory, run:
```bash
pytest tests/test_validator.py
```

### Automated Testing (CI/CD)
This project uses **GitHub Actions** to run the test suite automatically on every push. 
* **`test_validator_blocks_malicious_sql`**: Confirms that "piggybacked" commands like `DELETE` are blocked.
* **`test_validator_blocks_wrong_table`**: Verifies that if the LLM hallucinates a table name (e.g., `employees`), the system rejects the query.
* **`test_validator_allows_good_sql`**: Ensures that valid queries return the expected data format (a list of results).
