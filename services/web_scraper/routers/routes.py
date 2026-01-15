from fastapi import APIRouter, Query
from typing import List
from services.web_scraper.crud import random_books, top_popular_books
from services.web_scraper.schemas import Book

router = APIRouter()

# -----------------------------
#         RANDOM BOOKS
# -----------------------------
@router.get("/books/random", response_model=List[Book])
def random(limit: int = Query(10, gt=0, le=50)):
    return random_books(limit=limit)


# -----------------------------
#          TOP BOOKS
# -----------------------------
@router.get("/books/top", response_model=List[Book])
def top(limit: int = Query(10, gt=0, le=50)):
    return top_popular_books(limit=limit)