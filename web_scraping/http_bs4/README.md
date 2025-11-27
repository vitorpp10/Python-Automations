# HTTP + BeautifulSoup Scraping Demo

<div align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTTP-requests-FF6C37?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PARSING-BeautifulSoup-4B8BBE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/WEB_SCRAPING-Local_HTML-008000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/IDE-VS_CODE-0078D4?style=for-the-badge&logo=visualstudiocode&logoColor=white" />
  <img src="https://img.shields.io/badge/VERSION_CONTROL-GIT-F05032?style=for-the-badge&logo=git&logoColor=white" />
</div>

This project is a small web scraping exercise using `requests` and `BeautifulSoup` to parse a local HTML page served on `http://localhost:3333/`.

## Files

- `main.py`  
  Main Python script. It sends an HTTP GET request to the local server, reads the HTML as text and bytes, and parses it with BeautifulSoup using the `html.parser` engine.

- `site/index.html`  
  Static HTML file representing the page that will be scraped. It is served locally on port `3333`.

- `site/style.css`  
  Stylesheet used by `index.html` to define the layout and visual appearance of the page.

## main.py (raw code)

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

text

## What the script does

- Sends a GET request to `http://localhost:3333/` using the `requests` library.  
- Reads the server response both as a Unicode string (`response.text`) and as bytes (`response.content`).  
- Parses the HTML twice with BeautifulSoup:
  - First using the raw text and the `html.parser` backend.
  - Then using the raw bytes with explicit `from_encoding='utf-8'` to ensure proper character decoding.

You can extend this script to query specific elements from the parsed HTML (titles, links, product cards, etc.) and process them according to your scraping goal.
