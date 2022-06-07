import time
import unittest
from xml.dom.minidom import Element

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class heading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://programiz.com")

    # @unittest.skip("test skipped")
    def test_learn_to_code_for_free_heading(self):

        expectedheading = "Learn to Code \nfor Free"
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[1]/div/h1'
        )

        self.assertEqual(expectedheading, heading.text)

    def test_learn_to_code_for_free_paragraph(self):

        expectedparagraph = "Learn to code with our beginner-friendly tutorials and examples. Read tutorials and examples, write programs, run code and learn to code."
        paragraph = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[1]/div/p'
        )

        self.assertEqual(expectedparagraph, paragraph.text)

    @unittest.skip("test skipped")
    def test_homepage_image(self):

        img = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[1]/div[2]/img'
        )
        self.assertTrue(img.is_displayed())

    @unittest.skip("test skipped")
    def test_latest_updates(self):

        self.driver.find_element(
            By.XPATH,
            '//*[@id="mauticform_input_generalsubscribersformhomepage_email1"]',
        ).send_keys("abc@gmail.com")
        time.sleep(5)
        self.driver.find_element(
            By.XPATH,
            '//*[@id="mauticform_input_generalsubscribersformhomepage_subscribe"]',
        ).click()
        if "Thank you for subscribing!" in self.driver.page_source:
            print("email submitted!")
        else:
            print("email not submitted!")

    @unittest.skip("test skipped")
    def test_choose_what_to_learn_python(self):

        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div'
        ).click()
        if "Learn Python Programming" in self.driver.page_source:
            print("Test Successful")
        else:
            print("Test Unsuccessful")

    @unittest.skip("test skipped")
    def test_choose_what_to_learn_java(self):

        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[3]/div'
        ).click()
        if "Learn Java Programming" in self.driver.page_source:
            print("Test Successful")
        else:
            print("Test Unsuccessful")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
