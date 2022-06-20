import time
import unittest
from lib2to3.pgen2 import driver

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class whyProgramiz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com")

    # @unittest.skip("test skipped")
    def test_whyProgramizHeading(self):
        expectedHeading = "Why Programiz?"
        actualHeading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[4]/div/div[1]/h2'
        )

        self.assertEqual(expectedHeading, actualHeading.text)

    def test_whyProgramizContents(self):
        icon = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[4]/div/div[2]/div[1]/div/div[1]'
        ).is_displayed()
        time.sleep(2)
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[4]/div/div[2]/div[1]/div/div[2]/h3'
        ).is_displayed()
        time.sleep(2)
        paragraph = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[4]/div/div[2]/div[1]/div/div[2]/p'
        ).is_displayed()
        time.sleep(2)

        self.assertTrue(icon)
        self.assertTrue(heading)
        self.assertTrue(paragraph)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
