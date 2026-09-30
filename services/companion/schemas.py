
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request schema containing the user's question."""
    question: str = Field(min_length=1)


class ChatResponse(BaseModel):
    """Response schema containing the assistant's answer."""
    answer: str