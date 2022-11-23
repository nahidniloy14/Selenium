import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

from TestData.HomePageData import HomePageData #package.filename.classname
from pageObjects.homePage import HomePage
from utilities.baseclass import baseclass


class TestHomePage(baseclass):
    def test_formSubmission(self, getData):

        # driver.find_element(By.NAME,"name").send_keys("Nahid Hassan Niloy")
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Nahid Hassan Niloy")
        homepage1 = HomePage(self.driver)
        #homepage1.getname().send_keys(getData[0])
        homepage1.getname().send_keys(getData["name"])

        homepage2 = HomePage(self.driver)
        #method 1

        # dropdown=Select(homepage2.getgender())
        # dropdown.select_by_visible_text("Female")
        #method 2
        # # check base class for reuseable function
        # self.dropdown(homepage2.getgender(),"Male")
        #method 3
        #self.dropdown(homepage2.getgender(),getData[2] )
        self.driver.refresh() #to input multiple values
        #method4
        self.dropdown(homepage2.getgender(), getData["gender"])


        # @pytest.fixture(params=[("Nahid Hassan Niloy","Male"),("Surangana","Female")])
        # def getData(self,request):
        #     return request.param

        @pytest.fixture(params=HomePageData.test_HomePage_Data)
        def getData(self, request):
            return request.param

        # driver.find_element(By.XPATH, "//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys(
        #     "nahidniloy894@gmail.com")
        # # driver.find_element(By.ID,"exampleInputPassword1").send_keys("nahidniloy1414")
        # driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("nahidniloy1414")
        #
        # driver.find_element(By.ID, "exampleCheck1").click()
        # driver.find_element(By.XPATH, "//*[contains(@name,'bday')]").send_keys("09/20/1996")
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # # print(driver.find_element(By.CLASS_NAME,"alert-success").text)#use only one class name
        # print(driver.find_element(By.CSS_SELECTOR, ".alert-success").text)  # use only one class name
        # # *is a regular expression, it looks for a subtext which does not require 100% match
        # # print(driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text)
        # driver.find_element(By.XPATH, "//*[contains(@name,'bday')]").send_keys("09/20/1996")
        # time.sleep(3)
        # driver.find_element(By.LINK_TEXT, "Shop").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//a[text()='iphone X']").click()
        # # driver.quit()
        #
        # driver.find_element(By.ID,"exampleFormControlSelect1").click()
        # select class provides the method to handle the options of dropdown
        # dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))#select must be present in the inspect{import}
        # time.sleep(5)
        # dropdown.select_by_visible_text("Female")


