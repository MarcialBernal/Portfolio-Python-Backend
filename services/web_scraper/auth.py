import os
import time
import requests


class MercadoLibreAuth:
    TOKEN_URL = "https://api.mercadolibre.com/oauth/token"

    def __init__(self):
        self.client_id = os.getenv("ML_CLIENT_ID")
        self.client_secret = os.getenv("ML_CLIENT_SECRET")
        self.refresh_token = os.getenv("ML_REFRESH_TOKEN")

        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise RuntimeError("Faltan variables de entorno de MercadoLibre")

        self._access_token = None
        self._expires_at = 0

    def get_access_token(self) -> str:
        
        if self._access_token and time.time() < self._expires_at:
            return self._access_token

        return self._refresh_token()

    def _refresh_token(self) -> str:
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "refresh_token": self.refresh_token,
            },
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        self._access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self._expires_at = time.time() + data["expires_in"] - 60

        return self._access_token
