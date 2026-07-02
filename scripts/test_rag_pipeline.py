from enterprise_document_intelligence.rag.pipeline import RAGPipeline


QUESTION = "What is the maximum financing limit for SME working capital?"


def main():

    pipeline = RAGPipeline()

    answer, documents = pipeline.ask(QUESTION)

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(answer)

    print("\n")
    print("=" * 80)
    print("SOURCES")
    print("=" * 80)

    for doc in documents:

        print(
            f"{doc.metadata.get('document_name')} "
            f"(Page {doc.metadata.get('page')})"
        )


if __name__ == "__main__":
    main()