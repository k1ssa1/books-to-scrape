import requests
from bs4 import BeautifulSoup
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
    url: str

def scrape_books_by_category():

    books_collection = []

    base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/page-'
    extension = '.html'

    with requests.session() as session:
        for page in range(1,3):
            absolute_path = base_url + str(page) + extension

            res = session.get(absolute_path, timeout=10)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'html.parser')
            books = soup.find_all("article", class_="product_pod")
            for b in books:
                img_src = b.find("img", class_="thumbnail").get("src")
                img_alt = b.find("img", class_="thumbnail").get("alt")
                title = b.h3.text
                price = float(b.find("p", class_="price_color").text.replace("Â£", ""))
                availability = b.find("p", class_="instock availability").text.strip()
                rating = b.find("p", class_="star-rating").get("class")[1]
                url = b.h3.find("a").get("href")
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
                    url=url,
                )

                books_collection.append(book)

        print(books_collection)

        return books_collection

