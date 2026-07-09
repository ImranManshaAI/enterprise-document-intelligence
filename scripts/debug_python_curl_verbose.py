import os
import subprocess
from dotenv import load_dotenv

load_dotenv(override=True)

key = os.getenv("OPEN_ROUTER_API_KEY")

cmd = [
    "curl",
    "-v",
    "https://openrouter.ai/api/v1/chat/completions",
    "-H",
    f"Authorization: Bearer {key}",
    "-H",
    "Content-Type: application/json",
    "-d",
    '{"model":"deepseek/deepseek-chat","messages":[{"role":"user","content":"hello"}]}'
]

result = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
)

print("=" * 80)
print("RETURN CODE")
print("=" * 80)
print(result.returncode)

print()

print("=" * 80)
print("STDOUT")
print("=" * 80)
print(result.stdout)

print()

print("=" * 80)
print("STDERR")
print("=" * 80)
print(result.stderr)