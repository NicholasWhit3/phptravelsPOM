import pyperclip
import unittest

from faker import Faker
from selenium.webdriver.support.ui import Select
from random import randrange

from Src.PageObject.Pages.HomePagePageObject import HomePage
from Src.PageObject.Pages.RegistrationPageObject import RegistrationPage
from Src.TestBase.webdriversetup import WebDriverSetup
from Src.PageObject.Locators import Locator



class Test_RegistrationPage(WebDriverSetup):

    def test_registration(self):
        driver = self.driver
        self.driver.get("https://phptravels.com/")
        self.driver.implicitly_wait(10)

        homePO = HomePage(driver)
        homePO.get_login_button().click()

        driver.switch_to.window(driver.window_handles[1])

        try:
            if driver.title == Locator.registration_page_title:
                self.assertEqual(driver.title, Locator.registration_page_title)
                print(f"\n[] Web page '{driver.current_url}' loaded successfully!")
        except Exception as error:
            print(error + "Failed to load web page")



    def test_fill_registration_page(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        self.test_registration()

        regPO = RegistrationPage(driver)
        fake = Faker()

        regPO.get_first_name().send_keys(fake.first_name())
        regPO.get_last_name().send_keys(fake.last_name())
        regPO.get_email().send_keys(fake.ascii_email())
        regPO.get_phone_number().send_keys(fake.msisdn())
        regPO.get_company_name().send_keys(fake.company())
        regPO.get_address_1().send_keys(fake.street_address())
        regPO.get_address_2().send_keys(fake.street_address())
        regPO.get_billing_city().send_keys(fake.city())
        regPO.get_state().send_keys(fake.postcode())
        regPO.get_postcode().send_keys(fake.postcode())
        regPO.get_mobile_number().send_keys(fake.phone_number())
        select = Select(regPO.get_country( ))
        select.select_by_visible_text('Ukraine')

        regPO.get_generate_password_button().click()
        regPO.get_password_length().clear()
        regPO.get_password_length().send_keys(randrange(64))
        regPO.get_generate_new_password().click()
        regPO.get_copy_button().click()
        password = str(pyperclip.paste())               #Not necessary. Just to show that the password is generated properly
        regPO.get_copy_to_clipboard_and_insert().click()

        print('[] Password: ' + password)



if __name__ == '__main__':
    unittest.main()








