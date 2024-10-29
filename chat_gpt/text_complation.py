
from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "just say 'hey' "},
  ]
)

output = response.choices[0].message.content
print(output)
print(response)

