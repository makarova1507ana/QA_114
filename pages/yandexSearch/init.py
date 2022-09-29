from basePage import BasePage
from selenium.webdriver.support import wait
from pages.yandexSearch.LOCATORS import Locators
from pages.yandexSearch.element import Element

class YandexSearcher(BasePage):
    def enter_word(self, word):
        search_field = Element(self.get_driver(), Locators.search_field)
        search_field.click_element()
        search_field.send_key(word)
        return search_field

    def click_on_the_search_button(self):
        search_button = Element(self.get_driver(), Locators.search_button)
        search_button.click_element()
        return search_button

    def click_on_cancel_button(self):
        cancel_button = Element(Locators.cancel_button)
        cancel_button.click_element()
        return cancel_button

    def find_element_in_nav_bar(self):
        list_elements = self.driver.find_elements(Locators.element_nav_bar[0], Locators.element_nav_bar[1])
        return list_elements