

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")#link chrome




driver.get("https://opensource-demo.orangehrmlive.com/")




driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

