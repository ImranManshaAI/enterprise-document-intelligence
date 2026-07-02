from enterprise_document_intelligence.rag.vector_store import VectorStoreManager


def main():

    manager = VectorStoreManager()

    manager.create_collection()

    print()

    vector_store = manager.get_vector_store()

    print(vector_store)


if __name__ == "__main__":
    main()