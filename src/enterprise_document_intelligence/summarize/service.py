from enterprise_document_intelligence.prompts.summarize_prompt import (
    SUMMARIZE_PROMPT,
)

from enterprise_document_intelligence.rag.service import (
    RAGService,
)


class SummarizeService:
    """
    Enterprise document summarization service.
    """

    def __init__(self):

        self.rag = RAGService()

    def summarize(self, question: str):

        return self.rag.generate(
            question=question,
            prompt_template=SUMMARIZE_PROMPT,
        )