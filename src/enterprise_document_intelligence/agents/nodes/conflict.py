from enterprise_document_intelligence.agents.state import AgentState


def conflict_node(state: AgentState) -> AgentState:
    """
    Placeholder conflict detection node.
    """

    state["answer"] = (
        "Conflict detection workflow is not implemented yet."
    )

    return state