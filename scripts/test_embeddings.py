from enterprise_document_intelligence.rag.embeddings import get_embedding_model


def main():

    model = get_embedding_model()

    embedding = model.embed_query(
        "What is the maximum financing limit for SME loans?"
    )

    print("=" * 60)
    print(f"Embedding dimension : {len(embedding)}")
    print("=" * 60)

    print(embedding[:10])


if __name__ == "__main__":
    main()