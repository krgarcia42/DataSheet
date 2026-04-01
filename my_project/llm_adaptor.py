import os
import google.generativeai as genai

API_KEY = "MY_GEMINI_API_KEY"

def ask_gemini_to_summarize(user_rows):
  genai.configure(api_key = API_KEY)
  model = genai.GenerativeModel("gemini-pro")

  prompt = "I have a database of users. Can you summarize my list?"

  for row in user_rows:
    prompt += "\nUser " + str(row[0]) + " is " + str(row[1]) " years old."

  print("Sending data to Gemini...")
  response = model.generate_content(prompt)
  return response.text

if __name__ == "__main__":
  test_data = [("Alice", 25, "New York"), ("Bob", 30, "London")]

  summary = ask_gemini_to_summarize(test_data)
  print(summary)
