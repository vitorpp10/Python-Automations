from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 60

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

options = webdriver.ChromeOptions()
services = Service()
options.add_argument("--incognito")
browser = webdriver.Chrome(
    service=services,
    options=options,
)

browser.get('https://www.saucedemo.com/')

username = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.NAME, 'user-name')
    )
)
ActionChains(browser).click(username).pause(1.5).perform()
username.send_keys('standard_user')

password = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.NAME, 'password')
    )
)
ActionChains(browser).click(password).pause(1.5).perform()
password.send_keys('secret_sauce')

login = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.NAME, 'login-button')
    )
)
ActionChains(browser).click(login).pause(1.5).perform()

filter_class = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'product_sort_container')
    )
)
ActionChains(browser).click(filter_class).pause(1.5).perform()
sort = Select(filter_class)
sort.select_by_value('hilo')

add_cart_high = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
    )
)
ActionChains(browser).click(add_cart_high).pause(1.5).perform()

add_cart_low = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.NAME, 'add-to-cart-sauce-labs-onesie')
    )
)
ActionChains(browser).click(add_cart_low).pause(1.5).perform()

menu = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.ID, 'react-burger-menu-btn')
    )
)
ActionChains(browser).click(menu).pause(1.5).perform()

logout = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
        (By.ID, 'logout_sidebar_link')
    )
)
ActionChains(browser).click(logout).pause(1.5).perform()

sleep(WAIT_TIME)