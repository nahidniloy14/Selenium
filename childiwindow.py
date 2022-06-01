from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()

#initialy it will print the text of parent window
print(driver.find_element(By.TAG_NAME,"h3").text) #use it only if it is unique

childwindow=driver.window_handles[1] #lsit of windows openened by the selenium # [0] parent id [1] child id
driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME,"h3").text)

#if we want to go back to parent window
#parentwindow=driver._switch_to.window(driver.window_handles[0])
#driver.switch_to.window(parentwindow)
#print(driver.find_element(By.TAG_NAME,"h3").text)
