import requests

from book_details.scrape_details import scrape_details
from books_by_cat.scrape_books_by_category import scrape_books_by_category
from categories_list.scrape_categories_list import scrape_categories_list
from catalogue.scrape_catalogue import scrape_catalogue

import csv


def main():

    # load book main details in mystery category to dedicated CSV file

    mystery_books = scrape_books_by_category()

    with open(
        r"C:\Users\HP\Downloads\mystery_books.csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        wr1 = csv.writer(csvfile)
        wr1.writerow(
            [
                "title",
                "price",
                "availability",
                "rating",
                "image description",
                "image src",
                "url",
            ]
        )
        for mb in mystery_books:
            wr1.writerow(
                [
                    mb.title,
                    mb.price,
                    mb.availability,
                    mb.rating,
                    mb.image.description,
                    mb.image.src,
                    mb.url,
                ]
            )

    # load book main details across all catalogue pages to dedicated CSV file

    books_in_catalogue = scrape_catalogue()

    with open(
        r"C:\Users\HP\Downloads\books_catalogue.csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        wr2 = csv.writer(csvfile)
        wr2.writerow(
            [
                "title",
                "price",
                "availability",
                "rating",
                "image description",
                "image src",
                "url",
            ]
        )
        for book in books_in_catalogue:
            wr2.writerow(
                [
                    book.title,
                    book.price,
                    book.availability,
                    book.rating,
                    book.image.description,
                    book.image.src,
                    book.url,
                ]
            )

    # load book extra details across all catalogue pages to dedicated CSV file

    with requests.session() as session:
        detailed_books = []

        for book in books_in_catalogue:
            details = scrape_details(book.url, session)
            detailed_books.append(details)

        with open(
            r"C:\Users\HP\Downloads\book_details.csv", "w", newline="", encoding="utf-8"
        ) as csvfile:
            wr3 = csv.writer(csvfile)
            wr3.writerow(
                [
                    "title",
                    "price",
                    "availability",
                    "description",
                    "code",
                    "bookType",
                    "priceExclTax",
                    "priceInclTax",
                    "tax",
                    "reviewCount",
                    "imageSrc",
                    "imageDesc",
                ]
            )
            for d in detailed_books:
                wr3.writerow(
                    [
                        d.title,
                        d.price,
                        d.availability,
                        d.description,
                        d.code,
                        d.bookType,
                        d.priceExclTax,
                        d.priceInclTax,
                        d.tax,
                        d.reviewCount,
                        d.image.img_src,
                        d.image.img_description,
                    ]
                )

    # load all categories to dedicated CSV file

    category_list = scrape_categories_list()

    with open(
        r"C:\Users\HP\Downloads\category_list.csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        wr4 = csv.writer(csvfile)
        wr4.writerow(["name"])
        for cat in category_list:
            wr4.writerow([cat.name])


if __name__ == "__main__":
    main()
