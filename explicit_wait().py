#Explicit Wait time is applied only to those elements which are intended by us.
# It is recommended to use when the elements are taking long time to load and also for verifying the property of the element like(visibilityOfElementLocated, elementToBeClickable,elementToBeSelec

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait


def document_initialised(driver):
    return driver.execute_script("return initialised")
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2Fl")
el = WebDriverWait(driver, timeout=3).until(lambda d: d.driver.find_element(By.NAME,"Email").send_keys("niloy123@yourstore.com"))
assert el.text == "Hello from JavaScript!"
