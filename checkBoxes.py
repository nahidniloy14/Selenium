from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print (len(checkboxes))
for checkbox in checkboxes:
        checkbox.click()

time.sleep(5)
for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2" :
                checkbox.click()
                assert checkbox.is_selected()#expecting false

#print(driver.find_element(By.ID,"autosuggest").text)
#assert driver.find_element(By.ID,"autosuggest") .get_attribute('value') == "India"
#get_attribute('value') will go the location and print the vlaue typed in the place
#assert driver.find_element(By.ID,"autosuggest") .get_attribute('value') #actualvalue
#== "India" #expected value
#driver.quit()