#if we declare our fixture that fixture will be present to all testcases present in that particular fixture

import pytest
from _pytest import python
from selenium import webdriver


@pytest.fixture(scope="class")

def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver#assinging local driver of this fixture to the class driver
    yield
    driver.close()
