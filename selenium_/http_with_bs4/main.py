from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 60

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def setup_browser():
    options = webdriver.ChromeOptions()
    services = Service()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(
        service=services,
        options=options,
    )
    return browser

def perform_login(browser, username_val, password_val):
    browser.get('https://www.saucedemo.com/')
    
    username_field = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.NAME, 'user-name')
        )
    )
    ActionChains(browser).click(username_field).pause(0.5).perform()
    username_field.send_keys(username_val)

    password_field = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.NAME, 'password')
        )
    )
    ActionChains(browser).click(password_field).pause(0.5).perform()
    password_field.send_keys(password_val)

    login_button = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.NAME, 'login-button')
        )
    )
    ActionChains(browser).click(login_button).pause(1.5).perform()

def add_and_filter_items(browser):
    filter_class = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'product_sort_container')
        )
    )
    ActionChains(browser).click(filter_class).pause(0.5).perform()
    sort = Select(filter_class)
    sort.select_by_value('hilo')

    add_cart_high = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
        )
    )
    ActionChains(browser).click(add_cart_high).pause(0.5).perform()

    add_cart_low = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.NAME, 'add-to-cart-sauce-labs-onesie')
        )
    )
    ActionChains(browser).click(add_cart_low).pause(0.5).perform()

def perform_logout(browser):
    menu = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.ID, 'react-burger-menu-btn')
        )
    )
    ActionChains(browser).click(menu).pause(1.0).perform()

    logout = WebDriverWait(browser, WAIT_TIME).until(
        EC.presence_of_element_located(
            (By.ID, 'logout_sidebar_link')
        )
    )
    ActionChains(browser).click(logout).pause(1.0).perform()

def run_e2e_test():
    browser = setup_browser()
    try:
        perform_login(browser, 'standard_user', 'secret_sauce')
        add_and_filter_items(browser)
        perform_logout(browser)
        print('Teste E2E finalizado com sucesso!')
    except Exception as e:
        print(f'Teste falhou: {e}')
    finally:
        sleep(2)
        browser.quit()

if __name__ == '__main__':
    run_e2e_test()
