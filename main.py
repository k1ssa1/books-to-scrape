import requests

from book_details.scrape_details import scrape_details
from books_by_cat.scrape_books_by_category import scrape_books_by_category
from categories_list.scrape_categories_list import scrape_categories_list
from catalogue.scrape_catalogue import scrape_catalogue


def main():

    scrape_books_by_category()


if __name__ == "__main__":
    main()
