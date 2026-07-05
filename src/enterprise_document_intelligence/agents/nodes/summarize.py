from enterprise_document_intelligence.agents.state import AgentState

from enterprise_document_intelligence.summarize.service import (
    SummarizeService,
)


service = SummarizeService()


def summarize_node(state: AgentState) -> AgentState:
    """
    Execute summarization workflow.
    """

    response = service.summarize(
        state["question"]
    )

    state["answer"] = response.answer
    state["sources"] = response.sources

    return state