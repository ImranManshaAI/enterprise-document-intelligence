from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.prompts.summarize_prompt import (
    SUMMARIZE_PROMPT,
)
from enterprise_document_intelligence.rag.service import RAGService


class SummarizeService:
    """
    Enterprise document summarization workflow.
    """

    def __init__(self):

        self.rag = RAGService()

        self.llm = get_llm()

    def summarize(
        self,
        question: str,
    ):

        context, _, sources = self.rag.retrieve(
            question
        )

        prompt = SUMMARIZE_PROMPT.format(
            question=question,
            context=context,
        )

        response = self.llm.invoke(prompt)

        return response.content, sources