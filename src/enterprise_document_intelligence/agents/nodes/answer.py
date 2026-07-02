from enterprise_document_intelligence.agents.state import AgentState
from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.prompts.answer import ANSWER_PROMPT


llm = get_llm()


def answer_node(state: AgentState) -> AgentState:
    """
    Generate the final answer.
    """

    prompt = ANSWER_PROMPT.format(
        question=state["question"],
        context=state["context"],
    )

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state