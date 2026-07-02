from src.app.core.config import settings

print("=" * 50)
print(settings.app_name)
print(settings.app_version)
print(settings.environment)
print(settings.qdrant_url)
print(settings.qdrant_collection)
print("=" * 50)