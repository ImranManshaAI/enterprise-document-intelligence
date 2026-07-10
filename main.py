import uvicorn

from enterprise_document_intelligence.core.config import (
    get_settings,
)


if __name__ == "__main__":

    settings = get_settings()

    uvicorn.run(
        "enterprise_document_intelligence.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.environment == "development",
    )