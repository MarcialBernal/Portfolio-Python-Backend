from services.web_scraper.client import MercadoLibreClient
from datetime import datetime


ml = MercadoLibreClient()


def search_items(query: str, limit: int = 10):
    results = ml.search(query, limit=limit)

    mapped = []

    for item in results:
        mapped.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "title": item.get("title"),
            "price": item.get("price"),
            "image_url": item.get("thumbnail"),
            "item_url": item.get("permalink"),
            "full": item.get("shipping", {}).get("logistic_type") == "fulfillment",
        })

    return mapped