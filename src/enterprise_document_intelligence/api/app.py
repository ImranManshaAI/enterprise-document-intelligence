from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from enterprise_document_intelligence.api.routes import router


app = FastAPI(
    title="Enterprise Document Intelligence API",
    description="AI-powered Enterprise Document Intelligence System",
    version="1.0.0",
)

# Serve original enterprise documents
app.mount(
    "/documents",
    StaticFiles(directory="data/raw"),
    name="documents",
)

app.include_router(router)