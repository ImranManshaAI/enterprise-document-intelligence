from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.compare.service import CompareService


service = CompareService()


def compare_node(state: AgentState) -> AgentState:
    """
    Execute compare workflow.
    """

    answer, sources = service.compare(
        state["question"]
    )

    state["answer"] = answer
    state["sources"] = sources

    return state