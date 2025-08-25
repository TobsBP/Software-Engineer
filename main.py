from google.genai import types
from google import genai
import os

token = os.getenv("api_key")

client = genai.Client(api_key=token)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)

print(response.text)