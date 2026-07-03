from enterprise_document_intelligence.compare.service import CompareService


QUESTION = "Compare AML regulations with SME regulations."


def main():

    service = CompareService()

    answer, sources = service.compare(
        QUESTION,
    )

    print("=" * 100)
    print("ANSWER")
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