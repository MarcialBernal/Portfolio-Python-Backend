from fastapi import APIRouter, Query
from typing import List
from services.web_scraper.crud import get_random_books, get_top_popular_books
from services.web_scraper.schemas import Book

router = APIRouter()

# -----------------------------
#         RANDOM BOOKS
# -----------------------------
@router.get("/books/random", response_model=List[Book])
def random_books(limit: int = Query(10, gt=0, le=50)):
    return get_random_books(limit=limit)


# -----------------------------
#          TOP BOOKS
# -----------------------------
@router.get("/books/top", response_model=List[Book])
def top_books(limit: int = Query(10, gt=0, le=50)):
    return get_top_popular_books(limit=limit)