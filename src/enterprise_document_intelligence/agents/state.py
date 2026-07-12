from typing import Literal, TypedDict

from langchain_core.documents import Document

from enterprise_document_intelligence.core.enums import RetrievalMode

class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    question: str

    retrieval_mode: RetrievalMode

    route: Literal[
        "search",
        "compare",
        "summarize",
        "conflict",
    ]

    documents: list[Document]

    context: str

    answer: str

    sources: list[str]