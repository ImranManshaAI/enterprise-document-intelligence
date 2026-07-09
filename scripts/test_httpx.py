import os
from dotenv import load_dotenv
import httpx

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('OPEN_ROUTER_API_KEY')}",
    "Content-Type": "application/json",
}

payload = {
    "model": "deepseek/deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "Reply with exactly: OpenRouter is working."
        }
    ],
}

response = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=payload,
)

print(response.status_code)
print(response.text)