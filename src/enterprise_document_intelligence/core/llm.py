from langchain_google_genai import ChatGoogleGenerativeAI

from enterprise_document_intelligence.core.config import get_settings


def get_llm() -> ChatGoogleGenerativeAI:

    settings = get_settings()

    if not settings.google_api_key:
        raise ValueError("GOOGLE_API_KEY is not configured.")

    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        api_key=settings.google_api_key,
        temperature=0,
    )