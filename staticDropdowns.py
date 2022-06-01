from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#static options are fixed like(male,female)

driver.find_element(By.ID,"exampleFormControlSelect1").click()
#select class provides the method to handle the options of dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))#select must be present in the inspect{import}
time.sleep(5)
dropdown.select_by_visible_text("Female")
#time.sleep(5)
#dropdown.select_by_index(0)#male
