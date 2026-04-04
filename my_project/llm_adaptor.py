from google import genai

API_KEY = "AIzaSyALcW5U8S9J4T-tbVR6Pr1s7kheFu9CfyM"

def ask_gemini_to_sql(user_prompt, schema):
    client = genai.Client(
        api_key=API_KEY,
        http_options={'api_version': 'v1'}
    )
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # ADDING 'models/' BEFORE THE NAME
        response = client.models.generate_content(
            model="models/gemini-1.5-pro", 
            contents=prompt
        )
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users"
