from services.api_consumption.rawg_api_client import get_genres
from services.api_consumption.schemas import GenresResponse


# -----------------------------
#            GENRES
# -----------------------------
def fetch_genres() -> GenresResponse:
    data = get_genres()
    return GenresResponse.model_validate(data)