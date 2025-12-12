import google.generativeai as genai

genai.configure(api_key="AIzaSyDu4SqLVpvylPdw7ZfEkQ0FbNxe-cCAdfo")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Write a short poem about the ocean.")
print(response.text)
