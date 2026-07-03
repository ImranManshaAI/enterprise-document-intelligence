from enterprise_document_intelligence.compare.extractor import TopicExtractor
from enterprise_document_intelligence.compare.retriever import CompareRetriever


QUERY = "Compare AML regulations with SME regulations."


def print_documents(title, documents):

    print()
    print("=" * 80)
    print(title)
    print("=" * 80)

    for i, doc in enumerate(documents, 1):

        print(f"\n{i}")

        print(
            f"{doc.metadata.get('document_name')} "
            f"(Page {doc.metadata.get('page')})"
        )

        print()

        print(doc.page_content[:250])


def main():

    extractor = TopicExtractor()

    retriever = CompareRetriever()

    topics = extractor.extract(QUERY)

    result = retriever.retrieve(topics)

    print(f"LEFT : {result.left_topic}")
    print(f"RIGHT: {result.right_topic}")

    print_documents(
        "LEFT DOCUMENTS",
        result.left_documents,
    )

    print_documents(
        "RIGHT DOCUMENTS",
        result.right_documents,
    )



if __name__ == "__main__":
    main()