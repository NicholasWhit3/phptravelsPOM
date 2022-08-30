from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class RegistrationPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.firstName = driver.find_element(By.CSS_SELECTOR, Locator.input_first_name)
        self.lastName = driver.find_element(By.CSS_SELECTOR, Locator.input_last_name)
        self.email = driver.find_element(By.CSS_SELECTOR, Locator.input_email)
        self.phoneNumber = driver.find_element(By.CSS_SELECTOR, Locator.input_phone_number)
        self.companyName = driver.find_element(By.CSS_SELECTOR, Locator.input_company_name)
        self.address1 = driver.find_element(By.CSS_SELECTOR, Locator.input_address_1)
        self.address2 = driver.find_element(By.CSS_SELECTOR, Locator.input_address_2)
        self.city = driver.find_element(By.CSS_SELECTOR, Locator.input_city)
        self.state = driver.find_element(By.CSS_SELECTOR ,Locator.input_state)
        self.postcode = driver.find_element(By.CSS_SELECTOR ,Locator.input_postcode)
        self.country = driver.find_element(By.CSS_SELECTOR ,Locator.input_country) #dropdown menu
        self.mobileNumber = driver.find_element(By.CSS_SELECTOR ,Locator.input_mobile_number)
        self.generatePasswordButton = driver.find_element(By.XPATH ,Locator.generate_password_button)
        self.mailingToggl = driver.find_element(By.XPATH ,Locator.mailing_toggl_button)
        '''
         self.recaptcha = WebDriverWait(driver, 50).until(
                        EC.presence_of_element_located((By.XPATH ,Locator.recaptcha_button)))
                            
        def get_recaptcha(self):
            return self.recaptcha
        '''
        self.password_length = driver.find_element(By.CSS_SELECTOR, Locator.input_password_length)
        self.generated_password_output = driver.find_element(By.CSS_SELECTOR, Locator.generated_password_output)
        self.copy_to_clipboard_and_insert = driver.find_element(By.CSS_SELECTOR, Locator.copy_to_clipboard_and_insert)
        self.registerButton = driver.find_element(By.XPATH ,Locator.register_button)
        self.generateNewPassword = driver.find_element(By.XPATH, Locator.generate_new_password)
        self.copyButton = driver.find_element(By.CSS_SELECTOR, Locator.generate_copy_button)
        self.closeGenerateButton = driver.find_element(By.CSS_SELECTOR, Locator.close_generate_password_button)

    def get_close_generate_password_button(self):
        return self.closeGenerateButton

    def get_copy_button(self):
        return self.copyButton

    def get_generate_new_password(self):
        return self.generateNewPassword

    def get_copy_to_clipboard_and_insert(self):
        return self.copy_to_clipboard_and_insert

    def get_generated_password_output(self):
        return self.generated_password_output

    def get_password_length(self):
        return self.password_length

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phoneNumber

    def get_company_name(self):
        return self.companyName

    def get_address_1(self):
        return self.address1

    def get_address_2(self):
        return self.address2

    def get_billing_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postcode(self):
        return self.postcode

    def get_country(self):
        return self.country

    def get_mobile_number(self):
        return self.mobileNumber

    def get_generate_password_button(self):
        return self.generatePasswordButton

    def get_mailing_toggl(self):
        return self.mailingToggl

    def get_registration_button(self):
        return self.registerButton