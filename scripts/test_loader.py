from pathlib import Path

from enterprise_document_intelligence.ingestion.loader import DocumentLoader


def main() -> None:
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    documents = loader.load_pdf(pdf_path)

    print("=" * 80)
    print(f"Loaded {len(documents)} pages")
    print("=" * 80)

    first_page = documents[0]

    print("\nMetadata\n")
    for key, value in first_page.metadata.items():
        print(f"{key}: {value}")

    print("\nPreview\n")
    print(first_page.page_content[:700])


if __name__ == "__main__":
    main()