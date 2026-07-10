import os

from enterprise_document_intelligence.core.config import get_settings

print("=== Raw Environment ===")
print("LLM_PROVIDER:", os.getenv("LLM_PROVIDER"))
print("LLM_MODEL   :", os.getenv("LLM_MODEL"))

print()

settings = get_settings()

print("=== Pydantic Settings ===")
print("Provider:", settings.llm_provider)
print("Model   :", settings.llm_model)