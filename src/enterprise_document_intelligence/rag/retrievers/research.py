from langchain_core.documents import Document

from enterprise_document_intelligence.rag.retrievers.base import (
    BaseRetriever,
)


class ResearchRetriever(BaseRetriever):
    """
    Placeholder for future research retrieval.

    Planned features:
    - HyDE
    - RAG Fusion
    - Parent Document Retrieval
    - Contextual Compression
    - GraphRAG
    """

    def retrieve(
        self,
        question: str,
    ) -> list[Document]:

        raise NotImplementedError(
            "Research retrieval mode will be available in a future release."
        )