import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPEN_ROUTER_API_KEY")

subprocess.run([
    "curl",
    "https://openrouter.ai/api/v1/chat/completions",
    "-H",
    f"Authorization: Bearer {key}",
    "-H",
    "Content-Type: application/json",
    "-d",
    '{"model":"deepseek/deepseek-chat","messages":[{"role":"user","content":"hello"}]}'
])