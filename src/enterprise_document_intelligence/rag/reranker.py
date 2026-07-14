from functools import lru_cache

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder
from enterprise_document_intelligence.core.config import get_settings



@lru_cache(maxsize=1)
def get_reranker() -> CrossEncoder:
    """
    Returns a singleton CrossEncoder reranker.
    """

    print("Loading CrossEncoder reranker...")

    settings = get_settings()

    ...

    return CrossEncoder(
        settings.reranker_model,
    )


class CrossEncoderReranker:
    """
    Reranks retrieved documents using a CrossEncoder.
    """

    def __init__(self):
        self.model = get_reranker()

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:

        if not documents:
            return []

        pairs = [
            (query, doc.page_content)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, documents),
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            doc
            for _, doc in ranked[:top_k]
        ]