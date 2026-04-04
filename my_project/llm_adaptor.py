from google import genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"

def ask_gemini_to_sql(user_prompt, schema):
    # We pass the API_KEY directly into the Client here
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # Notice the new 'client.models.generate_content' syntax
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
