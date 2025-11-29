# Dragon Find Quotes 🐉

<div align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTTP-requests-FF6C37?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PARSING-BeautifulSoup-4B8BBE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CLI_UX-Colorama-e01e5a?style=for-the-badge" />
</div>

This project is an interactive Command Line Interface (CLI) tool that scrapes quotes from `http://quotes.toscrape.com/`. It combines web scraping logic with a stylized "Dragon" theme, offering pagination and error handling. [web:1]

## Files

- `dragon_quotes.py`  
  Main Python script. It handles HTTP requests, HTML parsing, and the interactive loop that displays the menu, processes user input, and manages page navigation.

## `dragon_quotes.py` (core logic)

```
def main_scraper(url):
global NEXT_PAGE

try:
  response = requests.get(url, timeout=5)
  response.raise_for_status()
  parsed_html = BeautifulSoup(response.text, 'html.parser')
  
  all_quotes = parsed_html.find_all('div', class_='quote')
  next_button = parsed_html.find('li', class_='next')
  
  if next_button:
    NEXT_PAGE = next_button.find('a')['href']
  else:
    NEXT_PAGE = None
      
  return all_quotes
except Exception as e:
    sys.exit()
```

## What the script does

- Sends GET requests to `http://quotes.toscrape.com/` using the `requests` library. [web:1]
- Parses the HTML response using `BeautifulSoup` to extract quote text, authors, and pagination links. [web:5]
- Implements a paginated navigation system, allowing the user to move to the "Next Page" directly from the terminal.
- Provides a robust CLI UX using `colorama` for colors, typing effects (`p()` function), and conditional screen clearing.
- Handles errors gracefully, ensuring the application does not crash on invalid inputs or connection issues.

## Possible extensions

***You can extend this script to include features such as:***

- *Saving favorite quotes to a database (SQLite)*.
- *Filtering quotes by specific tags*.

## Setup

If you are setting up this project for the first time, install the required libraries: `pip install requests beautifulsoup4 colorama`

---

![Made_with_heart](https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge)
