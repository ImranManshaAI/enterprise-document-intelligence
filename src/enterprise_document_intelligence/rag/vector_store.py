from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from enterprise_document_intelligence.rag.embeddings import get_embedding_model
from enterprise_document_intelligence.core.config import get_settings

settings = get_settings()

COLLECTION_NAME = settings.qdrant_collection


class VectorStoreManager:
    """
    Creates and manages the Qdrant vector store.
    """

    def __init__(self):

        self.client = QdrantClient(url=settings.qdrant_url)

        self.embedding_model = get_embedding_model()

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

        return QdrantVectorStore(
            client=self.client,
            collection_name=COLLECTION_NAME,
            embedding=self.embedding_model,
        )

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