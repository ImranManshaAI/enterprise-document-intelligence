from enterprise_document_intelligence.compare.extractor import TopicExtractor


QUERIES = [
    "Compare AML regulations with SME regulations.",
    "Compare customer due diligence with fair treatment of consumers.",
    "Compare Islamic Banking and SME financing.",
]


def main():

    extractor = TopicExtractor()

    for query in QUERIES:

        print("=" * 80)
        print(query)
        print("-" * 80)

        topics = extractor.extract(query)

        print("LEFT :", topics.left_topic)
        print("RIGHT:", topics.right_topic)
        print()


if __name__ == "__main__":
    main()