import requests

from book_details.scrape_details import scrape_details
from books_by_cat.scrape_books_by_category import scrape_books_by_category
from categories_list.scrape_categories_list import scrape_categories_list
from catalogue.scrape_catalogue import scrape_catalogue

import csv


def main():

    scrape_books_by_category()

    books_in_catalogue = scrape_catalogue()

    with open(r"C:\Users\HP\Downloads\books_catalogue.csv", 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "title",
            "price",
            "availability",
            "rating",
            "image description",
            "image src",
            "url"
        ])
        for book in books_in_catalogue:
            writer.writerow([book.title, book.price, book.availability, book.rating, book.image.description, book.image.src, book.url])

    with requests.session() as session:
        detailed_books = []

        for book in books_in_catalogue:
            details = scrape_details(book.url, session)
            detailed_books.append(details)

    category_list = scrape_categories_list()

    with open(r"C:\Users\HP\Downloads\category_list.csv", 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name"])
        for cat in category_list:
            writer.writerow([cat.name])


if __name__ == "__main__":
    main()
