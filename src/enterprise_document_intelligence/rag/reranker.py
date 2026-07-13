from functools import lru_cache

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder


@lru_cache(maxsize=1)
def get_reranker() -> CrossEncoder:
    """
    Returns a singleton CrossEncoder reranker.
    """

    print("Loading CrossEncoder reranker...")

    return CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2",
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