from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

#<input class="form-control ng-touched ng-dirty ng-valid" minlength="2" name="name" required="" type="text">
#<input tag name
#class=attribute
#value of attribute=form-control ng-touched ng-dirty ng-valid

#ID-findelemnetbyID

#NAME-findelemnetbyNAME

#class-findelementbyClass

#Xpath-//tagname[@attribute='value']
#Xpath(Regular)-//*[contains(@atrribute,'value')]
#Xpath(tagname)- //tagname[text()='value']

#CSS SELECTOR
#CSS-tagname[attribute='value']
#CSS(Regular)-tagname[attribute*='value']
#tagid tagname#valueofID
#tagclass tagname.valueofclass

# link text
# EX:<a href="............."Shop more on daraz /a>
# By.linktext,"Shop more on daraz"

#tagname
#findelement(by.tagname,"h3")


#using chropath
#//div[@id="checkbox-example"]/fieldset/label[1]/input


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.NAME,"name").send_keys("Nahid Hassan Niloy")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Nahid Hassan Niloy")

driver.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys("nahidniloy894@gmail.com")
#driver.find_element(By.ID,"exampleInputPassword1").send_keys("nahidniloy1414")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("nahidniloy1414")

driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//*[contains(@name,'bday')]").send_keys("09/20/1996")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
#print(driver.find_element(By.CLASS_NAME,"alert-success").text)#use only one class name
print(driver.find_element(By.CSS_SELECTOR,".alert-success").text)#use only one class name
#*is a regular expression, it looks for a subtext which does not require 100% match
#print(driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text)
driver.find_element(By.XPATH,"//*[contains(@name,'bday')]").send_keys("09/20/1996")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Shop").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='iphone X']").click()
#driver.quit()

