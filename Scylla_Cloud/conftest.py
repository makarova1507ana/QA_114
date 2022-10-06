import pytest
import random
import string
from Scylla_Cloud.browser import Browser

class User:
    def __init__(self, first_name, last_name, email, company, country, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self._password = ""
        self.company = company
        self.country = country

    @staticmethod
    def generate_password(count_special_chars, count_letters, count_numbers):
        special_chars = random.sample(string.punctuation, count_special_chars)
        letters = random.sample(string.ascii_letters, count_letters)
        numbers = random.sample(string.digits, count_numbers)
        password = special_chars + letters + numbers
        return password

    def password(self):
        """ 8 characters minimum
            One special character
            One letter
            One number
        """
        self._password = self.generate_password(count_special_chars=1, count_letters=5, count_numbers=2)
        return self._password

@pytest.fixture()
def browser():
    return Browser()

@pytest.fixture()
def test_user():
    return User(first_name="Ivan",
    last_name="Ivanov",
    email="makarova1507nastya+1@gmail.com",#надо подумать над уникальностью
    company="Step It",
    country="Russia",
    phone="+79331234455")