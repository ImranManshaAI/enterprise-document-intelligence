from enterprise_document_intelligence.core.config import get_settings

settings = get_settings()

print("Provider:", settings.llm_provider)
print("Model:", settings.llm_model)
print("Key prefix:", settings.open_router_api_key[:12])