from fastapi import APIRouter, Query
from services.api_consumption.crud import fetch_genres
from services.api_consumption.schemas import GenresResponse

router = APIRouter()

# -----------------------------
#            GENRES
# -----------------------------
@router.get("/rawg/genres", response_model=GenresResponse)
def get_genres_route():
    return fetch_genres()