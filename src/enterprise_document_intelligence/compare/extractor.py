from enterprise_document_intelligence.compare.schema import CompareTopics
from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.prompts.compare_extractor import (
    COMPARE_EXTRACTOR_PROMPT,
)


class TopicExtractor:
    """
    Extracts two comparison topics using Gemini.
    """

    def __init__(self):

        llm = get_llm()

        self.extractor = llm.with_structured_output(
            CompareTopics
        )

    def extract(self, question: str) -> CompareTopics:

        prompt = COMPARE_EXTRACTOR_PROMPT.format(
            question=question,
        )

        return self.extractor.invoke(prompt)