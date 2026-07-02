from enterprise_document_intelligence.rag.retrievers import RetrieverManager


QUERIES = [
    "What is the maximum financing limit for SME working capital?",
    "What is Regulation R-5?",
    "What are customer due diligence requirements?",
    "What is Fair Treatment of Consumers?",
    "What collateral is required for SME financing?",
]


def print_results(title, docs):

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)

    for i, doc in enumerate(docs, 1):

        print(f"\n{i}")

        print(
            f"{doc.metadata.get('document_name')} "
            f"(Page {doc.metadata.get('page')})"
        )

        print()
        print(doc.page_content[:250])


def main():

    manager = RetrieverManager(k=5)

    for query in QUERIES:

        print("\n" + "=" * 100)
        print(f"QUERY: {query}")
        print("=" * 100)

        print_results(
            "DENSE",
            manager.similarity_search(query),
        )

        print_results(
            "BM25",
            manager.bm25_search(query),
        )

        print_results(
            "HYBRID",
            manager.hybrid_search(query),
        )


if __name__ == "__main__":
    main()