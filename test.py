import os
import google.generativeai as genai


# Set the API key directly in the script
os.environ["API_KEY"] = "AIzaSyD1PB2ymbZxTvEuV1YpVYOwUiTirWumzrE"

# Retrieve the API key from the environment variable
api_key = os.environ["API_KEY"]

# Print the first few characters of the API key for verification
print(f"Using API_KEY: {api_key[:4]}******")  # Show part of the key

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

temp = input("Enter the prompt\n")

prompt = f"""
Given a piece of text, classify it as harassment or non-harassment. \n
text: {temp}"""
#model = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel("gemini-1.5-flash-8b")

response = model.generate_content(contents=prompt)
#print(response.text)
if "Non-harassment" in response.text: 
    print(temp)
else:
    print("Likely contains harassing messages")