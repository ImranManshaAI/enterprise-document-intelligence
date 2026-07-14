from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Enterprise Document Intelligence System"
    app_version: str = "0.1.0"

    # Environment
    environment: str = "development"

    # LLM Configuration
    llm_provider: str = "gemini"
    llm_model: str = "gemini-2.5-flash"

    # API Keys
    google_api_key: str = ""
    open_router_api_key: str = ""
    groq_api_key: str = ""

    # Vector Database
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "enterprise_documents"

    # Retrieval
    retrieval_top_k: int = 20
    rerank_top_k: int = 5

    # Reranker
    reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    return Settings()