from google import genai

API_KEY = "AIzaSyALcW5U8S9J4T-tbVR6Pr1s7kheFu9CfyM"
def ask_gemini_to_sql(user_prompt, schema):
    # FORCE v1 (Production)
    client = genai.Client(
        api_key=API_KEY,
        http_options={'api_version': 'v1'}
    )
    
    prompt = f"Given schema: {schema}, write a SQLite query for: {user_prompt}. Return ONLY SQL."

    try:
        # 2026 STABLE NAME: The '-preview' suffix is gone for production v1
        # We use 'gemini-3-flash' which is the current workhorse
        response = client.models.generate_content(
            model="gemini-3-flash", 
            contents=prompt
        )
        return response.text.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        # If 'gemini-3-flash' is still propagating, try the latest alias
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            return response.text.replace("```sql", "").replace("```", "").strip()
        except:
            print(f"DEBUG: Gemini Error: {e}")
            return "SELECT * FROM users"
