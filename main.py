import requests

from book_details.scrape_details import scrape_details
from catalogue.scrape_catalogue import scrape_catalogue


def main():
    books = scrape_catalogue()
    # scrape_categories()

    with requests.session() as session:
        detailed_books = []

        for book in books:
            details = scrape_details(book.url, session)
            detailed_books.append(details)


if __name__ == "__main__":
    main()
