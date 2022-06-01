from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#status = driver.find_element(By.XPATH,"//input[@id='RESULT_RadioButton-7_1']").is_selected()  # male
#print(status)
#driver.find_element(By.XPATH,"//input[@id='RESULT_RadioButton-7_1']").click()
#print(status)
#status=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/input"))).click()
#status=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "RESULT_RadioButton-7_0"))).click()
status = driver.find_element(By.XPATH,"//label[contains(text(),'Male')]").is_selected()  # male
print(status)

driver.find_element(By.XPATH,"//label[contains(text(),'Male')]").click() # male
status = driver.find_element(By.XPATH,"//label[contains(text(),'Male')]").is_enabled()
print(status)
# status = driver.find_element(By.ID, "RESULT_RadioButton-7_1").is_selected()  # female
# print(status)


