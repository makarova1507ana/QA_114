import string
import conftest
import pytest
from pages.signUp import SignUp
from browser import Browser
import time
from selenium import webdriver
import logging

LOGGER = logging.getLogger(__name__)

class TestSignUpPage:

    def test_signup(self, browser, user_test):
        LOGGER.info("start test : test_signup")
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=user_test)
        print(page.email.get_text())
        time.sleep(2)
        LOGGER.info("end test : test_signup")
        #assert browser.current_url == base_url + "/"

    def test_s(self):
        print("test")