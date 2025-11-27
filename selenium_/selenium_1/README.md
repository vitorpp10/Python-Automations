<h1 align="center"> SauceDemo Login E2E</h1>

<div align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/IDE-VS_CODE-0078D4?style=for-the-badge&logo=visualstudiocode&logoColor=white" />
  <img src="https://img.shields.io/badge/AUTOMATION-SELENIUM-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/VERSION_CONTROL-GIT-F05032?style=for-the-badge&logo=git&logoColor=white" />
</div>

<p align="center">
  End‑to‑end Selenium test that logs into SauceDemo, sorts products, adds items to the cart and logs out.
</p>

---

## Overview

This project is a small Selenium WebDriver E2E test written in Python.  
It follows a **function‑based structure** to keep each action of the flow isolated and easy to reuse:

- `setup_browser()` – starts a Chrome browser in incognito mode.  
- `perform_login()` – logs into SauceDemo with `standard_user` / `secret_sauce`.  
- `add_and_filter_items()` – sorts products by **Price (high to low)** and adds two items to the cart.  
- `perform_logout()` – opens the burger menu and logs out.  
- `run_e2e_test()` – orchestrates the full test and handles success/failure.

---

## Flow Details

The script performs the following end‑to‑end scenario:

1. Open Chrome in **incognito** mode.  
2. Navigate to `https://www.saucedemo.com/`.  
3. Wait for the username and password fields, type credentials and click the login button.  
4. Use the `product_sort_container` dropdown to select `hilo` (**Price (high to low)**).  
5. Add:
   - `sauce-labs-fleece-jacket` (most expensive item).  
   - `sauce-labs-onesie` (cheapest item).  
6. Open the burger menu and click **Logout**.  
7. Print a success or failure message and close the browser gracefully.

All interactions use `WebDriverWait`, `expected_conditions` and `ActionChains` for more reliable and realistic automation.

---

## Project Structure

saucedemo_login/
├── drivers/
│ └── chromedriver.exe
├── venv/ (optional – virtual environment)
└── main.py (script with the functions and E2E flow)

text

- `drivers/chromedriver.exe` – ChromeDriver binary used by Selenium.  
- `main.py` – contains `setup_browser`, `perform_login`, `add_and_filter_items`, `perform_logout` and `run_e2e_test`.  

---

## Requirements

- Python **3.10+**  
- Google Chrome installed  
- Matching version of **ChromeDriver** placed in `drivers/chromedriver.exe`  
- Python package:
  - `selenium`

Install the dependency:

pip install selenium

text

---

## How to Run

1. **Clone or download** this project.  
2. Make sure `chromedriver.exe` is inside the `drivers` folder at the project root.  
3. (Optional) Create and activate a virtual environment.  
4. Run the script:

python main.py

text

If everything goes well, you should see a message in the terminal:

Teste E2E finalizado com sucesso!

text

The browser will open, log in, sort by price, add two products to the cart, log out and then close after a short delay.

---

<p align="center">
  <img src="https://img.shields.io/badge/Made_with❤️_by-Vitor_de_Padua-blueviolet?style=for-the-badge" />
</p>
