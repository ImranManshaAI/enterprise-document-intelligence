from langgraph.graph import END, START, StateGraph

from enterprise_document_intelligence.agents.nodes import (
    answer_node,
    compare_node,
    conflict_node,
    context_node,
    router_node,
    search_node,
    summarize_node,
)
from enterprise_document_intelligence.agents.state import AgentState


def route_decision(state: AgentState) -> str:
    """
    Return the route selected by the router.
    """
    return state["route"]


def build_graph():

    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("router", router_node)
    graph.add_node("search", search_node)
    graph.add_node("context", context_node)
    graph.add_node("answer", answer_node)
    graph.add_node("compare", compare_node)
    graph.add_node("summarize", summarize_node)
    graph.add_node("conflict", conflict_node)

    # Start
    graph.add_edge(START, "router")

    # Conditional routing
    graph.add_conditional_edges(
        "router",
        route_decision,
        {
            "search": "search",
            "compare": "compare",
            "summarize": "summarize",
            "conflict": "conflict",
        },
    )

    # Search workflow
    graph.add_edge("search", "context")
    graph.add_edge("context", "answer")
    graph.add_edge("answer", END)

    # Placeholder workflows
    graph.add_edge("compare", END)
    graph.add_edge("summarize", END)
    graph.add_edge("conflict", END)

    return graph.compile()