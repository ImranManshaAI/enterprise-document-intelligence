from enum import Enum


class RetrievalMode(str, Enum):
    """
    Supported retrieval strategies.
    """

    FAST = "fast"

    ADVANCED = "advanced"

    RESEARCH = "research"