import requests

from book_details.scrape_details import scrape_details
from books_by_cat.scrape_books_by_category import scrape_books_by_category
from categories_list.scrape_categories_list import scrape_categories_list
from catalogue.scrape_catalogue import scrape_catalogue


def main():

    scrape_books_by_category()

    books = scrape_catalogue()

    with requests.session() as session:
        detailed_books = []

        for book in books:
            details = scrape_details(book.url, session)
            detailed_books.append(details)

    scrape_categories_list()

if __name__ == "__main__":
    main()
