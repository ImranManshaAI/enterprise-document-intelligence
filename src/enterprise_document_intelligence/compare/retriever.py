from enterprise_document_intelligence.compare.schema import (
    CompareTopics,
    CompareRetrievalResult,
)
from enterprise_document_intelligence.rag.retrievers import RetrieverManager


class CompareRetriever:
    """
    Retrieves documents independently for each comparison topic.
    """

    def __init__(self):

        # Retrieve only the top 4 documents for each topic.
        self.retriever = RetrieverManager(k=4)

    def retrieve(
        self,
        topics: CompareTopics,
    ) -> CompareRetrievalResult:

        left_documents = self.retriever.hybrid_search(
            topics.left_topic
        )

        right_documents = self.retriever.hybrid_search(
            topics.right_topic
        )

        return CompareRetrievalResult(
            left_topic=topics.left_topic,
            right_topic=topics.right_topic,
            left_documents=left_documents,
            right_documents=right_documents,
        )