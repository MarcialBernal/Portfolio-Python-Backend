from pydantic import BaseModel
from typing import List, Optional


class Genre(BaseModel):
    id: int
    name: str
    slug: Optional[str] = None
    games_count: Optional[int] = None
    image_background: Optional[str] = None


class GenresResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Genre]