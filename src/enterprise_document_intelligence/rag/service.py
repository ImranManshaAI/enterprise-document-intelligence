from langchain_core.documents import Document

from enterprise_document_intelligence.core.llm import get_llm

from enterprise_document_intelligence.rag.retrievers import (
    RetrieverManager,
)

from enterprise_document_intelligence.services.context_builder import (
    ContextBuilder,
)

from enterprise_document_intelligence.services.response import (
    AgentResponse,
)


class RAGService:
    """
    Shared RAG pipeline used by multiple agents.
    """

    def __init__(self):

        self.retriever = RetrieverManager()

        self.llm = get_llm()

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

    def generate(
        self,
        question: str,
        prompt_template: str,
    ) -> AgentResponse:
        """
        Complete RAG execution.

        Retrieve
            ↓
        Build Context
            ↓
        Prompt
            ↓
        LLM
        """

        context, _, sources = self.retrieve(
            question
        )

        prompt = prompt_template.format(
            question=question,
            context=context,
        )

        response = self.llm.invoke(
            prompt
        )

        return AgentResponse(
            answer=response.content,
            sources=sources,
        )