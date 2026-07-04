from langchain_core.documents import Document

from enterprise_document_intelligence.services.context_builder import ContextBuilder
from enterprise_document_intelligence.rag.retrievers import RetrieverManager


class RAGService:
    """
    Shared retrieval utilities used by multiple agents.
    """

    def __init__(self):

        self.retriever = RetrieverManager()

    def retrieve(
        self,
        question: str,
    ) -> tuple[str, list[Document], list[str]]:
        """
        Returns:
            context,
            retrieved documents,
            unique sources
        """

        documents = self.retriever.hybrid_search(question)

        context = ContextBuilder.build(documents)

        sources = []

        seen = set()

        for doc in documents:

            source = (
                f"{doc.metadata.get('document_name')} "
                f"(Page {doc.metadata.get('page')})"
            )

            if source not in seen:

                seen.add(source)

                sources.append(source)

        return context, documents, sources