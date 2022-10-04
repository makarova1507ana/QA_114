from selenium import webdriver

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com/user/signup"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

        #self.driver.implicitly_wait(5)
    def go_to_site(self):
        return self.driver.get(self.base_url)
    # @property
    # def current_url(self):
    #     return self.driver.current_url
    def get_driver(self):
        return self.driver

    def close_browser(self):
        return self.driver.quit()

