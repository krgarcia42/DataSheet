from google import genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"

def ask_gemini_to_sql(user_prompt, schema):
    # This force-switches you from the 'beta' that is crashing to 'v1'
    client = genai.Client(
        api_key=API_KEY,
        http_options={'api_version': 'v1'}
    )
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # Use 'gemini-1.5-flash' - it is the most compatible with 'v1'
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
