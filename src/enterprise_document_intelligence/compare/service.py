from enterprise_document_intelligence.compare.context_builder import (
    CompareContextBuilder,
)
from enterprise_document_intelligence.compare.extractor import TopicExtractor
from enterprise_document_intelligence.core.llm_utils import extract_text
from enterprise_document_intelligence.compare.retriever import CompareRetriever
from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.prompts.compare_prompt import (
    COMPARE_PROMPT,
)


class CompareService:
    """
    Enterprise comparison workflow.
    """

    def __init__(self):

        self.extractor = TopicExtractor()

        self.retriever = CompareRetriever()

        self.llm = get_llm()

    def compare(
        self,
        question: str,
    ):

        # Extract topics
        topics = self.extractor.extract(question)

        # Retrieve documents
        retrieval_result = self.retriever.retrieve(topics)

        # Build comparison context
        context = CompareContextBuilder.build(
            retrieval_result
        )

        # Build prompt
        prompt = COMPARE_PROMPT.format(
            question=question,
            context=context,
        )

        # Generate answer
        response = self.llm.invoke(prompt)

        print("=" * 80)
        print("RESPONSE TYPE:", type(response))
        print()
        print("CONTENT TYPE:", type(response.content))
        print()
        print("RAW RESPONSE:")
        print(response)
        print()
        print("CONTENT:")
        print(response.content)
        print("=" * 80)

        # Collect unique sources
        sources = []

        seen = set()

        for docs in (
            retrieval_result.left_documents,
            retrieval_result.right_documents,
        ):

            for doc in docs:

                source = (
                    f"{doc.metadata.get('document_name')} "
                    f"(Page {doc.metadata.get('page')})"
                )

                if source not in seen:

                    seen.add(source)

                    sources.append(source)

        answer = extract_text(response)

        return answer, sources