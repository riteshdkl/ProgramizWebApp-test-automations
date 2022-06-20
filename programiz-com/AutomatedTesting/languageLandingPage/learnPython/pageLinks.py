import time
import unittest
from multiprocessing.connection import wait

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(3)


class links(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/python-programming")
        wait()

    # @unittest.skip("test skipped")
    def test_interactive_python_course_link(self):
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
    def test_get_started_with_python_link(self):
        wait()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(2)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[3]/li[2]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/first-program",
        )
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "How to Get Started With Python?",
        )

    # @unittest.skip("test skipped")
    def test_python_tutorial_link(self):
        self.driver.execute_script("window.scrollTo(0, 3200)")
        time.sleep(2)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[3]/li[3]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://docs.python.org/3/tutorial/",
        )
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="the-python-tutorial"]/h1'
            ).text,
            "The Python Tutorial",
        )

    # @unittest.skip("test skipped")
    def test_learn_python_app(self):
        self.driver.execute_script("window.scrollTo(0, 3200)")
        time.sleep(2)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[3]/li[4]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/learn-python",
        )
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="node-2193"]/div/div[1]/div/div/div[1]/div/h1'
            ).text,
            "Learn Python\non the Go",
        )

    # @unittest.skip("test skipped")
    def test_youtube_button(self):
        wait()
        self.driver.find_element(
            By.XPATH, '//*[@id="movie_player"]/div[4]/button'
        ).click()
        wait()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(
            self.driver.current_url,
            "https://www.youtube.com/channel/UCREFp3D_n8JfcDonlm7Mpyw",
        )

    def test_python_examples_link(self):
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[4]/li[1]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/examples",
        )

    def test_python_references_link(self):
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[4]/li[2]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/methods",
        )

    def test_python_online_compiler(self):
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[4]/li[3]/a",
        ).click()
        self.assertEqual(
            self.driver.current_url,
            "https://dev.programiz.com/python-programming/online-compiler/",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
