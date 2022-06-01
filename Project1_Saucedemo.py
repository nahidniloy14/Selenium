from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#explicitly wait will be generated only to the targeted elements
# Web Test Case Scenario:
# - Go to https://www.saucedemo.com/
# - Save into a variable username(standard_user) & password from bottom & use it for login
# - Add Two Product into Cart
# - Click Cart Icon & Click Checkout
# - Fill-up First Name, Last Name, ZIP
# - Assert Item total amount & Click Finish
# - Assert Order Complete
# NB:
# 1. Don't use copy Paste xpath
# 2. Use different types of locator for different elements (example: for login field use xpath, for password use CSS, try parent,child & among other's)
# 3. Organized & write your code properly (write clean code)

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.XPATH,"//div[@class='shopping_cart_container']").click()
driver.find_element(By.CSS_SELECTOR,"#checkout").click()
driver.find_element(By.NAME,"firstName").send_keys("Nahid Hassan")
driver.find_element(By.NAME,"lastName").send_keys("Niloy")
driver.find_element(By.NAME,"postalCode").send_keys("1414")
driver.find_element(By.ID,"continue").click()
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(5)
# assert driver.find_element(By.CSS_SELECTOR,".summary_total_label").get_attribute("value") == "Total: $43.18"
# print(driver.find_element(By.CSS_SELECTOR,".summary_total_label").get_attribute("class"))
message=driver.find_element(By.CSS_SELECTOR,".summary_total_label").text
assert "$43.18" in message

print("test case 1 passed")
driver.find_element(By.NAME,"finish").click()

message=driver.find_element(By.TAG_NAME,"h2").text
assert "THANK YOU" in message
print("test case 2 passed")

driver.quit()