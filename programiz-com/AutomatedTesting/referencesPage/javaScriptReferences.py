import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(5)


class javaScriptReferences(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_js_math_sin(self):
        self.driver.get("https://dev.programiz.com/javascript/library")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/h3/a",
        ).click()
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/h1"
            ).text,
            "JavaScript Math sin()",
        )

    def test_related_topics(self):
        self.driver.get("https://dev.programiz.com/javascript/library/math/sin")

        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[1]/div/div[1]/div[5]/div/div/div/ul/li[5]/div/span/a",
        ).click()
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/h1"
            ).text,
            "JavaScript Math atan()",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
