import time
import unittest
from turtle import title
from xml.dom.minidom import Element

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class heading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com")

    # @unittest.skip("test skipped")
    def test_learn_to_code_for_free_heading(self):

        expectedheading = "Learn to Code\nfor Free"
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[1]/div/h1'
        )

        self.assertEqual(expectedheading, heading.text)

    # @unittest.skip("test skipped")
    def test_learn_to_code_for_free_paragraph(self):

        expectedparagraph = "Learn to code with our beginner-friendly tutorials and examples. Read tutorials and examples, write programs, run code and learn to code."
        paragraph = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[1]/div/p'
        )

        self.assertEqual(expectedparagraph, paragraph.text)

    # @unittest.skip("test skipped")
    def test_homepage_image(self):

        img = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[2]/img'
        )
        self.assertTrue(img.is_displayed())

    # @unittest.skip("test skipped")
    def test_latest_updates(self):

        self.driver.find_element(
            By.XPATH,
            '//*[@id="mauticform_input_generalsubscribersformhomepage_email1"]',
        ).send_keys("abc@gmail.com")

        self.driver.find_element(
            By.XPATH,
            '//*[@id="mauticform_input_generalsubscribersformhomepage_subscribe"]',
        ).click()

        message = self.driver.find_element(
            By.XPATH, '//*[@id="mauticform_generalsubscribersformhomepage_message"]'
        )
        self.assertTrue(message)

    # @unittest.skip("test skipped")
    def test_choose_what_to_learn_heading(self):
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[1]/div/h2'
        ).is_displayed()
        self.assertTrue(heading)

    # @unittest.skip("test skipped")
    def test_choose_what_to_learn_python(self):
        current_url = self.driver.current_url
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]'
        ).click()
        time.sleep(2)

        expected_title = self.driver.title
        actual_title = self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
        )
        time.sleep(2)
        after_url = self.driver.current_url

        self.assertEqual(expected_title, actual_title.text)
        self.assertNotEqual(current_url, after_url)

    # @unittest.skip("test skipped")
    def test_choose_what_to_learn_java(self):
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[3]/div'
        ).click()
        time.sleep(2)
        java_url = self.driver.current_url
        java_title = self.driver.title
        title = self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
        )
        time.sleep(2)
        expected_java_url = "https://dev.programiz.com/java-programming"

        self.assertEqual(java_title, title.text)
        self.assertEqual(java_url, expected_java_url)

    # @unittest.skip("test skipped")
    def test_view_all_tutorials(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/div/div[1]/a/span',
        ).click()
        a = self.driver.find_element(
            By.PARTIAL_LINK_TEXT, "View fewer tutorials"
        ).is_displayed()
        self.assertTrue(a)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
