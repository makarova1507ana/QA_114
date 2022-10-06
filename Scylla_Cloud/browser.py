from selenium import webdriver

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_site(self, url):
        curl_url = self.base_url + url
        return self.driver.get(curl_url)
    # @property
    # def current_url(self):
    #     return self.driver.current_url
    def get_driver(self):
        return self.driver

    def close_browser(self):
        return self.driver.quit()

