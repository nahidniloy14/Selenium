from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
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

    