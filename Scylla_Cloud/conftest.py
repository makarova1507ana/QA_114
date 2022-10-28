import pytest
import random
import string
import datetime
from browser import Browser
import logging
from pathlib import Path

def setup_logging(id_test):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    filenameLog = logs_dir/f'scylla-cloud_{id_test}.log'
    # logging.basicConfig(level='DEBUG', filename=filenameLog,
    #                     format="[%(asctime)s] - %(levelname)s - "
    #                            "<%(module)s>: %(message)s ")# добавили обрабочка, который закрепелен за логгеров
    root_logger = logging.getLogger()
    file_handler = logging.FileHandler(filenameLog)
    file_handler.setLevel(level='INFO')
    log_format = logging.Formatter("[%(asctime)s] - %(levelname)s - <%(module)s>: %(message)s ")
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(level='INFO')

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

@pytest.fixture(scope="session")
def id_test():
    return datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

@pytest.fixture()
def browser(id_test):
    setup_logging(id_test)
    return Browser()

@pytest.fixture()
def user_test(id_test):
    return User(first_name="Ivan",
    last_name="Ivanov",
    email=f"testeriko123+{id_test}@gmail.com",
    company="Step It",
    country="Russia",
    phone="+79331234455")