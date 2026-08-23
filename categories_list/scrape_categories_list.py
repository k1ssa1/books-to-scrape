import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel


class Category(BaseModel):
    name: str


def scrape_categories_list():
    with requests.session() as session:
        url = "https://books.toscrape.com/index.html"
        res = session.get(url, timeout=10)

        soup = BeautifulSoup(res.text, "html.parser")
        aside_menu = soup.find("ul", class_="nav nav-list")
        links = aside_menu.find_all("a")

        category_list = []

        for l in links:
            extracted_name = l.text.strip()
            category = Category(name=extracted_name)
            category_list.append(category)

    return category_list
