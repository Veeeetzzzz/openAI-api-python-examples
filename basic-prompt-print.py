import os
import openai

OPENAI_API_KEY = os.getenv("your API key goes here")

# Prompt the user for input
prompt = input("Enter a prompt: ")

# Generate completion using OpenAI API - increase max tokens if you get cut off responses
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    temperature=0
)

# Print the output
print(response.choices[0].text)
