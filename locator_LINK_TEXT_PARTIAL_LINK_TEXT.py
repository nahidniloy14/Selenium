from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(
    "https://member.daraz.com.bd/user/login?spm=a2o2r5.tm800082663.header.d5.46ab6487yKu6BD&redirect=https%3A%2F%2Fpages.daraz.com.bd%2Fwow%2Fgcp%2Fdaraz%2Fchannel%2Fbd%2Fnew-help-pages%2Ffree-pickup%3Fspm%3Da2a0e.home.top.dbr1.735212f7HEThdw%26scm%3D1003.4.icms-zebra-100031732-2885620.OTHER_6053521296_7612189")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys(
    "nahidniloy894@gmail.com")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/input")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/input").send_keys(
    "Nahidniloy14@124634")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/button").click()
# link text <a href="............."Shop more on daraz /a>
driver.maximize_window()  # maximizes the window
driver.find_element(By.LINK_TEXT, "SAVE MORE ON APP").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "SAVE MOR").click()
#driver.quit()  # closes all the tab after execution
print("test passed")
