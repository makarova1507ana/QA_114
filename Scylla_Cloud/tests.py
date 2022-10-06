import string
from Scylla_Cloud import conftest
import pytest
from pages.signUp import SignUp
from browser import Browser
import time
from selenium import webdriver



class TestSignUpPage:

    def test_signup(self, browser, test_user):
        browser.go_to_site()
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=test_user)
        page.agreement_check_box.click_element()
        time.sleep(2)
        page.signup_button.click_element()
        time.sleep(2)
        #assert browser.current_url == base_url + "/"
