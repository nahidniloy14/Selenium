from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#displayed or enabled
status=driver.find_element(By.NAME,"RESULT_TextField-1").is_displayed()
print(status)
status=driver.find_element(By.NAME,"RESULT_TextField-1").is_enabled()
print(status)
#how many input boxes are present
noe=driver.find_elements(By.CLASS_NAME,"text_field")#careful about find elements
print(len(noe))
#how to provide values into text box
driver.find_element(By.NAME,"RESULT_TextField-5").send_keys("Dhaka")
