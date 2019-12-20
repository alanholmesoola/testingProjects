import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"../drivers/geckodriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        elem2 = driver.find_elements(By.CSS_SELECTOR,"#content a")
        resultFound = self.look_for_text_in_search_results(elem2, "docs.python.org")
        self.assertEqual(resultFound, True)

    def look_for_text_in_search_results(self, result, searchCriteria):
        for item in result:
            # print(item.text)
            if item.text == searchCriteria:
                return True
        return False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
