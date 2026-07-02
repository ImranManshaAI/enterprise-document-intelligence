from enterprise_document_intelligence.agents.schema import RouteDecision
from enterprise_document_intelligence.core.llm import get_llm
from enterprise_document_intelligence.prompts.router import ROUTER_PROMPT


class RouterService:
    """
    Uses Gemini to decide which workflow
    should handle the request.
    """

    def __init__(self):

        llm = get_llm()

        self.router_llm = llm.with_structured_output(
            RouteDecision
        )

    def route(self, question: str) -> str:

        prompt = ROUTER_PROMPT.format(
            question=question,
        )

        decision = self.router_llm.invoke(prompt)

        return decision.route