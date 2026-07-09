import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("OPEN_ROUTER_API_KEY")

print(key[:15])
print(len(key))

client = OpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: OpenRouter is working."
        }
    ],
)

print(response.choices[0].message.content)