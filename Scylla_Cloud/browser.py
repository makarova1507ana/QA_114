from selenium import webdriver

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
