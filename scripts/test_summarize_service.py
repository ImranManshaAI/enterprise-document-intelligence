from enterprise_document_intelligence.summarize.service import (
    SummarizeService,
)


QUESTION = "Summarize the Fair Treatment of Consumers framework."


def main():

    service = SummarizeService()

    response = service.summarize(
        QUESTION,
    )

    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)

    print(response.answer)

    print()

    print("=" * 100)
    print("SOURCES")
    print("=" * 100)

    for source in response.sources:

        print(source)


if __name__ == "__main__":
    main()