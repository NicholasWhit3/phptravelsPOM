import pyperclip
import unittest
import os
import sys
import re
import time
import urllib
import speech_recognition as sr
import pydub

from faker import Faker
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys , ActionChains
from selenium.webdriver.support.ui import Select
from random import randrange

from Src.PageObject.Pages.HomePagePageObject import HomePage
from Src.PageObject.Pages.RegistrationPageObject import RegistrationPage
from Src.TestBase.webdriversetup import WebDriverSetup
from Src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By



class Test_RegistrationPage(WebDriverSetup):

    def reCaptchaV2(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)

        frames = driver.find_elements(By.TAG_NAME,"iframe")
        recaptcha_control_frame = None
        recaptcha_challenge_frame = None
        for index , frame in enumerate(frames):
            if re.search('reCAPTCHA' , frame.get_attribute("title")):
                recaptcha_control_frame = frame

            if re.search('recaptcha challenge' , frame.get_attribute("title")):
                recaptcha_challenge_frame = frame
        if not (recaptcha_control_frame and recaptcha_challenge_frame):
            print("[ERROR] Unable to find recaptcha. Abort solver.")
            sys.exit()
        # switch to recaptcha frame
        driver.implicitly_wait(5)
        frames = driver.find_elements(By.TAG_NAME,"iframe")
        driver.switch_to.frame(recaptcha_control_frame)
        # click on checkbox to activate recaptcha
        time.sleep(3)
        recaptcha_chexbox = driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]')
        action.move_to_element(recaptcha_chexbox)
        recaptcha_chexbox.click()

        body = driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(Keys.PAGE_DOWN)

        # switch to recaptcha audio control frame
        time.sleep(3)
        driver.switch_to.default_content()
        frames = driver.find_elements(By.TAG_NAME,"iframe")
        driver.switch_to.frame(recaptcha_challenge_frame)

        captchaFrame = driver.find_elements(By.CSS_SELECTOR, 'div[id="rc-imageselect"]')
        time.sleep(3)

        if len(captchaFrame) <= 0:
                registration_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Register"]')
                action.move_to_element(registration_button)
                registration_button.click()
        else:
            # click on audio challenge
            driver.implicitly_wait(10)
            time.sleep(3)
            recaptcha_audio_button =  driver.find_element(By.CSS_SELECTOR,'#recaptcha-audio-button')
            action.move_to_element(recaptcha_audio_button)
            recaptcha_audio_button.click()
            # switch to recaptcha audio challenge frame
            driver.switch_to.default_content()

            frames = driver.find_elements(By.TAG_NAME , "iframe")
            driver.switch_to.frame(recaptcha_challenge_frame)

            # get the mp3 audio file
            driver.implicitly_wait(5)
            src = driver.find_element(By.CSS_SELECTOR, '#audio-source').get_attribute("src")
            print(f"[INFO] Audio src: {src}")

            path_to_mp3 = os.path.normpath(os.path.join(os.getcwd() , "sample.mp3"))
            path_to_wav = os.path.normpath(os.path.join(os.getcwd() , "sample.wav"))

            # download the mp3 audio file from the source
            urllib.request.urlretrieve(src , path_to_mp3)

            # load downloaded mp3 audio file as .wav
            try:
                sound = pydub.AudioSegment.from_mp3(path_to_mp3)
                sound.export(path_to_wav , format = "wav")
                sample_audio = sr.AudioFile(path_to_wav)
            except Exception:
                sys.exit(
                    "[ERROR] Please run program as administrator or download ffmpeg manually, "
                    "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
                )

                # translate audio to text with google voice recognition
            driver.implicitly_wait(5)
            r = sr.Recognizer( )
            with sample_audio as source:
                audio = r.record(source)
            key = r.recognize_google(audio)
            print(f"[INFO] Recaptcha Passcode: {key}")

            # key in results and submit
            driver.implicitly_wait(5)
            driver.find_element_by_id("audio-response").send_keys(key.lower( ))
            driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
            time.sleep(5)
            driver.switch_to.default_content( )
            time.sleep(5)
            driver.find_element(By.ID , "recaptcha-demo-submit").click( )




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
        # Not necessary. Just to show that the password is generated properly
        password = str(pyperclip.paste())
        regPO.get_copy_to_clipboard_and_insert().click()
        regPO.get_close_generate_password_button().click()
        regPO.get_mailing_toggl().click()
        self.reCaptchaV2()


        print('[] Password: ' + password)



if __name__ == '__main__':
    unittest.main()








