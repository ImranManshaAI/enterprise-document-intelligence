from enterprise_document_intelligence.rag.indexer import DocumentIndexer


def main():

    indexer = DocumentIndexer()

    indexer.index_directory(
        "data/raw",
        reset=True,
    )


if __name__ == "__main__":
    main()