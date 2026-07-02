from langchain_core.tools import tool

from enterprise_document_intelligence.rag.retrievers import RetrieverManager


retriever = RetrieverManager(k=5)


@tool
def search_documents(query: str) -> dict:
    """
    Search enterprise documents using hybrid retrieval.
    """

    documents = retriever.hybrid_search(query)

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

    return {
        "documents": documents,
        "sources": sources,
    }