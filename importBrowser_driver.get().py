from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")#link chrome

driver.get("https://www.wikipedia.org/")#open this url in chrome
print(driver.title)#prints title of the url

