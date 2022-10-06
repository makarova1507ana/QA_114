import pytest
from pages.signUp import SignUp
from browser import Browser
import time
from selenium import webdriver



class User:
    def __init__(self, first_name,
        last_name, email, password,
        company, country,agreement_check_box,
        signup_button):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.company = company
        self.country = country
        self.agreement_check_box = agreement_check_box
        self.signup_button = signup_button

    # 8 characters minimum
    # One special
    # character
    # One letter
    # One number

@pytest.fixture()
def browser():
    return Browser()

class TestSignUpPage:
    def test_signup(self, browser):
        browser.go_to_site()
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.first_name.enter_text("Ivan")
        page.last_name.enter_text("Ivanov")
        page.email.enter_text("makarova1507nastya+1@gmail.com")
        page.password.enter_text("PasswordIvan1.")
        # 8 characters minimum
        # One special
        # character
        # One letter
        # One number
        page.company.enter_text("Step It")
        page.country.enter_text("Russia")

        page.agreement_check_box.click_element()
        time.sleep(2)
        page.signup_button.click_element()
        time.sleep(2)
        #assert browser.current_url == base_url + "/"