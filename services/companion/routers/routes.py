from fastapi import APIRouter, HTTPException
from services.companion.companion import Companion
from services.companion.schemas import ChatRequest, ChatResponse

from services.companion.companion import Companion

router = APIRouter()
companion = Companion()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """Generate a response to a user question using the Companion assistant.
    Args:
        request: Request containing the user's question.
    Returns:
        The assistant's answer.
    Raises:
        HTTPException: If the question is invalid or the assistant fails.
    """
    try:
        answer = companion.answer(request.question)
        return ChatResponse(answer=answer)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        ) from error