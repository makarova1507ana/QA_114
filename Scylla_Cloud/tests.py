import pytest
from pages.signUp import SignUp
from browser import Browser
import time



class TestSignUpPage:
    def test_signup(self):
        page = SignUp()
       # self.driver.implicitly_wait(5)
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
        time.sleep(2)
        page.agreement_check_box.click_element()
        page.signup_button.click_element()
        #assert browser.current_url == base_url + "/"