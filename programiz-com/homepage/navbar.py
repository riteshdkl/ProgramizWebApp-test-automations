import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class navbar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_homepage_logo(self):
        self.driver.get("https://programiz.com")
        title = self.driver.title
        self.driver.refresh()
        title2 = self.driver.title
        self.assertEqual(title, title2)

    @unittest.skip("test skipped")
    def test_search(self):
        self.driver.get("https://programiz.com")
        self.driver.find_element(By.XPATH, '//*[@id="edit-keys-2"]').send_keys(
            "python", Keys.ENTER
        )
        count_element = self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div/p"
        ).text
        data = count_element
        data = data.replace("results found", "")
        data = int(data)

        self.assertGreater(data, 1)

    # @unittest.skip("test skipped")
    def test_tutorials(self):
        self.driver.get("https://programiz.com")
        self.driver.find_element(
            By.XPATH, "/html/body/main/header/nav/div/div/div[2]/a[2]/span"
        ).click()
        list_new = self.driver.find_elements_by_class_name(
            (By.CLASS_NAME, "tabbed-link")
        )
        self.assertEqual(10, len(list_new))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
