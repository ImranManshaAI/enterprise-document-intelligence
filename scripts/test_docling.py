from pathlib import Path

from docling.document_converter import DocumentConverter


def main():
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))

    document = result.document

    print("=" * 80)
    print("Markdown Preview")
    print("=" * 80)

    markdown = document.export_to_markdown()

    print(markdown[:3000])


if __name__ == "__main__":
    main()