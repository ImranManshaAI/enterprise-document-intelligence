from enterprise_document_intelligence.core.enums import RetrievalMode

from enterprise_document_intelligence.rag.retrievers.advanced import (
    AdvancedRetriever,
)
from enterprise_document_intelligence.rag.retrievers.fast import (
    FastRetriever,
)
from enterprise_document_intelligence.rag.retrievers.research import (
    ResearchRetriever,
)


class RetrieverManager:
    """
    Backward-compatible facade for retrieval strategies.
    """

    def __init__(
        self,
        k: int = 5,
        mode: RetrievalMode = RetrievalMode.ADVANCED,
    ):
        self.mode = mode

        self.fast = FastRetriever(k)

        self.advanced = AdvancedRetriever(k)

        self.research = ResearchRetriever()

    def _strategy(self):
        if self.mode == RetrievalMode.FAST:
            return self.fast

        if self.mode == RetrievalMode.RESEARCH:
            return self.research

        return self.advanced

    def hybrid_search(
        self,
        query: str,
    ):
        return self._strategy().retrieve(query)