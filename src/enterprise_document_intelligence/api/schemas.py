from typing import Literal

from pydantic import BaseModel

from enterprise_document_intelligence.core.enums import RetrievalMode

class ChatRequest(BaseModel):
    question: str

    retrieval_mode: RetrievalMode = RetrievalMode.ADVANCED


class ChatResponse(BaseModel):
    success: bool

    route: str

    answer: str

    sources: list[str]

    provider: str

    model: str

    retrieval_mode: str

    latency_ms: int

    cached: bool