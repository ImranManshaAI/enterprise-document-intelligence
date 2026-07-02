from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.services.router import RouterService


router = RouterService()


def router_node(state: AgentState) -> AgentState:
    """
    Decide which workflow should handle the request.
    """

    state["route"] = router.route(
        state["question"]
    )

    return state