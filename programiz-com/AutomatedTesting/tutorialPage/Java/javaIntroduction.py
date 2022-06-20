import time
import unittest
from multiprocessing.connection import wait

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(3)


class introduction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_introduction(self):
        self.driver.get("https://dev.programiz.com/java-programming")
        self.driver.find_element(
            By.XPATH, '//*[@id="introduction"]/div/div/ul/li[1]/a'
        ).click()
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Java Hello World Program",
        )

    @unittest.skip("test skipped")
    def test_java_comments(self):
        self.driver.get("https://dev.programiz.com/java-programming/hello-world")
        self.driver.find_element(By.XPATH, '//*[@id="node-801"]/div/ol/li[1]/a').click()
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Java Comments",
        )

    def test_run_code(self):
        self.driver.get("https://dev.programiz.com/java-programming/comments")
        self.driver.find_element(
            By.XPATH, '//*[@id="node-1018"]/div/div[1]/div[2]/a'
        ).click()
        wait()
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait()
        print(self.driver.title)
        self.assertEqual(self.driver.title, "Online Java Compiler")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
