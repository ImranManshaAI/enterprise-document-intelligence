from pydantic import BaseModel


class AgentResponse(BaseModel):
    """
    Standard response returned by all AI agents.
    """

    answer: str

    sources: list[str]