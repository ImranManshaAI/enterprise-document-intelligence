import time

from enterprise_document_intelligence.core.config import get_settings
from fastapi import APIRouter

from enterprise_document_intelligence.api.dependencies import graph
from enterprise_document_intelligence.api.schemas import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Enterprise Document Intelligence API"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    settings = get_settings()

    start_time = time.perf_counter()

    state = graph.invoke(
        {
            "question": request.question,
            "retrieval_mode": request.retrieval_mode,
        }
    )

    latency_ms = int(
        (time.perf_counter() - start_time) * 1000
    )

    return ChatResponse(
        success=True,
        route=state["route"],
        answer=state["answer"],
        sources=state["sources"],
        provider=settings.llm_provider,
        model=settings.llm_model,
        retrieval_mode=request.retrieval_mode,
        latency_ms=latency_ms,
        cached=False,
    )