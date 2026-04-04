from google import genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"

def ask_gemini_to_sql(user_prompt, schema):
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # NOTICE: We added 'models/' to the front. 
        # This tells the API exactly where to look, bypassing the 404.
        response = client.models.generate_content(
            model="models/gemini-1.5-flash", 
            contents=prompt
        )
        
        sql_output = response.text.strip()
        # Clean up any potential markdown the AI might include
        return sql_output.replace("```sql", "").replace("```", "").strip()
        
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
