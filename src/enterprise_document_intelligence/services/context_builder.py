from langchain_core.documents import Document


class ContextBuilder:
    """
    Builds the context string sent to the LLM.
    """

    @staticmethod
    def build(documents: list[Document]) -> str:

        sections = []

        for document in documents:

            section = (
                f"Document: {document.metadata.get('document_name')}\n"
                f"Page: {document.metadata.get('page')}\n\n"
                f"{document.page_content}"
            )

            sections.append(section)

        return "\n\n----------------------\n\n".join(sections)