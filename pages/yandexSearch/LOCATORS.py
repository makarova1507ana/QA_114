from selenium.webdriver.common.by import By


class Locators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search3__button.mini-suggest__button")
    cancel_button = (By.CLASS_NAME, "search3__svg_clear")
    element_nav_bar = (By.CLASS_NAME, "service__name")