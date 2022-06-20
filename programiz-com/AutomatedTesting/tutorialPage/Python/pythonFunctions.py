import time
import unittest
from multiprocessing.connection import wait

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(3)


class functions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_function(self):
        self.driver.get("https://dev.programiz.com/python-programming")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a",
        ).click()
        time.sleep(3)
        self.assertTrue(
            self.driver.find_element(By.XPATH, '//*[@id="functions"]').is_displayed()
        )

    @unittest.skip("test skipped")
    def test_python_functions(self):
        self.driver.get("https://dev.programiz.com/python-programming")
        time.sleep(3)

        self.driver.find_element(
            By.XPATH, '//*[@id="functions"]/div/div/ul/li[1]/a'
        ).click()
        time.sleep(3)

        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Python Functions",
        )

    @unittest.skip("test skipped")
    def test_rules_of_writing_identifiers(self):
        self.driver.get("https://dev.programiz.com/python-programming/function")
        wait()
        self.driver.find_element(
            By.XPATH, '//*[@id="node-58"]/div/ol[1]/li[2]/a'
        ).click()
        wait()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/keywords-identifier#rules",
        )

    @unittest.skip("test skipped")
    def test_python_global_keywords(self):
        self.driver.get("https://dev.programiz.com/python-programming/function")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[2]/div/div[1]/div[5]/div/div/div/ul/li[6]/div/span/a",
        ).click()
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Python Global Keyword",
        )

    # @unittest.skip("test skipped")
    def test_run_code(self):
        self.driver.get("https://dev.programiz.com/python-programming/function")
        # print(a)
        self.driver.find_element(
            By.XPATH, '//*[@id="node-58"]/div/div[6]/div[2]/a'
        ).click()
        wait()
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[1]/div[2]/h1/a/span/span'
            ).text,
            "Python Online Compiler",
        )

    @unittest.skip("test skipped")
    def test_previous_tutorial(self):
        self.driver.get("https://dev.programiz.com/python-programming/function")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[2]/div/div[2]/div[5]/div[1]/div[1]/a",
        ).click()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Python pass statement",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
