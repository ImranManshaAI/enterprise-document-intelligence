import uvicorn

from enterprise_document_intelligence.api.app import app


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )