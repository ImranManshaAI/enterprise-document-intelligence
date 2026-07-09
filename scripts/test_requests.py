import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

try:
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": "Reply exactly: OpenRouter is working."
            }
        ],
    )

    print(response)

except Exception as e:
    print(type(e))
    print(e)

    if hasattr(e, "response") and e.response is not None:
        print("\nStatus:", e.response.status_code)
        print("\nBody:")
        print(e.response.text)