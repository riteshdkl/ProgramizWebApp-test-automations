import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# from multiprocessing.connection import wait


def wait():
    time.sleep(3)


class filesExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # @unittest.skip("test skipped")
    def test_files_text(self):
        self.driver.get("https://dev.programiz.com/python-programming/examples")
        wait()
        self.driver.find_element(
            By.XPATH,
            '//*[@id="edit-select-26"]/a',
        ).click()
        wait()
        a = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents.contents--neg-120 > div > div.example-contents > div > div > div:nth-child(1) > div",
        )
        wait()
        a = a.find_elements(By.TAG_NAME, "li")
        l = []
        for i in a:
            l.append(i.text)
        files_list = [
            "Python Program to Merge Mails",
            "Python Program to Find the Size (Resolution) of a Image",
            "Python Program to Find Hash of File",
            "Python Program to Safely Create a Nested Directory",
            "Python Program to Catch Multiple Exceptions in One Line",
            "Python Program to Copy a File",
            "Python Program Read a File Line by Line Into a List",
            "Python Program to Append to a File",
            "Python Program to Extract Extension From the File Name",
            "Python Program to Get the File Name From the File Path",
            "Python Program to Get Line Count of a File",
            "Python Program to Find All File with .txt Extension Present Inside a Directory",
            "Python Program to Get File Creation and Modification Date",
            "Python Program to Get the Full Path of the Current Working Directory",
            "Python Program to Check the File Size",
        ]

        self.assertEqual(l, files_list)

    @unittest.skip("test skipped")
    def test_check_file_size(self):
        self.driver.get("https://dev.programiz.com/python-programming/examples")
        wait()
        self.driver.find_element(
            By.XPATH,
            '//*[@id="edit-select-26"]/a',
        ).click()
        wait()
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[8]/div/div[3]/div/div/div[1]/div/div/div[2]/ol/li[15]/a",
        ).click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
