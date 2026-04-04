from google import genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"

def ask_gemini_to_sql(user_prompt, schema):
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # The new library uses 'gemini-1.5-flash'
        response = client.models.generate_content(
            model="gemini-pro", 
            contents=prompt
        )
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
