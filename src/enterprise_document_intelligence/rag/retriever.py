from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.documents import Document

from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.rag.vector_store import VectorStoreManager


class RetrieverManager:

    def __init__(self, k: int = 5):

        manager = VectorStoreManager()

        self.vector_store = manager.get_vector_store()

        self.base_retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

    def similarity_search(
        self,
        query: str,
    ) -> list[Document]:

        return self.base_retriever.invoke(query)

    def multi_query_search(
        self,
        query: str,
    ) -> list[Document]:

        retriever = MultiQueryRetriever.from_llm(
            retriever=self.base_retriever,
            llm=get_llm(),
        )

        return retriever.invoke(query)