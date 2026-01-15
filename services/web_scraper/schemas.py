from pydantic import BaseModel

class Book(BaseModel):
    title: str
    price: str
    rating: str
    image_url: str
    book_url: str