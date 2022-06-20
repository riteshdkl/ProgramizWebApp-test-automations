import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(10)


class heading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/sql")

    def test_page_heading(self):
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
            ).text,
            "Learn SQL: SQL Tutorial for Beginners",
        )

    def test_tutorials_button(self):
        a = self.driver.title
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[1]"
        ).click()
        b = self.driver.title

        self.assertEqual(a, b)

    def test_sql_editor_button(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[2]"
        ).click()
        self.assertEqual(
            self.driver.current_url, "https://dev.programiz.com/sql/online-compiler"
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
