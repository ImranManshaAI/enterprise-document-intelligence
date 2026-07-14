import time

from fastapi import APIRouter

from enterprise_document_intelligence.api.dependencies import graph
from enterprise_document_intelligence.api.schemas import (
    ChatRequest,
    ChatResponse,
    Citation,
)
from enterprise_document_intelligence.core.config import get_settings

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

    try:

        state = graph.invoke(
            {
                "question": request.question,
                "retrieval_mode": request.retrieval_mode,
            }
        )

    except NotImplementedError:

        latency_ms = int(
            (time.perf_counter() - start_time) * 1000
        )

        return ChatResponse(
            success=False,
            route="search",
            answer="Research retrieval mode will be available in a future release.",
            sources=[],
            citations=[],
            provider=settings.llm_provider,
            model=settings.llm_model,
            retrieval_mode=request.retrieval_mode,
            latency_ms=latency_ms,
            cached=False,
        )

    latency_ms = int(
        (time.perf_counter() - start_time) * 1000
    )

    citations = []

    seen = set()

    for document in state["documents"]:

        document_name = document.metadata.get("document_name")

        page = document.metadata.get("page")

        key = (document_name, page)

        if key in seen:
            continue

        seen.add(key)

        citations.append(
            Citation(
                document=document_name,
                page=page,
            )
        )

    return ChatResponse(
        success=True,
        route=state["route"],
        answer=state["answer"],
        sources=state["sources"],
        citations=citations,
        provider=settings.llm_provider,
        model=settings.llm_model,
        retrieval_mode=request.retrieval_mode,
        latency_ms=latency_ms,
        cached=False,
    )