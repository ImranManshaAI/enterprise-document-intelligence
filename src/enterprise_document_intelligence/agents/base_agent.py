from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.rag.service import RAGService
from enterprise_document_intelligence.services.response import (
    AgentResponse,
)


class BaseRAGAgent:
    """
    Base class for agents that follow:

    Retrieve
        ↓
    Build Context
        ↓
    Prompt
        ↓
    LLM
    """

    def __init__(self):

        self.rag = RAGService()

        self.llm = get_llm()

    def run(
        self,
        question: str,
        prompt_template: str,
    ) -> AgentResponse:

        context, _, sources = self.rag.retrieve(
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