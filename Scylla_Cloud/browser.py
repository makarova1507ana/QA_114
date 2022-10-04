from selenium import webdriver

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com/user/signup"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(self.base_url)
        #self.driver.implicitly_wait(5)
    # @property
    # def current_url(self):
    #     return self.driver.current_url

    def close_browser(self):
        self.driver.quit()

