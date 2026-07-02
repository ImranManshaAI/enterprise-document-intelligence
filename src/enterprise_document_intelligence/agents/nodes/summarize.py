from enterprise_document_intelligence.agents.state import AgentState


def summarize_node(state: AgentState) -> AgentState:
    """
    Placeholder summarize node.
    """

    state["answer"] = (
        "Summarization workflow is not implemented yet."
    )

    return state