from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.tools.search import search_documents


def search_node(state: AgentState) -> AgentState:
    """
    Retrieve relevant enterprise documents.
    """

    result = search_documents.invoke(
        {
            "query": state["question"]
        }
    )

    state["documents"] = result["documents"]
    state["sources"] = result["sources"]

    return state