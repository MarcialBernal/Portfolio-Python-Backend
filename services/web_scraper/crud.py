from services.web_scraper.book_scraper import scrape_books
from services.web_scraper.schemas import Book
from typing import List
import random

def get_random_books(limit: int = 10) -> List[Book]:
    books_raw = scrape_books()
    books_sample = random.sample(books_raw, min(len(books_raw), limit))
    return [Book(**book) for book in books_sample]


def get_top_popular_books(limit: int = 10) -> List[Book]:
    books_raw = scrape_books(top_popular=True)
    return [Book(**book) for book in books_raw[:limit]]