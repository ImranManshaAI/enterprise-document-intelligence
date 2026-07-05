from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.conflict.service import (
    ConflictService,
)


service = ConflictService()


def conflict_node(state: AgentState) -> AgentState:
    """
    Execute conflict detection workflow.
    """

    response = service.detect(
        state["question"]
    )

    state["answer"] = response.answer
    state["sources"] = response.sources

    return state