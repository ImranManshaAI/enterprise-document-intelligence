import re

from langchain_core.documents import Document


class DocumentFilter:
    """
    Removes low-value pages before chunking.
    """

    MIN_CONTENT_LENGTH = 200

    LOW_VALUE_PATTERNS = [
        r"table of contents",
        r"contents",
        r"this page intentionally left blank",
    ]

    def keep(self, document: Document) -> bool:

        text = document.page_content.strip()

        # Very short pages
        if len(text) < self.MIN_CONTENT_LENGTH:
            return False

        lower = text.lower()

        # TOC / blank pages
        for pattern in self.LOW_VALUE_PATTERNS:
            if re.search(pattern, lower):
                return False

        return True

    def filter_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:

        return [doc for doc in documents if self.keep(doc)]