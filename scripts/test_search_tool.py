from enterprise_document_intelligence.tools.search import search_documents


def main():

    result = search_documents.invoke(
        {
            "query": "What are customer due diligence requirements?"
        }
    )

    print("=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in result["sources"]:
        print(source)

    print("\n")
    print("=" * 80)
    print("FIRST DOCUMENT")
    print("=" * 80)

    print(result["documents"][0].page_content[:500])


if __name__ == "__main__":
    main()