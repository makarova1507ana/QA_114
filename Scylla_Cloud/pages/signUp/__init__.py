from Scylla_Cloud.pages.signUp import locators
from Scylla_Cloud.browser import Browser
from selenium import webdriver

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

    def __init__(self, base_url="https://cloud.scylladb.com/user/signup"):
       # self.path = "/user/signup"
      #  self.url = base_url + self.path
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(self.base_url)
        self.first_name = InputElement(self.driver, locators.first_name_locator)
        self.last_name = InputElement(self.driver, locators.last_name_locator)
        self.email = InputElement(self.driver, locators.email_locator)
        self.password = InputElement(self.driver, locators.password_locator)
        self.company = InputElement(self.driver, locators.company_locator)
     #   self.country = InputElement(self.driver, locators.country_locator)
        self.phone = InputElement(self.driver, locators.phone_locator)
        self.agreement_check_box = CheckBoxElement(self.driver, locators.agreement_check_box_locator)
        self.signup_button = ButtonElement(self.driver, locators.signup_button_locator)

    def signup(self):
        pass

