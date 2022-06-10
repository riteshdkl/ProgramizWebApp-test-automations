import time
import unittest
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from xml.dom.minidom import Element

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class navbar(unittest.TestCase):
    def wait():
        time.sleep(5)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/python-programming")

    @unittest.skip("test skipped")
    def test_python_page_heading(self):
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
            ).text,
            "Learn Python Programming",
        )

    @unittest.skip("test skipped")
    def test_try_pro_for_free_button(self):
        wait()
        self.driver.find_element(
            By.XPATH, "/html/body/main/header/nav/div/div/div[3]/a"
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="__next"]/main/div/section[1]/div/div/div[2]/section/div/h1',
            ).text,
            "Become a Python Master",
        )

    @unittest.skip("test skipped")
    def test_tutorials_button(self):
        wait()
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[1]"
        ).click()
        self.driver.refresh()
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
            ).text,
            "Learn Python Programming",
        )

    @unittest.skip("test skipped")
    def test_course_button(self):
        wait()
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[2]"
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://programiz.pro/learn/master-python?utm_source=landing-nav=programiz&utm_medium=referral",
        )
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="__next"]/main/div/section[1]/div/div/div[2]/section/div/h1',
            ).text,
            "Become a Python Master",
        )

    # @unittest.skip("test skipped")
    def test_examples_button(self):

        # while (
        #     len(
        #         self.driver.find_element(
        #             By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[3]"
        #         )
        #     )
        #     == 0
        # ):
        # pass
        # WebDriverWait(self.driver, 10)
        wait(self)
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[3]"
        ).click()
        # WebDriverWait(self.driver, 10)
        # self.assertEqual(
        #     self.driver.find_element(
        #         By.XPATH, "/html/body/main/div[7]/div/div/div/div[1]/div/h1"
        #     ).text(),
        #     "Python Examples",
        # )
        # time.sleep(10)
        # a = self.driver.find_element(
        #     By.XPATH, "/html/body/main/div[8]/div/div[1]/div[2]/a/div"
        # ).text
        # print(a)

        # wait()
        # self.driver.find_element(
        #     By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[3]"
        # ).click()
        # wait()
        # a = self.driver.find_element(
        #     By.CLASS_NAME,
        #     "ctools-auto-submit-full-form ctools-auto-submit-processed jquery-once-2-processed",
        # )
        # print(a.text)

    @unittest.skip("test skipped")
    def test_page_index(self):
        a = self.driver.find_element(
            By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]"
        )
        a = a.find_elements(By.TAG_NAME, "li")
        l = []
        for i in a:
            l.append(i.text)
        print(l)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
