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
    Retrieval strategy manager with lazy initialization.
    """

    def __init__(
        self,
        k: int = 5,
        mode: RetrievalMode = RetrievalMode.ADVANCED,
    ):
        self.k = k
        self.mode = mode

        self._fast = None
        self._advanced = None
        self._research = None

    @property
    def fast(self):

        if self._fast is None:
            print("Initializing FastRetriever...")
            self._fast = FastRetriever(self.k)

        return self._fast

    @property
    def advanced(self):

        if self._advanced is None:
            print("Initializing AdvancedRetriever...")
            self._advanced = AdvancedRetriever(self.k)

        return self._advanced

    @property
    def research(self):

        if self._research is None:
            print("Initializing ResearchRetriever...")
            self._research = ResearchRetriever()

        return self._research

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