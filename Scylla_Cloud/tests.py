import string
from Scylla_Cloud import conftest
import pytest
from pages.signUp import SignUp
from browser import Browser
import time
from selenium import webdriver



class TestSignUpPage:

    def test_signup(self, browser, user_test):
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=user_test)
        print(page.email.get_text())
        time.sleep(2)
        #assert browser.current_url == base_url + "/"
