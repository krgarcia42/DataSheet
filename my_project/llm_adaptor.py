import google.generativeai as genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"
genai.configure(api_key = API_KEY)

def ask_gemini_to_sql(user_prompt, schema):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    You are an SQL generator. Given the schema: {schema}
    translate the following request into an SQLite SELECT statement.
    Return ONLY the SQL code, no explanation.

    Request: {user_prompt}
    """

    try:
        response = model.generate_content(prompt)
        # clean output
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        return "SELECT * FROM users" # fallback
