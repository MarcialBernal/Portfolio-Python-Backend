import os
import requests

RAWG_BASE_URL = "https://api.rawg.io/api"
API_KEY = os.getenv("RAWG_API_KEY")


def get_genres():
    url = f"{RAWG_BASE_URL}/genres"
    params = {"key": API_KEY}
    results = []

    while url:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        results.extend(data.get("results", []))
        url = data.get("next")
        
        params = {"key": API_KEY} if url else None

    return {"count": len(results), "next": None, "previous": None, "results": results}
