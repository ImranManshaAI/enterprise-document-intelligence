from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


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