import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from urllib.parse import urljoin

class Image(BaseModel):
    img_src: str
    img_description: str

class Book(BaseModel):
    title: str
    price: float
    availability: str
    description: str | None
    code: str
    bookType: str
    priceExclTax: float
    priceInclTax: float
    tax: float
    reviewCount: int
    image: Image

def scrape_details(url: str, session: requests.Session):

    base_url = "https://books.toscrape.com/catalogue/"

    absolute_url = urljoin(base_url, url)

    res = session.get(absolute_url, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    details = soup.find("article", class_="product_page")
    img_section = details.find("div", class_="item active")
    img_src = img_section.find("img").get("src")
    img_description = img_section.find("img").get("alt")
    header = details.find("div", class_="col-sm-6 product_main")
    title = header.h1.text
    price = float(header.p.text.replace("Â£", ""))
    availability = details.find("p", class_="instock availability").text.strip()
    description_section = details.find("div", id="product_description")
    if description_section:
        description = description_section.find_next_sibling("p").text.strip()
    else:
        description = None
    information_table = details.find("table", class_="table table-striped")
    row_selector = information_table.find_all("tr")
    product_code = row_selector[0].find("td").text.strip()
    product_type = row_selector[1].find("td").text.strip()
    price_excl_tax = float(row_selector[2].find("td").text.replace("Â£", ""))
    price_incl_tax = float(row_selector[3].find("td").text.replace("Â£", ""))
    tax = float(row_selector[4].find("td").text.replace("Â£", ""))
    review_count = int(row_selector[6].find("td").text.strip())

    book = Book(
        title=title,
        price=price,
        availability=availability,
        description=description,
        code=product_code,
        bookType=product_type,
        priceExclTax= price_excl_tax,
        priceInclTax= price_incl_tax,
        tax= tax,
        reviewCount= review_count,
        image= {
            "img_src": img_src,
            "img_description": img_description
        }
    )

    return book