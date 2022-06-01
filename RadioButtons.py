from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

rb=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
rb=driver.find_elements(By.NAME,"radioButton")
rb[2].click()
#print (len(checkboxes))
#for checkbox in checkboxes:
        #print(checkbox.get_attribute("name"))
        #break


