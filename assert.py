from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#assert always tends to return true
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Nahid Hassan Niloy")

driver.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys("nahidniloy894@gmail.com")
#driver.find_element(By.ID,"exampleInputPassword1").send_keys("nahidniloy1414")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("nahidniloy1414")

driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//*[contains(@name,'bday')]").send_keys("09/20/1996")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
#print(driver.find_element(By.CLASS_NAME,"alert-success").text)#use only one class name
message=driver.find_element(By.CSS_SELECTOR,".alert-success").text #use only one class name
#assert "success" in message #is the word present in the sentence
