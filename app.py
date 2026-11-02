from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI()

question = input("user: ")

response = client.chat.completions.create(
    model="gpt-5.3-chat-latest",
    max_tokens=50,
    n=1,
    temperature=0,
    messages=[
        {"role": "user", "content": question}
    ]
)

for choise in response.choices:
    print("AI{choise.message.content}")