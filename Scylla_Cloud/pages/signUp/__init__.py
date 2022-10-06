from Scylla_Cloud.pages.signUp import locators
from Scylla_Cloud.browser import Browser
from selenium import webdriver
from Scylla_Cloud.conftest import User
import time

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator  # (By.ID, "id")
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_element(self):
        self.element.click()

class InputElement(Element):

    def enter_text(self, text):
        self.click_element()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.get_attribute("value")

class CheckBoxElement(Element):
    pass

class ButtonElement(Element):
    pass

class SignUp():

        def __init__(self, browser):
       # self.path = "/user/signup"
      #  self.url = base_url + self.path
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
            self.first_name.enter_text(user.first_name)
            self.last_name.enter_text(user.last_name)
            self.email.enter_text(user.email)
            self.password.enter_text(user.password())
            self.company.enter_text(user.company)
            self.country.enter_text(user.country)
            # time.sleep(2)
            # self.phone.enter_text(user.phone)

