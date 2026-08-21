from bs4 import BeautifulSoup
import requests

from pydantic import BaseModel


class Image(BaseModel):
    description: str
    src: str


class Book(BaseModel):
    title: str
    price: float
    availability: str
    rating: int
    image: Image


def scrape_catalogue():

    baseurl = "https://books.toscrape.com/catalogue/page-"
    extension = '.html'

    books_collection = []

    with requests.Session() as session:
        for page in range(1, 51):

            res = session.get(baseurl + str(page) + extension, timeout=10)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, "html.parser")

            books = soup.find_all("article", class_="product_pod")
            for b in books:
                img_src = b.find("img", class_="thumbnail").get("src")
                img_alt = b.find("img", class_="thumbnail").get("alt")
                title = b.h3.text
                price = float(b.find("p", class_="price_color").text.replace("Â£", ""))
                availability = b.find("p", class_="instock availability").text.strip()
                rating = b.find("p", class_="star-rating").get("class")[1]
                if rating == "One":
                    rating = 1
                elif rating == "Two":
                    rating = 2
                elif rating == "Three":
                    rating = 3
                elif rating == "Four":
                    rating = 4
                elif rating == "Five":
                    rating = 5

                book = Book(
                    title=title,
                    price=price,
                    availability=availability,
                    rating=rating,
                    image={"description": img_alt, "src": img_src},
                )

                books_collection.append(book)

    return books_collection
