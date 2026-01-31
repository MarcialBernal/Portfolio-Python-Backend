from fastapi import APIRouter
from services.auto_ml.schemas import PredictionResponse
from services.auto_ml.crud import get_prediction

# ============================================================
#                   ROUTER
# ============================================================

router = APIRouter(tags=["Auto ML"])


# ============================================================
#                   ROUTES
# ============================================================

@router.get("/predict", response_model=PredictionResponse)
def predict():
    return get_prediction()
