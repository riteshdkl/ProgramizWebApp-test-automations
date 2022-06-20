import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

# from multiprocessing.connection import wait


def wait():
    time.sleep(5)


class allExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_convert_km(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/hello-world"
        )
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[1]/div/div[1]/div[1]/div/div/div/ul/li[8]/div/span/a",
        ).click()
        wait()

        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/examples/km-mile/bgg",
        )

    def test_logo(self):
        self.driver.get("https://dev.programiz.com")
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div'
        ).click()
        time.sleep(10)
        self.assertTrue(
            self.driver.find_element(
                By.XPATH, "/html/body/main/header/nav/div/div/div[3]"
            ).is_displayed()
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports"
        )
    )
