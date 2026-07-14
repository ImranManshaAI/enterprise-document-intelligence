from enterprise_document_intelligence.rag.storage import DocumentStorage

docs = DocumentStorage.load()

print("=" * 80)

print(docs[0].metadata)

print("=" * 80)