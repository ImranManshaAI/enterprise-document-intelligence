from abc import ABC, abstractmethod
from langchain_core.documents import Document


class BaseRetriever(ABC):
    """
    Base interface for all retrieval strategies.
    """

    @abstractmethod
    def retrieve(
        self,
        question: str,
    ) -> list[Document]:
        """
        Retrieve relevant documents.
        """
        pass