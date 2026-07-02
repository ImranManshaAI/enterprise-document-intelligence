from pathlib import Path

from enterprise_document_intelligence.ingestion.cleaner import DocumentCleaner
from enterprise_document_intelligence.ingestion.loader import DocumentLoader
from enterprise_document_intelligence.ingestion.section_parser import SectionParser


def main():

    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    loader = DocumentLoader()
    cleaner = DocumentCleaner()
    parser = SectionParser()

    documents = loader.load_pdf(pdf_path)
    cleaned = cleaner.clean_documents(documents)
    sections = parser.parse(cleaned)

    print("=" * 80)
    print(f"Pages    : {len(documents)}")
    print(f"Sections : {len(sections)}")
    print("=" * 80)

    for i, section in enumerate(sections[:10], start=1):

        print(f"\nSection {i}")
        print("-" * 40)
        print(f"Title : {section.title}")
        print(f"Length: {len(section.content)}")
        print(section.content[:250])


if __name__ == "__main__":
    main()