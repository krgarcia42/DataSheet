import google.generativeai as genai

API_KEY = "MY_GEMINI_API_KEY"
genai.configure(api_key = API_KEY)

def ask_gemini_to_sql(user_prompt, schema):
  model = genai.GenerativeModel("gemini-pro")

  #1. format data
  data_content = ""
  for row in rows:
    #row[0] = name, row[1] = age, row[2] = city
    data_content += f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}\n"

  #prompt engineering
  prompt = f"""
  You are an SQL generator. Given the schema: {schema}
  translate the following request into an SQLite SELECT statement.
  Return ONLY the SQL code, no explanation.
  
  Request: {user_prompt}
  """

  try:
    response = model.generate_content(prompt)
    #clean output
    return response.text.replace("```sql", "").replace("```", "").strip()
  except Exception as e:
    return f"SELECT * FROM users" #fallback
