from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Enterprise Document Intelligence System"
    app_version: str = "0.1.0"

    # Environment
    environment: str = "development"

    # API Keys
    google_api_key: str = ""

    # Vector Database
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "enterprise_documents"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    return Settings()