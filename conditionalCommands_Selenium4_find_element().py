from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
destination=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=destination)#link chrome

#everything inside in a webpage are known as a web element
#<input name="txtUsername" id="txtUsername" type="text">
#input is tag name
#name and id is attribute
#sendkeys will pass the value

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
web_title=driver.title
exp_title="OrangeHRM"
if web_title==exp_title:
    print("matched")
else:
    print("did not matched")
