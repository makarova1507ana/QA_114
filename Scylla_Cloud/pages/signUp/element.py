from selenium import webdriver
from selenium.webdriver import Keys
from Scylla_Cloud.pages.signUp.locators import is_checked_locator

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

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)

class CheckBoxElement(Element):
    is_checked = False

    def checked(self):
        self.element.click_element()
        self.is_checked = True
        return self.is_checked

    def unchecked(self):
        self.element.click_element()
        self.is_checked = False
        return self.is_checked

    def state(self):
        """return when checkBox is checked or not"""
        if self.is_checked and self.driver.find_element(is_checked_locator[0],is_checked_locator[1]):
            return True
        else:
            return False

class ButtonElement(Element):

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)