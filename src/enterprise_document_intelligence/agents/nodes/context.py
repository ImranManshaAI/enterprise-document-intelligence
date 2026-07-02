from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.services.context_builder import ContextBuilder


def context_node(state: AgentState) -> AgentState:
    """
    Build the context supplied to the LLM.
    """

    state["context"] = ContextBuilder.build(
        state["documents"]
    )

    return state