from enterprise_document_intelligence.rag.retriever import RetrieverManager


def main():

    retriever = RetrieverManager(k=5)

    query = "What is the maximum financing limit for SME working capital?"

    documents = retriever.retrieve(query)

    print("=" * 80)
    print(f"Retrieved {len(documents)} documents")
    print("=" * 80)

    for i, document in enumerate(documents, start=1):

        print(f"\nResult {i}")
        print("-" * 60)

        print(f"Document : {document.metadata.get('document_name')}")
        print(f"Page     : {document.metadata.get('page')}")

        print("\nPreview:\n")

        print(document.page_content[:400])


if __name__ == "__main__":
    main()