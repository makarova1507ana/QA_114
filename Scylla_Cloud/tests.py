import re
import string
import conftest
import pytest
from pages.signUp import SignUp
from browser import Browser
import time
from selenium import webdriver
import logging
from gmail_client import GmailClient
LOGGER = logging.getLogger(__name__)

class TestSignUpPage:

    def test_signup(self, browser, user_test):
        LOGGER.info("start test : test_signup")
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=user_test)
        LOGGER.info("end test : test_signup")
        time.sleep(2)
        #assert browser.current_url == base_url + "/"

    def test_verification(self, browser, user_test):
        gmail_client = GmailClient(email_addr="testeriko123@gmail.com", password="usgnqbvjpewlqfwz")
        messages = gmail_client.get_messages(to_email="testeriko123@gmail.com", find_before=40)  # работает
        assert len(messages) == 1, f"More than one message for {user_test.email} in  the Inbox"
        LOGGER.info(messages[0])
        match_obj = re.search('\/\/cloud.scylladb.com.\/me\/verify/+"', str(messages[0]))
        assert match_obj is not None, f"Link not found in {messages[0]}"
        verification_link = "https:"+match_obj.group()#просто 1 убрать
        browser.go_to_url(verification_link)
        time.sleep(5)
        LOGGER.info(verification_link)


