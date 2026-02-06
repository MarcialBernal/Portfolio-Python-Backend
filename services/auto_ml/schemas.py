from pydantic import BaseModel


# ============================================================
#                   RESPONSES
# ============================================================

class PredictionResponse(BaseModel):
    date: str
    trend: str
    confidence: float
