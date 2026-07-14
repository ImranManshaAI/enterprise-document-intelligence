from enterprise_document_intelligence.rag.retrievers import RetrieverManager

retriever = RetrieverManager()

docs = retriever.hybrid_search("What is Customer Due Diligence (CDD)?")

for doc in docs:
    print("=" * 60)
    print("Document:", doc.metadata.get("document_name"))
    print("Page:", doc.metadata.get("page"))
    print("File:", doc.metadata.get("file_path"))