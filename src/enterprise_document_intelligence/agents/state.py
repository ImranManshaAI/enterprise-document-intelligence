from typing import Literal, TypedDict

from langchain_core.documents import Document


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    question: str

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