from typing import Literal

from pydantic import BaseModel, Field


class RouteDecision(BaseModel):
    """
    Structured output for router decisions.
    """

    route: Literal[
        "search",
        "compare",
        "summarize",
        "conflict",
    ] = Field(
        description="Selected route for the user's request."
    )