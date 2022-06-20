import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(10)


class Pagelinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/sql")

    def test_online_sql_compiler_link(self):
        a = self.driver.current_url
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ol[2]/li[2]/a",
        ).click()
        b = self.driver.current_url

        self.assertNotEqual(a, b)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
