from enterprise_document_intelligence.rag.vector_store import VectorStoreManager


def main():
    manager = VectorStoreManager()
    vector_store = manager.get_vector_store()

    docs = vector_store.similarity_search(
        "Small and Medium Enterprise Financing Prudential Regulations",
        k=10,
    )

    for i, doc in enumerate(docs, 1):
        print("=" * 80)
        print(f"Chunk {i}")
        print("=" * 80)
        print("Document:", doc.metadata.get("document_name"))
        print("Page:", doc.metadata.get("page"))
        print("Length:", len(doc.page_content))
        print()
        print(repr(doc.page_content[:300]))


if __name__ == "__main__":
    main()