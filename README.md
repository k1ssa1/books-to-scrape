# Books to Scrape

## Objective

For educational purposes only.

This project scrapes the demo website [Books to Scrape](https://books.toscrape.com/) to demonstrate fundamental web scraping concepts using Python.

## Project Structure

```text
books-to-scrape/
├── books_details/
│   └── scrape_details.py
├── books_by_cat/
│   └── scrape_books_by_category.py
├── catalogue/
│   └── scrape_catalogue.py
├── categories_list/
│   └── scrape_categories_list.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Project Modules

The project is organized into independent modules, with each module responsible for a specific web scraping task.

### `books_by_cat/`

**Purpose:** Scrape the main information of books belonging to a specific category.

The module navigates through the selected category pages and extracts:

- Book title
- Price
- Availability
- Rating
- Image description
- Image URL
- Book URL

The extracted data is validated using Pydantic models before being returned as a collection of `Book` objects.

---

### `catalogue/`

**Purpose:** Scrape the main information of books across the entire catalogue.

The module handles catalogue pagination and extracts the same basic book information as the category scraper:

- Book title
- Price
- Availability
- Rating
- Image description
- Image URL
- Book URL

This module demonstrates pagination and systematic traversal of multiple catalogue pages.

---

### `book_details/`

**Purpose:** Scrape additional information from individual book detail pages.

The module receives a book URL and extracts more detailed information, including:

- Book title
- Price
- Availability
- Description
- Product code
- Book type
- Price excluding tax
- Price including tax
- Tax
- Number of reviews
- Image information

A `requests.Session` is reused when processing multiple books to maintain a persistent HTTP session.

---

### `categories_list/`

**Purpose:** Extract the list of available book categories from the website.

The module navigates the site's category navigation menu and extracts each category name.

The resulting collection is validated using a Pydantic `Category` model.

---

### `main.py`

**Purpose:** Serve as the entry point and coordinate the scraping and loading operations.

The main module:

1. Calls the appropriate scraping modules.
2. Receives validated Pydantic objects.
3. Writes the extracted data into dedicated CSV files.

The generated datasets are:

- `mystery_books.csv` — books from the Mystery category.
- `books_catalogue.csv` — books from the complete catalogue.
- `book_details.csv` — detailed information for catalogue books.
- `category_list.csv` — available book categories.

This separation keeps the scraping logic independent from the execution and CSV loading logic.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/k1ssa1/books-to-scrape.git
cd books-to-scrape


### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the requirements

```bash
pip install -r requirements.txt
```

## Run

Run the application from your IDE or from the terminal:

```bash
python main.py
```
