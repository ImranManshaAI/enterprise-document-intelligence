from langchain_core.documents import Document

from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

from enterprise_document_intelligence.rag.retrievers.base import (
    BaseRetriever,
)
from enterprise_document_intelligence.rag.storage import (
    DocumentStorage,
)
from enterprise_document_intelligence.rag.vector_store import (
    VectorStoreManager,
)


class FastRetriever(BaseRetriever):
    """
    Fast enterprise retrieval.

    Dense
        +
    BM25

    No MultiQuery expansion.
    """

    def __init__(self, k: int = 5):

        self.k = k

        manager = VectorStoreManager()

        self.vector_store = manager.get_vector_store()

        # Dense Retriever
        self.dense_retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

        # BM25 Retriever
        docs = DocumentStorage.load()

        self.bm25_retriever = BM25Retriever.from_documents(
            docs
        )
        self.bm25_retriever.k = k

        # Hybrid Retriever
        self.hybrid_retriever = EnsembleRetriever(
            retrievers=[
                self.dense_retriever,
                self.bm25_retriever,
            ],
            weights=[
                0.7,
                0.3,
            ],
        )

    def retrieve(
        self,
        question: str,
    ) -> list[Document]:

        documents = self.hybrid_retriever.invoke(
            question
        )

        return documents[: self.k]