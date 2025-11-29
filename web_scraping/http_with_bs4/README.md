# HTTP + BeautifulSoup Scraping Demo

This project is a small web scraping exercise using `requests` and `BeautifulSoup` to parse a local HTML page served on `http://localhost:3333/`.

## Files

- `main.py`  
  Main Python script. It sends an HTTP GET request to the local server, reads the HTML as text and bytes, and parses it with BeautifulSoup using the `html.parser` engine.

- `site/index.html`  
  Static HTML file representing the page that will be scraped. It is served locally on port `3333`.

- `site/style.css`  
  Stylesheet used by `index.html` to define the layout and visual appearance of the page.

## main.py (raw code)

```
import requests
from bs4 import BeautifulSoup
url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
```

## What the script does

- Sends a GET request to `http://localhost:3333/` using the `requests` library.  
- Reads the server response both as a Unicode string (`response.text`) and as bytes (`response.content`).  
- Parses the HTML twice with BeautifulSoup:
  - First using the raw text and the `html.parser` backend.
  - Then using the raw bytes with explicit `from_encoding='utf-8'` to ensure proper character decoding.

***You can extend this script to query specific elements from the parsed HTML (titles, links, product cards, etc.) and process them according to your scraping goal.***

---

If you are setting this project up for the first time, make sure to read `tutorial.txt`.
It contains a detailed guide on creating the virtual environment, starting the HTTP server, and running the script.
