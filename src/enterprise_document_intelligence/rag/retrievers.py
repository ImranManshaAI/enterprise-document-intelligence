from langchain_core.documents import Document

from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_community.retrievers import BM25Retriever

from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.rag.storage import DocumentStorage
from enterprise_document_intelligence.rag.vector_store import VectorStoreManager


class RetrieverManager:
    """
    Production retrieval layer.

    - Dense Retrieval (Qdrant)
    - MultiQuery Retrieval
    - BM25 Retrieval
    - Hybrid Retrieval (Ensemble)
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

        self.bm25_retriever = BM25Retriever.from_documents(docs)
        self.bm25_retriever.k = k

        # Multi Query Retriever
        self.multi_query_retriever = MultiQueryRetriever.from_llm(
            retriever=self.dense_retriever,
            llm=get_llm(),
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

    def similarity_search(
        self,
        query: str,
    ) -> list[Document]:

        return self.dense_retriever.invoke(query)


    def bm25_search(
        self,
        query: str,
    ) -> list[Document]:

        return self.bm25_retriever.invoke(query)


    def multi_query_search(
        self,
        query: str,
    ) -> list[Document]:

        documents = self.multi_query_retriever.invoke(query)

        return documents[: self.k]


    def hybrid_search(
        self,
        query: str,
    ) -> list[Document]:

        documents = self.hybrid_retriever.invoke(query)

        return documents[: self.k]