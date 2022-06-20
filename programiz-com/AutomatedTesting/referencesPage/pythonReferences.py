import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(5)


class pythonReferences(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_search_bar(self):
        self.driver.get("https://dev.programiz.com/python-programming/methods")
        self.driver.find_element(By.XPATH, '//*[@id="edit-title"]').send_keys("int")
        wait()
        self.driver.find_element(
            By.XPATH, '//*[@id="edit-submit-python-methods-reference"]'
        ).click()
        wait()
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.view.view-python-methods-reference.view-id-python_methods_reference.view-display-id-page.attachment-page-views.view-dom-id-05bbf508d0db84019883b2e623bd506e.jquery-once-1-processed > div.contents.contents--reference > div > div",
            ).is_displayed()
        )

    def test_python_any_method(self):
        self.driver.get("https://dev.programiz.com/python-programming/methods")
        wait()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.view.view-python-methods-reference.view-id-python_methods_reference.view-display-id-page.attachment-page-views.view-dom-id-05bbf508d0db84019883b2e623bd506e.jquery-once-1-processed > div.contents.contents--reference > div > div > div > div.view.view-python-methods-reference.view-id-python_methods_reference.view-display-id-attachment_1.attachment-views-individual > div > div:nth-child(3)",
        ).click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
