from enterprise_document_intelligence.summarize.service import (
    SummarizeService,
)


QUESTION = "Summarize the Fair Treatment of Consumers framework."


def main():

    service = SummarizeService()

    answer, sources = service.summarize(
        QUESTION,
    )

    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)

    print(answer)

    print()

    print("=" * 100)
    print("SOURCES")
    print("=" * 100)

    for source in sources:

        print(source)


if __name__ == "__main__":
    main()