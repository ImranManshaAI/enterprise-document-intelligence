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

    state = graph.invoke(
        {
            "question": request.question,
        }
    )

    return ChatResponse(
        route=state["route"],
        answer=state["answer"],
        sources=state["sources"],
    )