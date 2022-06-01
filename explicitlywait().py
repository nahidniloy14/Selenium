from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#explicitly wait will be generated only to the targeted elements


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
#driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
addToCart=driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for i in addToCart:
    i.click()
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button[1]").click()
wait = WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located(driver.find_element(By.CSS_SELECTOR,".promoBtn")))
#wait until the locator(promocode) is present in the webpage


driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()



