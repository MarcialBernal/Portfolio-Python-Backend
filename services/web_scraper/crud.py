from services.web_scraper.book_scraper import get_random_books, get_top_popular_books
from services.web_scraper.schemas import Book
from typing import List
import random

def random_books(limit: int = 10) -> List[Book]:
    return get_random_books(limit=limit)


def top_popular_books(limit: int = 10) -> List[Book]:
    return get_top_popular_books(limit=limit) 