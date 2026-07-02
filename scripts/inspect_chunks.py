from pathlib import Path

from enterprise_document_intelligence.ingestion.loader import DocumentLoader
from enterprise_document_intelligence.ingestion.cleaner import DocumentCleaner
from enterprise_document_intelligence.ingestion.filter import DocumentFilter
from enterprise_document_intelligence.ingestion.chunker import DocumentChunker


def main():
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    cleaner = DocumentCleaner()
    doc_filter = DocumentFilter()
    chunker = DocumentChunker()

    pages = loader.load_pdf(pdf_path)
    pages = cleaner.clean_documents(pages)
    pages = doc_filter.filter_documents(pages)
    chunks = chunker.split_documents(pages)

    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:20], start=1):
        print("\n" + "=" * 80)
        print(f"Chunk {i}")
        print("=" * 80)
        print(f"Page: {chunk.metadata.get('page')}")
        print(chunk.page_content[:500])


if __name__ == "__main__":
    main()