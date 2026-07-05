from fastapi import FastAPI

from enterprise_document_intelligence.api.routes import router


app = FastAPI(
    title="Enterprise Document Intelligence API",
    description="AI-powered Enterprise Document Intelligence System",
    version="1.0.0",
)

app.include_router(router)