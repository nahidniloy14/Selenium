from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

action=ActionChains(driver)
menu=driver.find_element(By.ID,"mousehover")
action.move_to_element(menu).perform()
time.sleep(5)
top=driver.find_element(By.LINK_TEXT,"Top")
action.move_to_element(top).click().perform()
driver.back()
time.sleep(5)
action.context_click(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(5)
action.double_click(driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")).perform()

