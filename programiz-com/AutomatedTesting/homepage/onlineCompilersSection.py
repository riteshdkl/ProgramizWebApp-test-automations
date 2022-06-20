import time
import unittest
from lib2to3.pgen2 import driver
from turtle import title

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class onlineCompilers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://programiz.com")
        self.driver.execute_script("window.scrollTo(0, 1800)")

    # @unittest.skip("test skipped")
    def test_sectionHeading(self):
        expectedHeading = "Practice with our Online Compilers"
        actualHeading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[3]/div/div/div[2]/h2'
        )
        time.sleep(2)

        self.assertEqual(expectedHeading, actualHeading.text)

        # def test_pythonCompiler(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[3]/div/div/div[2]/div/a[1]/h5'
        ).click()
        time.sleep(2)
        get_url = self.driver.current_url
        actual_url = "https://www.programiz.com/python-programming/online-compiler/"

        self.assertEqual(get_url, actual_url)

    # @unittest.skip("test skipped")
    def test_javaCompiler(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[3]/div/div/div[2]/div/a[5]/h5'
        ).click()
        time.sleep(2)
        get_url = self.driver.current_url
        print(get_url)
        actual_url = "https://www.programiz.com/java-programming/online-compiler/"

        self.assertEqual(get_url, actual_url)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
