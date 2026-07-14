from langchain_core.documents import Document

from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_community.retrievers import BM25Retriever

from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.rag.retrievers.base import (
    BaseRetriever,
)
from enterprise_document_intelligence.rag.storage import (
    DocumentStorage,
)
from enterprise_document_intelligence.rag.vector_store import (
    VectorStoreManager,
)

from enterprise_document_intelligence.core.config import get_settings
from enterprise_document_intelligence.rag.reranker import CrossEncoderReranker

class AdvancedRetriever(BaseRetriever):
    """
    Advanced enterprise retrieval.

    MultiQuery
        +
    Dense
        +
    BM25
    """

    def __init__(self, k: int = 5):

        settings = get_settings()

        self.k = settings.rerank_top_k
        self.retrieval_k = settings.retrieval_top_k

        manager = VectorStoreManager()

        self.vector_store = manager.get_vector_store()

        # Dense Retriever
        self.dense_retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": self.retrieval_k},
        )

        # BM25 Retriever
        docs = DocumentStorage.load()

        self.bm25_retriever = BM25Retriever.from_documents(
            docs
        )
        self.bm25_retriever.k = self.retrieval_k

        # MultiQuery Retriever
        self.multi_query_retriever = (
            MultiQueryRetriever.from_llm(
                retriever=self.dense_retriever,
                llm=get_llm(),
            )
        )

        # Hybrid Retriever
        self.hybrid_retriever = EnsembleRetriever(
            retrievers=[
                self.multi_query_retriever,
                self.bm25_retriever,
            ],
            weights=[
                0.7,
                0.3,
            ],
        )

        self.reranker = CrossEncoderReranker()

    def retrieve(
        self,
        question: str,
    ) -> list[Document]:

        documents = self.hybrid_retriever.invoke(
            question
        )

        documents = self.reranker.rerank(
            query=question,
            documents=documents,
            top_k=self.k,
        )

        return documents