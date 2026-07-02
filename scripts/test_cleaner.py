from pathlib import Path

from enterprise_document_intelligence.ingestion.cleaner import DocumentCleaner
from enterprise_document_intelligence.ingestion.loader import DocumentLoader


def main() -> None:
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    cleaner = DocumentCleaner()

    documents = loader.load_pdf(pdf_path)
    cleaned_documents = cleaner.clean_documents(documents)

    print("=" * 80)
    print(f"Original Pages : {len(documents)}")
    print(f"Cleaned Pages  : {len(cleaned_documents)}")
    print("=" * 80)

    print("\nFirst 700 Characters\n")
    print(cleaned_documents[0].page_content[:700])


if __name__ == "__main__":
    main()