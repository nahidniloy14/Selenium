from selenium.webdriver.common.by import By


class page2:
    def __init__(self, driver):  # constructor
        self.driver = driver
        # self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        # self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
        # self.driver.find_element(By.XPATH, "//div[@class='shopping_cart_container']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    atc1 = (By.NAME, "add-to-cart-sauce-labs-backpack")
    atc2 = (By.NAME, "add-to-cart-sauce-labs-bike-light")
    con = (By.XPATH, "//div[@class='shopping_cart_container']")
    co = (By.XPATH, "//div[@class='shopping_cart_container']")

    def backpack(self):
        return self.driver.find_element(*page2.atc1)

    def bikelight(self):
        return self.driver.find_element(*page2.atc2)

    def container(self):
        return self.driver.find_element(*page2.con)

    # def checkout(self):
    #     self.driver.find_element(*page2.co).click()
    #     page3 = page2(self.driver)
    #
    #     return page3

