🐉 Dragon Find Quotes: CLI Scraper & Manager

<div align="center">
<img src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://www.google.com/search?q=https://img.shields.io/badge/DATABASE-SQLite3-003B57%3Fstyle%3Dfor-the-badge%26logo%3Dsqlite%26logoColor%3Dwhite" />
<img src="https://img.shields.io/badge/PARSING-BeautifulSoup-4B8BBE?style=for-the-badge" />
<img src="https://img.shields.io/badge/HTTP-Requests-FF6C37?style=for-the-badge" />
<img src="https://www.google.com/search?q=https://img.shields.io/badge/UX-Colorama_CLI-e01e5a%3Fstyle%3Dfor-the-badge" />
</div>

Phase 2 Project: Advanced Automation & Data Persistence.

Dragon Find Quotes is not just a scraper; it is a full-featured Command Line Interface (CLI) Application. It automates the extraction of quotes from http://quotes.toscrape.com/, allows interactive pagination, and implements a local database system to manage user favorites.

🚀 Key Features

🕷️ Dynamic Scraping: Fetches quotes, authors, and tags in real-time using requests and BeautifulSoup.

🔄 Smart Pagination: Detects "Next Page" links automatically, allowing the user to traverse the entire website via the terminal.

💾 Data Persistence (SQLite): Integrated SQL database to save, view, and delete favorite quotes. Data persists even after the program closes.

🎨 Dragon UX Engine: A custom interface layer using colorama for typing effects, dragon-themed styling, and robust error handling loops.

📂 Project Structure

dragon_quotes.py The core application. It handles:

HTTP Logic: Connecting to the web server with timeouts and status checks.

Parsing Logic: Extracting data structure from raw HTML.

Database Logic: CRUD operations (Create, Read, Delete) for favorites using sqlite3.

UI Logic: Managing the infinite loop, menus, and user input sanitization.

favorites.db An SQLite database file (automatically generated on first run). It stores your saved quotes relationally.

💻 Code Highlights

1. The Scraper Engine (Pagination Aware)

The script uses a global state to track navigation links, turning a static page into a navigable stream.

def main_scraper(url):
    global NEXT_PAGE
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        parsed_html = BeautifulSoup(response.text, 'html.parser')

        # Logic to find the "Next" button dynamic link
        next_button = parsed_html.find('li', class_='next')
        NEXT_PAGE = next_button.find('a')['href'] if next_button else None
        
        return parsed_html.find_all('div', class_='quote')
    except Exception as e:
        sys.exit(f"Critical Error: {e}")


2. SQL Persistence Layer

Instead of simple text files, this project uses structured SQL queries to ensure data integrity.

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


⚙️ Installation & Usage

Clone the repository:

git clone [https://github.com/vitor-de-padua/python-automations.git](https://github.com/vitor-de-padua/python-automations.git)
cd python-automations/web_scraping


Install dependencies:

pip install requests beautifulsoup4 colorama


(Note: sqlite3 is built-in with Python, no installation required.)

Run the Dragon:

python dragon_quotes.py
