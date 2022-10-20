import logging
import time
from selenium import webdriver
from Scylla_Cloud.pages.signUp import locators
from Scylla_Cloud.browser import Browser
from Scylla_Cloud.conftest import User
from Scylla_Cloud.pages.signUp.element import Element, InputElement, CheckBoxElement, ButtonElement

LOGGER = logging.getLogger(__name__)

class SignUp():
        path = "/user/signup"
        def __init__(self, browser):
            self.first_name = InputElement(driver=browser.get_driver(), locator=locators.first_name_locator)
            self.last_name = InputElement(driver=browser.get_driver(), locator=locators.last_name_locator)
            self.email = InputElement(driver=browser.get_driver(), locator=locators.email_locator)
            self.password = InputElement(driver=browser.get_driver(), locator=locators.password_locator)
            self.company = InputElement(driver=browser.get_driver(), locator=locators.company_locator)
            self.country = InputElement(driver=browser.driver, locator=locators.country_locator)
            self.phone = InputElement(driver=browser.get_driver(), locator=locators.phone_locator)
            self.agreement_check_box = CheckBoxElement(driver=browser.get_driver(), locator=locators.agreement_check_box_locator)
            self.signup_button = ButtonElement(driver=browser.get_driver(), locator=locators.signup_button_locator)

        def signup(self, user: User):
            LOGGER.info("Signing up ...")
            self.first_name.enter_text(user.first_name)
            self.last_name.enter_text(user.last_name)
            self.email.enter_text(user.email)
            self.password.enter_text(user.password())
            self.company.enter_text(user.company)
            self.country.enter_text(user.country)
            self.country.key_code()
            # time.sleep(2)
            self.phone.enter_text(user.phone)
            self.agreement_check_box.click_element()
            print("\n", self.agreement_check_box.state())
            if self.agreement_check_box.state() == False:
                LOGGER.warning("Check box is False ...")
            LOGGER.info("Signup complete ...")
           # time.sleep(2)
           # self.signup_button.click_element()
