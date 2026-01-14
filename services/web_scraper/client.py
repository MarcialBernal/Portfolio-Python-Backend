import requests
from services.web_scraper.auth import MercadoLibreAuth


class MercadoLibreClient:
    BASE_URL = "https://api.mercadolibre.com"

    def __init__(self):
        self.auth = MercadoLibreAuth()

    def _headers(self):
        token = self.auth.get_access_token()
        return {"Authorization": f"Bearer {token}"}

    def search(self, query: str, limit: int = 10):
        r = requests.get(
            f"{self.BASE_URL}/sites/MLM/search",
            headers=self._headers(),
            params={"q": query, "limit": limit},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()["results"]

    def get_item(self, item_id: str):
        r = requests.get(
            f"{self.BASE_URL}/items/{item_id}",
            headers=self._headers(),
            timeout=10,
        )
        r.raise_for_status()
        return r.json()
