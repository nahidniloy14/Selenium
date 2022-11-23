import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
# @pytest.mark.usefixtures("setup")
from pageObjects.addToCart import page2
from pageObjects.login import page1
from utilities.baseclass import baseclass


class TestOne(baseclass):
    def test_endToEnd(self):
        login1 = page1(self.driver)
        login1.username().send_keys("standard_user")
        login2 = page1(self.driver)
        login2.password().send_keys("secret_sauce")
        login3 = page1(self.driver)
        login3.login().click()

        atc1 = page2(self.driver)
        atc1.backpack().click()
        atc2 = page2(self.driver)
        atc2.bikelight().click()
        atc3 = page2(self.driver)
        atc3.container().click()

        # page3 = page2.checkout()

        # self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # self.driver.find_element(By.ID, "login-button").click()
        # self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        # self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
        # self.driver.find_element(By.XPATH, "//div[@class='shopping_cart_container']").click()
        # self.explicitWait("text") #is defined in baseclass
        # self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        # self.driver.find_element(By.NAME, "firstName").send_keys("Nahid Hassan")
        # self.driver.find_element(By.NAME, "lastName").send_keys("Niloy")
        # # self.driver.find_element(By.NAME, "postalCode").send_keys("1414")
        # self.driver.find_element(By.ID, "continue").click()
        # self.driver.execute_script("window.scrollTo(0, 200)")
        # time.sleep(5)
        #
        # message = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        # assert "$43.18" in message
        #
        # print("test case 1 passed")
        # self.driver.find_element(By.NAME, "finish").click()
        #
        # message = self.driver.find_element(By.TAG_NAME, "h2").text
        # assert "THANK YOU" in message
        # print("test case 2 passed")
