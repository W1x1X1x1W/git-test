
from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "be stric data anylisize person as pasable"},
    {"role": "user", "content": "genrate for me the names of all week days and put for every day a one word discribing the weather i want evrething i json format and put them all in a dictionry called 'happy days' "},
  ]
)

output = response.choices[0].message.content
print(output)
print(response)

