# Dragon Find Quotes: CLI Scraper & Manager

![Python](https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Database SQLite3](https://img.shields.io/badge/DATABASE-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Parsing BeautifulSoup](https://img.shields.io/badge/PARSING-BeautifulSoup-4B8BBE?style=for-the-badge)
![HTTP Requests](https://img.shields.io/badge/HTTP-Requests-FF6C37?style=for-the-badge)
![UX Colorama CLI](https://img.shields.io/badge/UX-Colorama_CLI-e01e5a?style=for-the-badge)

Phase 2 Project: Advanced Automation & Data Persistence.

**Dragon Find Quotes** is a full-featured Command Line Interface (CLI) application. It automates the extraction of quotes from `http://quotes.toscrape.com/`, allows interactive pagination, and implements a local database system to manage user favorites.

## Key Features

- Dynamic scraping: Fetches quotes, authors, and tags in real time using `requests` and `BeautifulSoup`.
- Smart pagination: Detects `"Next Page"` links automatically, allowing the user to traverse the entire website via the terminal.
- Data persistence (SQLite): Integrated SQL database to save, view, and delete favorite quotes. Data persists even after the program closes.
- Dragon UX Engine: A custom interface layer using `colorama` for typing effects, themed styling, and robust error-handling loops.

## Project Structure

- `dragon_quotes.py`  
  Core application script. It handles:
  - **HTTP logic**: Connecting to the web server with timeouts and status checks.
  - **Parsing logic**: Extracting structured data from raw HTML.
  - **Database logic**: CRUD operations (Create, Read, Delete) for favorites using `sqlite3`.
  - **UI logic**: Managing the main loop, menus, and user input sanitization.

- `favorites.db`  
  SQLite database file (automatically generated on first run). It stores saved quotes in a relational structure.

## Code Highlights

### 1. Scraper Engine (Pagination-Aware)

The script uses a global state to track navigation links, turning a static page into a navigable stream:

def main_scraper(url):
global NEXT_PAGE
try:
response = requests.get(url, timeout=5)
response.raise_for_status()
parsed_html = BeautifulSoup(response.text, 'html.parser')

text
    # Logic to find the "Next" button dynamic link
    next_button = parsed_html.find('li', class_='next')
    NEXT_PAGE = next_button.find('a')['href'] if next_button else None

    return parsed_html.find_all('div', class_='quote')
except Exception as e:
    sys.exit(f"Critical Error: {e}")
text

### 2. SQL Persistence Layer

Instead of simple text files, this project uses structured SQL queries to ensure data integrity:

def setup_db():
conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()
# Creates table only if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS favorites (
id INTEGER PRIMARY KEY,
quote TEXT UNIQUE,
author TEXT
)
''')
conn.commit()

text

## Installation & Usage

1. Clone the repository:

git clone https://github.com/vitor-de-padua/python-automations.git
cd python-automations/web_scraping

text

2. Install dependencies:

pip install requests beautifulsoup4 colorama

text

> Note: `sqlite3` is built into Python, so no extra installation is required.

3. Run the application:

python dragon_quotes.py
