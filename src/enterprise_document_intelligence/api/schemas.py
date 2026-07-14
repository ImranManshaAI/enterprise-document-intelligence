from pydantic import BaseModel

from enterprise_document_intelligence.core.enums import RetrievalMode


class ChatRequest(BaseModel):
    question: str

    retrieval_mode: RetrievalMode = RetrievalMode.ADVANCED


class Citation(BaseModel):
    """
    Structured citation for frontend consumption.
    """

    document: str

    page: int


class ChatResponse(BaseModel):
    success: bool

    route: str

    answer: str

    sources: list[str]

    citations: list[Citation]

    provider: str

    model: str

    retrieval_mode: str

    latency_ms: int

    cached: bool