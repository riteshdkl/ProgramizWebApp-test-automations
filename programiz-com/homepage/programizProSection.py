import time
import unittest
from ast import Assert

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class programizPro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://programiz.com")
        self.driver.execute_script("window.scrollTo(0,950)")
        time.sleep(2)

    @unittest.skip("test skipped")
    def test_join_for_free_Heading(self):
        expectedHeading = "Invest in coding Now\nfor a bright career!"
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[2]/div/div[1]/div[1]/div/h2'
        )
        self.assertEqual(expectedHeading, heading.text)

    @unittest.skip("test skipped")
    def test_join_for_free_button(self):
        nonPro_url = self.driver.current_url
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[2]/div/div[1]/div[1]/a/button'
        ).click()
        pro_url = "https://www.programiz.com/"
        self.assertEqual(nonPro_url, pro_url)

    @unittest.skip("test skipped")
    def test_enroll_now_for_free_heading(self):
        heading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[2]/div/div[2]/div/div[1]/div/h2'
        ).is_displayed()
        self.assertTrue(heading)

    @unittest.skip("test skipped")
    def test_Interactive_python_course(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[2]/div/div[2]/div/div[2]/a[1]/div/h3'
        ).click()
        time.sleep(2)
        get_url = self.driver.current_url
        actualHeading = "Become a Python Master"
        page_heading = self.driver.find_element(
            By.XPATH,
            '//*[@id="__next"]/main/div/section[1]/div/div/div[2]/section/div/h1',
        )

        actual_url = "https://programiz.pro/learn/master-python?utm_source=home-body-enroll-now&utm_campaign=programiz&utm_medium=referral"

        self.assertEqual(actualHeading, page_heading.text)
        self.assertEqual(get_url, actual_url)

    # @unittest.skip("test skipped")
    def test_view_all_courses(self):
        # self.driver.execute_script("window.scrollTo(0,950)")
        time.sleep(2)
        self.driver.find_element(
            By.XPATH,
            '//*[@id="node-368"]/div/div[2]/div/div[2]/div/div[2]/a[3]/div/span',
        ).click()
        time.sleep(2)
        row = self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/div'
        )
        time.sleep(2)
        row = row.find_elements_by_class_name("catalog-card")

        list_new = []

        for i in row:
            list_new.append(i.text)

        actual_list = [
            "Become a Python Master\nLearning Path",
            "Become a C Master\nLearning Path",
            "Learn Python Basics\nCourse",
            "Python Beyond Basics\nCourse",
            "Learn C Programming\nCourse",
            "Python Basics Challenges\nChallenge",
            "Python Beyond Basics Challenges\nChallenge",
            "C Programming Challenges\nChallenge",
            "Become a Java Master\nLearning Path\nComing Soon",
            "Java Basics\nCourse\nComing Soon",
            "Java Basics Challenges\nChallenge\nComing Soon",
            "Java OOP\nCourse\nComing Soon",
            "Java OOP Challenges\nChallenge\nComing Soon",
            "Java Beyond Basics\nCourse\nComing Soon",
            "Java Beyond Basics Challenges\nChallenge\nComing Soon",
        ]
        self.assertEqual(len(list_new), len(actual_list))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
