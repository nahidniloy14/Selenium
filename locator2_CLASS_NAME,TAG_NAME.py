from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.daraz.com.bd/?spm=a2a0e.login_signup.header.dhome.7aeb2829k7SHfN")
#captured from a list of catagories
#find_element will take us to the first link to execute it perfectly we have to declare it as  find_elements
sliders=driver.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
print(len(sliders))
#prints total number of links available in the webpage
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
driver.close()
