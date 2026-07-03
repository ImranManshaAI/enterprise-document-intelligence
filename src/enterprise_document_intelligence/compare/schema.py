from langchain_core.documents import Document
from pydantic import BaseModel, Field, ConfigDict


class CompareTopics(BaseModel):
    """
    Two topics extracted from the user's comparison request.
    """

    left_topic: str = Field(
        description="The first comparison topic."
    )

    right_topic: str = Field(
        description="The second comparison topic."
    )


class CompareRetrievalResult(BaseModel):
    """
    Result of retrieving documents for both comparison topics.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    left_topic: str

    right_topic: str

    left_documents: list[Document]

    right_documents: list[Document]