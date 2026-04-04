import google.generativeai as genai

API_KEY = "AIzaSyBgQHfDCG1iIxUENF9jyupSAyLUFqjcwDc"
# FORCE STABLE CONFIGURATION
genai.configure(api_key=API_KEY)

def ask_gemini_to_sql(user_prompt, schema):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    prompt = f"""
    You are an SQL generator. 
    Schema: {schema}
    Request: {user_prompt}
    
    Return only the SQL code. No markdown. No explanation.
    """

    try:
        # specify the model name again here to be safe
        response = model.generate_content(prompt)
        sql = response.text.strip()
        # Remove any markdown formatting if the AI adds it
        return sql.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        print(f"DEBUG: Gemini Error: {e}")
        return "SELECT * FROM users" # Safety fallback
