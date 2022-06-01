from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a ")
print(len(countries))
time.sleep(2)
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID,"autosuggest").text)
assert driver.find_element(By.ID,"autosuggest") .get_attribute('value') == "India"
#get_attribute('value') will go the location and print the vlaue typed in the place
#assert driver.find_element(By.ID,"autosuggest") .get_attribute('value') #actualvalue
#== "India" #expected value
