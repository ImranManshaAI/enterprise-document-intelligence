from pathlib import Path

from enterprise_document_intelligence.ingestion.loader import DocumentLoader


def main():
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    docs = loader.load_pdf(pdf_path)

    print(repr(docs[0].page_content))


if __name__ == "__main__":
    main()