from selenium import webdriver
import logging

LOGGER = logging.getLogger(__name__)

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com"):
        LOGGER.info("Initialization browser...")
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_site(self, url):
        curl_url = self.base_url + url
        LOGGER.info(f"going to url '{curl_url}'...")
        return self.driver.get(curl_url)

    def go_to_url(self, url):
        LOGGER.info(f"going to url '{url}'...")
        return self.driver.get(url)
    # @property
    # def current_url(self):
    #     return self.driver.current_url
    def get_driver(self):
        return self.driver

    def close_browser(self):
        LOGGER.info("Browser close...")
        return self.driver.quit()

