import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait():
    time.sleep(3)


class popularExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_program_to_check_prime_number(self):
        self.driver.get("https://dev.programiz.com/python-programming/examples")
        wait()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div:nth-child(2)",
        ).click()

    @unittest.skip("test skipped")
    def test_for_loop(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/prime-number"
        )
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/ul/li[2]/a"
        ).click()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Python for Loop",
        )

    @unittest.skip("test skipped")
    def test_run_code(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/prime-number"
        )
        self.driver.find_element(
            By.XPATH, '//*[@id="node-98"]/div/div[1]/div[2]/a'
        ).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[1]/div[2]/h1/a/span/span'
            ).text,
            "Python Online Compiler",
        )

    @unittest.skip("test skipped")
    def test_happy_face_emoji(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/prime-number"
        )
        time.sleep(5)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents > div > div.row > div > div.right-bar > div.block > section > div.vote-wrapper > div > div.vote-up",
        ).click()
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[6]/div/div[1]/div/div[2]/div[5]/section/div[4]",
            ).text,
            "We are glad you liked the article. Share with your friends.",
        )
        wait()

    def test_check_armstrong(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/prime-number"
        )
        time.sleep(3)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents > div > div.view.view-similar-python-programming-examples.view-id-similar_python_programming_examples.view-display-id-block.above-bottom-recommended-articles.view-dom-id-775e83e23cae755cc52c545819c39546 > div > div > div:nth-child(5)",
        ).click()

        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/h1"
            ).text,
            "Python Program to Check Armstrong Number",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
