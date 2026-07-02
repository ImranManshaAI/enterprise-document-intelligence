import re
from dataclasses import dataclass

from langchain_core.documents import Document


@dataclass
class DocumentSection:
    title: str
    content: str
    metadata: dict


class SectionParser:
    """
    Groups page content into logical document sections.

    If no headings are detected, the entire page becomes one section.
    """

    SECTION_PATTERN = re.compile(
        r"^(?:"
        r"\d+(?:\.\d+)*\.?\s+.+|"      # 1. Heading / 1.1 Heading
        r"Chapter\s+\d+.*|"
        r"Part\s+[A-Z0-9]+.*|"
        r"Appendix.*|"
        r"Annex.*"
        r")$",
        re.IGNORECASE,
    )

    def parse(self, documents: list[Document]) -> list[DocumentSection]:
        sections = []

        for document in documents:

            lines = [
                line.strip()
                for line in document.page_content.splitlines()
                if line.strip()
            ]

            current_title = "Untitled Section"
            current_content = []

            for line in lines:

                if self.SECTION_PATTERN.match(line):

                    if current_content:
                        sections.append(
                            DocumentSection(
                                title=current_title,
                                content="\n".join(current_content),
                                metadata=document.metadata.copy(),
                            )
                        )

                    current_title = line
                    current_content = []

                else:
                    current_content.append(line)

            if current_content:
                sections.append(
                    DocumentSection(
                        title=current_title,
                        content="\n".join(current_content),
                        metadata=document.metadata.copy(),
                    )
                )

        return sections