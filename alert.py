from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//fieldset[@class='pull-right']/input[1]").send_keys("Option3")
driver.find_element(By.XPATH,"//fieldset[@class='pull-right']/input[2]").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept() #ok

validateText="Option3"
driver.find_element(By.XPATH,"//fieldset[@class='pull-right']/input[1]").send_keys("Option3")
driver.find_element(By.XPATH,"//fieldset[@class='pull-right']/input[2]").click()
alert=driver.switch_to.alert
alertText=alert.text
assert validateText in alertText
alert.dismiss() #cancel