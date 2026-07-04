from enterprise_document_intelligence.core.llm import get_llm

from enterprise_document_intelligence.prompts.conflict_prompt import (
    CONFLICT_PROMPT,
)

from enterprise_document_intelligence.rag.service import RAGService

from enterprise_document_intelligence.services.response import (
    AgentResponse,
)


class ConflictService:
    """
    Detects conflicting or inconsistent information
    across enterprise documents.
    """

    def __init__(self):

        self.rag = RAGService()

        self.llm = get_llm()

    def detect(
        self,
        question: str,
    ) -> AgentResponse:

        context, _, sources = self.rag.retrieve(
            question
        )

        prompt = CONFLICT_PROMPT.format(
            question=question,
            context=context,
        )

        response = self.llm.invoke(prompt)

        return AgentResponse(
            answer=response.content,
            sources=sources,
        )