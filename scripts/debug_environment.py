import os

print("=" * 60)
print("PROXY VARIABLES")
print("=" * 60)

for key in [
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "NO_PROXY",
    "no_proxy",
]:
    print(f"{key}: {os.getenv(key)}")