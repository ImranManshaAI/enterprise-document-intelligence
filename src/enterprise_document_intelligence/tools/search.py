from langchain_core.tools import tool

from enterprise_document_intelligence.rag.retrievers import RetrieverManager

from enterprise_document_intelligence.core.enums import RetrievalMode


@tool
def search_documents(
    query: str,
    retrieval_mode: RetrievalMode,
) -> dict:
    
    """
    Search enterprise documents using hybrid retrieval.
    """
    retriever = RetrieverManager(
        k=5,
        mode=retrieval_mode,
    )
    
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