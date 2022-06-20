import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# def wait():
#     time.sleep(5)


class allExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # @unittest.skip("test skipped")
    def test_hello_world(self):
        self.driver.get("https://dev.programiz.com/python-programming/examples")
        time.sleep(5)
        self.wait = WebDriverWait(self.driver, 10)
        element = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "body > main > div.contents.contents--neg-120 > div > div.example-contents > div > div > div.tabbed-content.d-block.d-lg-flex.view.view-python-programming-examples-page.view-id-python_programming_examples_page.view-display-id-page.examples-page-views.view-dom-id-5fc1ce27c8bbc1b96eb4b03cb9cba872.jquery-once-2-processed > div.tabbed-content__right > ol > li:nth-child(1)",
                )
            )
        )
        element.click()
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[8]/div/div[3]/div/div/div[1]/div[2]/ol/li[1]",
        ).click()

        # self.driver.close()

        # self.assertEqual(
        #     self.driver.find_element(
        #         By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/h1"
        #     ).text,
        #     "Python Program to Print Hello world!",
        # )

    @unittest.skip("test skipped")
    def test_how_to_get_started(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/hello-world"
        )
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/ul/li[1]/a"
        ).click()

        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "How to Get Started With Python?",
        )
        # self.driver.close()

    @unittest.skip("test skipped")
    def test_convert_km(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/hello-world"
        )
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[1]/div/div[1]/div[1]/div/div/div/ul/li[8]/div/span/a",
        ).click()

        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/examples/km-mile",
        )
        # self.driver.close()

    @unittest.skip("test skipped")
    def test_python_string(self):
        self.driver.get(
            "https://dev.programiz.com/python-programming/examples/hello-world"
        )
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div/div[1]/div/div[1]/div[3]/div/div/div/ul/li[3]/div/span/a",
        ).click()

        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/string",
        )
        # self.driver.close()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
