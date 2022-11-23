import pytest
from driver import driver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class baseclass:
    def dropdown(self,locator,text):
        dropdown=Select(locator)
        dropdown.select_by_visible_text(text)


    # def explicitWait(self,text):
    # WebDriverWait(driver, timeout=10).until(document_initialised)
    # el = driver.find_element(By.TAG_NAME,"text")


