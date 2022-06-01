from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

# Implicit wait  -
#import time
#pause the test for few seconds using Time class
#driver.implicitly_wait(5)
# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
addToCart=driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for i in addToCart:
    i.click()
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button[1]").click()
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
