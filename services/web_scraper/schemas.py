from pydantic import BaseModel
from typing import Optional

class ScrapedItem(BaseModel):
    date: str
    title: str
    price: Optional[str]
    image_url: Optional[str]
    item_url: str
    full: bool