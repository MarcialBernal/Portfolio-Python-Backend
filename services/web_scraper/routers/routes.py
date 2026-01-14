from fastapi import APIRouter, Query
from services.web_scraper.crud import search
from typing import List
from services.web_scraper.schemas import ScrapedItem

router = APIRouter()

@router.get("/scraper", response_model=List[ScrapedItem])
def scrape_items(query: str = Query(..., min_length=2)):
    return search(query)