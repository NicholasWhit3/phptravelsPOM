import unittest

from Src.PageObject.Locators import Locator
from Src.PageObject.Pages.HomePagePageObject import HomePage
from Src.TestBase.webdriversetup import WebDriverSetup


class Test_HomePage(WebDriverSetup):

    def test_home_page(self):
        driver = self.driver
        self.driver.get("https://phptravels.com/")
        self.driver.implicitly_wait(10)

        try:
            if driver.title == Locator.main_page_title:
                self.assertEqual(driver.title, Locator.main_page_title)
                print(f"\n[] Web page '{driver.current_url}' loaded successfully!")
        except Exception as error:
            print(error + "Failed to load web page")



    def test_open_registration_page(self):
        driver = self.driver
        self.test_home_page()
        self.driver.implicitly_wait(10)

        homePage = HomePage(driver)


        logButton = homePage.get_login_button()
        logButton.click()

        driver.switch_to.window(driver.window_handles[1])

        try:
            if driver.title == Locator.registration_page_title:
                self.assertEqual(driver.title, Locator.registration_page_title)
                print(f"\n[] Web page '{driver.current_url}' loaded successfully!")
        except Exception as error:
            print(error + "Failed to load web page")




if __name__ == '__main__':
    unittest.main()