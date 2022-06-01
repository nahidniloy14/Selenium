from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#can specify only once in a web page and will be applicable for all the elements of this particular page
#Implicit Wait time is applied to all the elements in the script,

driver.implicitly_wait(10)#will wait for maximum 10s


driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("niloy123@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("1414")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

