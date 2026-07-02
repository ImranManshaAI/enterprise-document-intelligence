from pathlib import Path

from enterprise_document_intelligence.ingestion.chunker import DocumentChunker
from enterprise_document_intelligence.ingestion.cleaner import DocumentCleaner
from enterprise_document_intelligence.ingestion.loader import DocumentLoader


def main() -> None:
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    cleaner = DocumentCleaner()
    chunker = DocumentChunker()

    documents = loader.load_pdf(pdf_path)
    cleaned_docs = cleaner.clean_documents(documents)
    chunks = chunker.split_documents(cleaned_docs)

    print("=" * 80)
    print(f"Original pages : {len(documents)}")
    print(f"Generated chunks : {len(chunks)}")
    print("=" * 80)

    first_chunk = chunks[0]

    print("\nMetadata\n")
    print(first_chunk.metadata)

    print("\nChunk Length\n")
    print(len(first_chunk.page_content))

    print("\nPreview\n")
    print(first_chunk.page_content)


if __name__ == "__main__":
    main()