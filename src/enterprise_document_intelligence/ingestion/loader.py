from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads enterprise PDF documents and enriches them with metadata.
    """

    ORGANIZATION = "State Bank of Pakistan"

    def load_pdf(self, pdf_path: str | Path) -> list[Document]:
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"File not found: {pdf_path}")

        loader = PyMuPDFLoader(str(pdf_path))
        documents = loader.load()

        for document in documents:
            document.metadata.update(
                {
                    "document_name": pdf_path.stem,
                    "organization": self.ORGANIZATION,
                    "document_type": "regulation",
                    "source": str(pdf_path),
                }
            )

        return documents