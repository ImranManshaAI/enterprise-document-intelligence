from functools import lru_cache

from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from enterprise_document_intelligence.core.config import get_settings
from enterprise_document_intelligence.rag.embeddings import get_embedding_model

settings = get_settings()
COLLECTION_NAME = settings.qdrant_collection


@lru_cache(maxsize=1)
def get_qdrant_client() -> QdrantClient:
    """
    Returns a singleton Qdrant client.
    """
    print("Creating Qdrant client...")

    return QdrantClient(
        url=settings.qdrant_url,
    )


@lru_cache(maxsize=1)
def get_vector_store() -> QdrantVectorStore:
    """
    Returns a singleton Qdrant vector store.
    """
    print("Creating vector store...")

    return QdrantVectorStore(
        client=get_qdrant_client(),
        collection_name=COLLECTION_NAME,
        embedding=get_embedding_model(),
    )


class VectorStoreManager:
    """
    Helper class around the shared vector store.
    """

    def __init__(self):
        self.client = get_qdrant_client()

    def create_collection(self):

        collections = self.client.get_collections().collections

        existing = [c.name for c in collections]

        if COLLECTION_NAME not in existing:

            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE,
                ),
            )

            print(f"Created collection: {COLLECTION_NAME}")

        else:

            print(f"Collection already exists: {COLLECTION_NAME}")

    def get_vector_store(self):

        return get_vector_store()

    def collection_exists(self) -> bool:

        collections = self.client.get_collections().collections

        return COLLECTION_NAME in [c.name for c in collections]

    def delete_collection(self) -> None:

        if self.collection_exists():

            self.client.delete_collection(COLLECTION_NAME)

            print(f"Deleted collection: {COLLECTION_NAME}")

    def reset_collection(self) -> None:

        self.delete_collection()

        self.create_collection()