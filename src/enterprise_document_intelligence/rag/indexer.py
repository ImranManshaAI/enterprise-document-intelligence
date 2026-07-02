from pathlib import Path
from uuid import uuid4

from enterprise_document_intelligence.ingestion.filter import DocumentFilter
from langchain_core.documents import Document
from enterprise_document_intelligence.rag.storage import DocumentStorage

from enterprise_document_intelligence.ingestion.loader import DocumentLoader
from enterprise_document_intelligence.ingestion.cleaner import DocumentCleaner
from enterprise_document_intelligence.ingestion.chunker import DocumentChunker
from enterprise_document_intelligence.rag.vector_store import VectorStoreManager


class DocumentIndexer:
    """
    Loads, cleans, chunks and indexes documents into Qdrant.
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.cleaner = DocumentCleaner()
        self.filter = DocumentFilter()
        self.chunker = DocumentChunker()

        self.manager = VectorStoreManager()

        self.vector_store = self.manager.get_vector_store()

    def index_directory(
        self,
        directory: str | Path,
        reset: bool = False,
    ):

        directory = Path(directory)
        if reset:
            self.manager.reset_collection()
        else:
            self.manager.create_collection()

        pdf_files = sorted(directory.glob("*.pdf"))

        total_chunks = 0

        all_chunks: list[Document] = []

        for pdf_file in pdf_files:

            print(f"\nIndexing: {pdf_file.name}")

            pages = self.loader.load_pdf(pdf_file)
            pages = self.cleaner.clean_documents(pages)
            pages = self.filter.filter_documents(pages)
            chunks = self.chunker.split_documents(pages)

            document_id = str(uuid4())

            ids = []

            for chunk_index, chunk in enumerate(chunks):

                chunk.metadata["document_id"] = document_id
                chunk.metadata["chunk_id"] = str(uuid4())
                chunk.metadata["chunk_index"] = chunk_index

                ids.append(chunk.metadata["chunk_id"])

            self.vector_store.add_documents(
                documents=chunks,
                ids=ids,
            )

            all_chunks.extend(chunks)

            print(
                f"Pages kept: {len(pages)} | "
                f"Chunks indexed: {len(chunks)}"
            )

            total_chunks += len(chunks)

        DocumentStorage.save(all_chunks)
        print(f"\nSaved {len(all_chunks)} chunks for BM25 retrieval.")
        print("\n" + "=" * 60)
        print(f"Total indexed chunks: {total_chunks}")
        print("=" * 60)