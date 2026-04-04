import google.generativeai as genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"
genai.configure(api_key = API_KEY)

def ask_gemini_to_sql(user_prompt, schema):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Given the schema {schema}, write a SQLite query for: {user_prompt}. Return only SQL."

    try:
        response = model.generate_content(prompt)
        # clean output
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
