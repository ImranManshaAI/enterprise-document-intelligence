from enterprise_document_intelligence.compare.context_builder import CompareContextBuilder
from enterprise_document_intelligence.compare.extractor import TopicExtractor
from enterprise_document_intelligence.compare.retriever import CompareRetriever


QUERY = "Compare AML regulations with SME regulations."


def main():

    extractor = TopicExtractor()
    retriever = CompareRetriever()

    topics = extractor.extract(QUERY)

    result = retriever.retrieve(topics)

    context = CompareContextBuilder.build(result)

    print("=" * 80)
    print("COMPARE CONTEXT")
    print("=" * 80)
    print(context)


if __name__ == "__main__":
    main()