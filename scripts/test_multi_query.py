from enterprise_document_intelligence.rag.retriever import RetrieverManager


QUERY = "What is the maximum financing limit for SME working capital?"


def main():

    manager = RetrieverManager(k=5)

    docs = manager.multi_query_search(QUERY)

    print("=" * 80)
    print(f"Retrieved {len(docs)} documents")
    print("=" * 80)

    for i, doc in enumerate(docs, start=1):

        print(f"\nResult {i}")
        print("-" * 60)

        print("Document :", doc.metadata.get("document_name"))
        print("Page     :", doc.metadata.get("page"))

        print()

        print(doc.page_content[:400])


if __name__ == "__main__":
    main()