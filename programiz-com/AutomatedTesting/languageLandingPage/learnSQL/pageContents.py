import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(10)


class contents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/sql")

    def test_page_index_card(self):
        a = self.driver.find_element(
            By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]"
        )
        a = a.find_elements(By.TAG_NAME, "li")
        l = []
        for i in a:
            l.append(i.text)

        list_new = [
            "Introduction",
            "SQL SELECT (I)",
            "SQL SELECT (II)",
            "SQL JOIN",
            "SQL Database",
            "SQL Insert and Delete",
            "SQL Constraints",
            "SQL Additional Topics",
            "About SQL",
            "Why learn SQL?",
            "How to Learn SQL?",
        ]

        self.assertEqual(l, list_new)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
