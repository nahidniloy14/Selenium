from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#CSS selector
#tagid tagname#valueofID
#tagname is optional
#driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
driver.find_element(By.CSS_SELECTOR,"#Email").clear()
driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("niloy123@yourstore.com")
#tagclass tagname.valueofclass
driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.CSS_SELECTOR,".password").send_keys("1414")
#driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


#tag attribute
#tagname[attribute=value]
#any attribute will work fine
driver.find_element(By.CSS_SELECTOR,"[button type=submit]").click()

driver.quit()