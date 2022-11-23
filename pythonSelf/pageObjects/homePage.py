
#self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Nahid Hassan Niloy")
# driver.find_element(By.ID,"exampleFormControlSelect1").click()
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):  # constructor
        self.driver = driver

    name = (By.CSS_SELECTOR,"input[name='name']")
    gender=(By.ID,"exampleFormControlSelect1")

    # pw = (By.ID, "password")
    # loginbtn = (By.ID, "login-button")

    # def username(self):
    #     return self.driver.find_element(*page1.un)  # * will read the particular variable as a tuple
    #
    # def password(self):
    #     return self.driver.find_element(*page1.pw)  # * will read the particular variable as a tuple
    #
    # def login(self):
    #     return self.driver.find_element(*page1.loginbtn)

    def getname(self):
        return self.driver.find_element(*HomePage.name)
    def getgender(self):
        return self.driver.find_element(*HomePage.gender)




