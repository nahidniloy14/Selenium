from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
#if it is inside a frame it can not be identified by the locator
#generaly they are named as frame,iframe,frameset
#have to pass frmae id

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("learning frame")
#will fail to print initialy the title for this we have to take our system out of the frame again
#following method would be useful to get rid
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)




