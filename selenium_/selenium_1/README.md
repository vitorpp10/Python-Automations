# SauceDemo Login and Sorting Automation

<p align="center">
  <!-- Linguagem -->
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />

  <!-- IDE -->
  <img src="https://img.shields.io/badge/IDE-VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode&logoColor=white" />

  <!-- Ferramentas / Stack extra -->
  <img src="https://img.shields.io/badge/Automation-Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Version_Control-Git-F05032?style=for-the-badge&logo=git&logoColor=white" />

  <!-- Status do projeto -->
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

This project is a simple Selenium WebDriver exercise in Python that automates a full login and product-sorting flow on the demo e-commerce site <https://www.saucedemo.com>.

## What the script does

- Opens Google Chrome in incognito mode and navigates to the SauceDemo login page.
- Logs in using the demo credentials `standard_user` and `secret_sauce`.
- Selects the product sort option **"Price (high to low)"** using the dropdown with class `product_sort_container`.
- Adds the most expensive item (`sauce-labs-fleece-jacket`) and the cheapest item (`sauce-labs-onesie`) to the cart.
- Opens the burger menu and logs out of the application, then waits before closing the browser.

## Project structure

- `drivers/chromedriver.exe` – ChromeDriver binary path used by Selenium.
- `your_script.py` – Main automation script (the file containing the code above).
- `venv/` – Optional virtual environment folder for dependency management.

## Requirements

- Python 3.10+
- Google Chrome installed
- Matching version of ChromeDriver placed in `drivers/chromedriver.exe`
- Packages:
  - `selenium`

Install dependencies:

`pip install selenium`

## How to run

1. Clone or download this project.
2. Ensure `chromedriver.exe` is inside the `drivers` folder at the project root.
3. (Optional) Activate your virtual environment.
4. Run the script: `python your_script.py`


***The browser will open, perform the login, sort products by price, add two items to the cart, open the menu, log out, and then stay open for `WAIT_TIME` seconds before the script ends.***