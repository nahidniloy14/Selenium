from selenium.webdriver.common.by import By


class page1:
    def __init__(self, driver):  # constructor
        self.driver = driver

    un = (By.ID, "user-name")
    pw = (By.ID, "password")
    loginbtn = (By.ID, "login-button")

    def username(self):
        return self.driver.find_element(*page1.un)  # * will read the particular variable as a tuple

    def password(self):
        return self.driver.find_element(*page1.pw)  # * will read the particular variable as a tuple

    def login(self):
        return self.driver.find_element(*page1.loginbtn)




