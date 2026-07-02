from pathlib import Path

from unstructured.partition.pdf import partition_pdf


def main():
    pdf_path = Path("data/raw/SME-PRs-Updtd-Jan-2025.pdf")

    elements = partition_pdf(
        filename=str(pdf_path),
        strategy="fast",
    )

    print(f"Total elements: {len(elements)}")
    print("=" * 80)

    for element in elements[:20]:
        print(type(element).__name__)
        print(repr(element.text[:150]))
        print("-" * 80)


if __name__ == "__main__":
    main()