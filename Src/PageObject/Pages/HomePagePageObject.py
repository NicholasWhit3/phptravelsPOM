from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.demoButton = driver.find_element(By.XPATH, Locator.demo_button)
        self.signInButton = driver.find_element(By.XPATH, Locator.sign_up_button)


    def get_login_button(self):
        return self.signInButton

