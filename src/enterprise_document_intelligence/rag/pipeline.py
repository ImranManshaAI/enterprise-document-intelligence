from langchain_core.documents import Document

from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.rag.retriever import RetrieverManager


class RAGPipeline:
    """
    Enterprise RAG Pipeline.

    Retrieval
        ↓
    Prompt Construction
        ↓
    Gemini
        ↓
    Answer + Sources
    """

    def __init__(self):

        self.llm = get_llm()

        self.retriever = RetrieverManager(k=5)

    def _build_context(
        self,
        documents: list[Document],
    ) -> str:

        sections = []

        for i, doc in enumerate(documents, start=1):

            source = (
                f"Document: {doc.metadata.get('document_name')}\n"
                f"Page: {doc.metadata.get('page')}\n\n"
                f"{doc.page_content}"
            )

            sections.append(source)

        return "\n\n----------------------\n\n".join(sections)

    def ask(
        self,
        question: str,
    ):

        documents = self.retriever.multi_query_search(question)

        context = self._build_context(documents)

        print("=" * 80)
        print("CONTEXT SENT TO GEMINI")
        print("=" * 80)
        print(context)
        print("=" * 80)

        prompt = f"""
You are an Enterprise Banking AI Assistant.

Answer ONLY using the provided context.

If the answer is not contained in the documents,
reply:

"I could not find this information in the provided documents."

Always cite the document name and page number.

Context:

{context}

Question:

{question}
"""

        response = self.llm.invoke(prompt)

        return response.content, documents