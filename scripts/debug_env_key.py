from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPEN_ROUTER_API_KEY")

print(repr(key))
print(key.encode())