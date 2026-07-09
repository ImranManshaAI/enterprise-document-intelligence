from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from enterprise_document_intelligence.core.config import get_settings


def get_llm():

    settings = get_settings()

    provider = settings.llm_provider.lower()

    if provider == "gemini":

        if not settings.google_api_key:
            raise ValueError(
                "GOOGLE_API_KEY is not configured."
            )

        return ChatGoogleGenerativeAI(
            model=settings.llm_model,
            api_key=settings.google_api_key,
            temperature=0,
        )

    elif provider == "openrouter":

        if not settings.open_router_api_key:
            raise ValueError(
                "OPEN_ROUTER_API_KEY is not configured."
            )

        return ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.open_router_api_key,
            base_url="https://openrouter.ai/api/v1",
            temperature=0,
        )

    elif provider == "groq":

        if not settings.groq_api_key:
            raise ValueError(
                "GROQ_API_KEY is not configured."
            )

        return ChatGroq(
            model=settings.llm_model,
            api_key=settings.groq_api_key,
            temperature=0,
        )

    else:

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )