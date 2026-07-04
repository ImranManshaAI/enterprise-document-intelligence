from enterprise_document_intelligence.conflict.service import (
    ConflictService,
)


QUESTION = (
    "Do the AML regulations conflict with the SME regulations?"
)


def main():

    service = ConflictService()

    response = service.detect(
        QUESTION,
    )

    print("=" * 100)
    print("CONFLICT ANALYSIS")
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