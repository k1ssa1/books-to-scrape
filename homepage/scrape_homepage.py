from bs4 import BeautifulSoup
import requests


def scrp_homepage():

    url = "https://books.toscrape.com/index.html"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    books_collection = []

    books = soup.find_all("article", class_="product_pod")
    for b in books:
        img_src = b.find("img", class_="thumbnail").get("src")
        img_alt = b.find("img", class_="thumbnail").get("alt")
        title = b.h3.text
        price = b.find("p", class_="price_color").text.replace("Â£", "")
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

        books_collection.append(
            {
                "title": title,
                "availability": availability,
                "price": price,
                "rating": str(rating) + "/5",
                "image": {"description": img_alt, "src": img_src},
            }
        )

    print(books_collection)
