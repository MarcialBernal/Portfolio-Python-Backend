import random
import requests
from bs4 import BeautifulSoup
from typing import List
from services.web_scraper.schemas import Book

BASE_URL = "http://books.toscrape.com/"

# ============================================================
#                  WEBSITE DATA
# ============================================================
def get_all_book_urls() -> List[str]:
    """
    Recorre todas las páginas y devuelve los enlaces de todos los libros.
    """
    urls = []
    page = 1
    while True:
        url = f"{BASE_URL}catalogue/page-{page}.html"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod h3 a")
        if not books:
            break

        for book in books:
            link = book.get("href")
            # Ajustar enlaces relativos
            if not link.startswith("http"):
                link = BASE_URL + "catalogue/" + link.replace("../", "")
            urls.append(link)

        page += 1

    return urls


# ============================================================
#                  BOOK DATA
# ============================================================
def scrape_book(url: str) -> Book:
    """
    Extrae título, precio, imagen y disponibilidad de un libro.
    """
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.select_one("div.product_main h1").get_text(strip=True)
    price = soup.select_one("p.price_color").get_text(strip=True)
    image = soup.select_one("div.carousel img")["src"].replace("../../", BASE_URL)
    availability = "In stock" in soup.select_one("p.availability").get_text(strip=True)

    return Book(
        title=title,
        price=price,
        image_url=image,
        item_url=url,
        full=availability
    )


# ============================================================
#                      RANDOM BOOKS
# ============================================================
def get_random_books(limit: int = 10) -> List[Book]:
    """
    Devuelve 'limit' libros seleccionados aleatoriamente.
    """
    all_urls = get_all_book_urls()
    selected_urls = random.sample(all_urls, min(limit, len(all_urls)))
    return [scrape_book(url) for url in selected_urls]


# ============================================================
#                       TOP BOOKS
# ============================================================
def get_top_popular_books(limit: int = 10) -> List[Book]:
    """
    Devuelve los libros más populares según la posición en la web.
    """
    all_urls = get_all_book_urls()
    # Por simplicidad, los primeros N de la lista son "populares"
    selected_urls = all_urls[:limit]
    return [scrape_book(url) for url in selected_urls]
