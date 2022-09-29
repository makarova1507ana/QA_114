from basePage import BasePage
from selenium.webdriver.support import wait
from selenium import webdriver

class Element():
    def __init__(self,driver, locator):
        self.driver = driver
        self.locator = locator #(By.ID, "text")

    def click_element(self):
        element = self.driver.find_element(self.locator[0],self.locator[1])
        element.click()

    def send_key(self,word):
        element = self.driver.find_element(self.locator[0], self.locator[1])
        element.click()
        element.send_keys(word)