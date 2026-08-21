from categories.scrape_categories import scrape_categories
from homepage.scrape_homepage import scrape_catalogue


def main():
    scrape_catalogue()
    scrape_categories()


if __name__ == "__main__":
    main()
