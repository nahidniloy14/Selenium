from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")#link chrome
#forward navigation
driver.get("https://www.wikipedia.org/")#open this url in chrome
print(driver.title)#prints title of the url


#backward navigation
driver.get("https://www.quora.com/")#open this url in chrome
print(driver.title)#prints title of the url

driver.back()
print(driver.title)#prints title of the url
time.sleep(3) #sets timer{import}

driver.forward()
print(driver.title)#prints title of the url
time.sleep(5)

