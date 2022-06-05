#
# # chrome browser --- inspect -- console
# # document.getElementsByClassName("ajax_cart_no_product unvisible")[0]
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
#
# import time
# driver = webdriver.Chrome()
# driver.get("http://automationpractice.com/index.php")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//a[@data-id-product='6']/span").click()
# driver.find_element(By.XPATH,"//span[@class='continue btn btn-default button exclusive-medium']").click()
# driver.find_element(By.XPATH,"//a[@data-id-product='4']/span").click()
# driver.find_element(By.XPATH,"//a[@title='Proceed to checkout']").click()
# action=ActionChains(driver)
# hover=driver.find_element(By.XPATH,"//a[@title='View my shopping cart']")
# action.move_to_element(hover).perform()
# time.sleep(3)
# # to perform click opertaion by jsDOM
# checkout= driver.find_element(By.XPATH,"//div[@class='shopping_cart']/a/span[5]")
# driver.execute_script("arguments[0].click();",checkout

