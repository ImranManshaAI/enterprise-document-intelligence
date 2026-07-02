import re

from langchain_core.documents import Document


class DocumentCleaner:
    """
    Cleans enterprise documents before chunking.

    Responsibilities
    ----------------
    - normalize whitespace
    - remove repeated headers
    - remove printed page numbers
    - preserve metadata
    """

    HEADER_THRESHOLD = 0.7

    def clean_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:

        repeated_headers = self._find_repeated_headers(documents)

        cleaned_docs = []

        for doc in documents:

            text = doc.page_content

            text = self._normalize_whitespace(text)

            text = self._remove_repeated_headers(
                text,
                repeated_headers,
            )

            text = self._remove_page_numbers(text)

            text = text.strip()

            if not text:
                continue

            cleaned_docs.append(
                Document(
                    page_content=text,
                    metadata=doc.metadata,
                )
            )

        return cleaned_docs

    def _normalize_whitespace(
        self,
        text: str,
    ) -> str:

        text = re.sub(r"\n{3,}", "\n\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        return text

    def _find_repeated_headers(
        self,
        documents: list[Document],
    ) -> set[str]:

        counts = {}

        for doc in documents:

            lines = [
                line.strip()
                for line in doc.page_content.splitlines()
                if line.strip()
            ]

            if not lines:
                continue

            header = lines[0]

            counts[header] = counts.get(header, 0) + 1

        threshold = int(len(documents) * self.HEADER_THRESHOLD)

        return {
            header
            for header, count in counts.items()
            if count >= threshold
        }

    def _remove_repeated_headers(
        self,
        text: str,
        headers: set[str],
    ) -> str:

        lines = text.splitlines()

        cleaned = []

        for line in lines:

            if line.strip() in headers:
                continue

            cleaned.append(line)

        return "\n".join(cleaned)

    def _remove_page_numbers(
        self,
        text: str,
    ) -> str:

        patterns = [
            r"^\s*\d+\s*\|\s*P\s*a\s*g\s*e\s*$",
            r"^\s*[ivxlcdmIVXLCDM]+\s*\|\s*P\s*a\s*g\s*e\s*$",
            r"^\s*Page\s+\d+\s*$",
        ]

        lines = text.splitlines()

        cleaned = []

        for line in lines:

            remove = False

            for pattern in patterns:

                if re.match(pattern, line.strip()):

                    remove = True
                    break

            if not remove:
                cleaned.append(line)

        return "\n".join(cleaned)