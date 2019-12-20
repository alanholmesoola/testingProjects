from selenium import webdriver
from config import Config

class Browser(object):

    configuration = Config('config.json')
    base_url = 'https://alantest.wpengine.com/wp-admin/'
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(configuration.driver_path, chrome_options=opts)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def quit(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)