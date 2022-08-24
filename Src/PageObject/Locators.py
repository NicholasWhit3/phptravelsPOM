class Locator(object):

    #titlest
    main_page_title = "PHPTRAVELS booking script and system for hotels airline flights tours cars online application - PHPTRAVELS"
    registration_page_title = "Register - PHPTRAVELS"


    #Home page
    demo_button = '//nav[@class="clearfix"]/a[1]'
    sign_up_button = '//nav[@class="clearfix"]/a[5]'


    #Registration page
    input_first_name = 'input[id="inputFirstName"]'
    input_last_name = 'input[id="inputLastName"]'
    input_email = 'input[id="inputEmail"]'
    input_phone_number = 'input[id="inputPhone"]'
    input_company_name = 'input[id="inputCompanyName"]'
    input_address_1 = 'input[id="inputAddress1"]'
    input_address_2 = 'input[id="inputAddress2"]'
    input_city = 'input[id="inputCity"]'
    input_state = 'input[id="stateinput"]'
    input_postcode = 'input[id="inputPostcode"]'
    input_country = 'select[id="inputCountry"]'
    input_mobile_number = 'input[id="customfield2"]'
    generate_password_button = '//button[contains(text(), "Generate Password")]'
    mailing_toggl_button = '//div[@class="bootstrap-switch-container"]'
    #recaptcha_button = '//span[@id="recaptcha-anchor"]/div'
    register_button = '//input[@value="Register"]'
    select_list_countries = 'select[id="inputCountry"]'

    #Generate password popup
    input_password_length = 'input[id="inputGeneratePasswordLength"]'
    generated_password_output = 'input[id="inputGeneratePasswordOutput"]'
    copy_to_clipboard_and_insert = 'button[id="btnGeneratePasswordInsert"]'
    generate_new_password = '//*[text()[contains(.,"Generate new password")]]'
    generate_copy_button = 'img[alt="Copy to clipboard"]'


    def get_input_first_name(self):
        return self.input_first_name

    def get_input_last_name(self):
        return self.get_input_last_name

    def get_main_page_title(self):
        return self.main_page_title

    def get_registration_page_title(self):
        return self.registration_page_title

    def get_sign_up_button(self):
        return self.sign_up_button

    def get_demo_button(self):
        return self.demo_button