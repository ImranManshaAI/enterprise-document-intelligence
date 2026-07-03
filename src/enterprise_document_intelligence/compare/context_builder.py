from enterprise_document_intelligence.compare.schema import CompareRetrievalResult


class CompareContextBuilder:
    """
    Builds structured context for comparison prompts.
    """

    @staticmethod
    def build(result: CompareRetrievalResult) -> str:

        sections = []

        # Left topic
        sections.append("=" * 80)
        sections.append(f"TOPIC A: {result.left_topic}")
        sections.append("=" * 80)

        for doc in result.left_documents:

            sections.append(
                f"""
Document: {doc.metadata.get("document_name")}
Page: {doc.metadata.get("page")}

{doc.page_content}
"""
            )

            sections.append("-" * 80)

        # Right topic
        sections.append("=" * 80)
        sections.append(f"TOPIC B: {result.right_topic}")
        sections.append("=" * 80)

        for doc in result.right_documents:

            sections.append(
                f"""
Document: {doc.metadata.get("document_name")}
Page: {doc.metadata.get("page")}

{doc.page_content}
"""
            )

            sections.append("-" * 80)

        return "\n".join(sections)