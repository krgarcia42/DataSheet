import google.generativeai as genai

API_KEY = "MY_GEMINI_API_KEY"
genai.configure(api_key = API_KEY)

def ask_gemini_to_summarize(rows):
  model = genai.GenerativeModel("gemini-pro")

  #1. format data
  data_content = ""
  for row in rows:
    #row[0] = name, row[1] = age, row[2] = city
    data_content += f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}\n"

  #prompt engineering
  prompt = f"Analyze these filtered users and give a brief summary:\n{data_content}"

  try:
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    return f"AI Error: {e}"
