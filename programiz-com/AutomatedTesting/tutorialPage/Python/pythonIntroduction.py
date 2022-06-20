import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(3)


class introduction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip("test skipped")
    def test_getting_started(self):
        self.driver.get("https://dev.programiz.com/python-programming")
        time.sleep(10)
        # a = self.driver.find_element(By.XPATH, '//*[@id="introduction"]/div/div')
        self.driver.find_element(
            By.XPATH,
            '//*[@id="introduction"]/div/div/ul/li[1]/a',
        ).click()
        time.sleep(5)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "How to Get Started With Python?",
        )

    @unittest.skip("test skipped")
    def test_thonny_ide(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        self.driver.find_element(
            By.XPATH, '//*[@id="node-78"]/div/ol[1]/li[1]/a'
        ).click()
        self.assertEqual(self.driver.current_url, "https://thonny.org/")
        self.assertEqual(
            self.driver.find_element(By.XPATH, '//*[@id="maincolumn"]/h1').text,
            "Thonny",
        )

    @unittest.skip("test skipped")
    def test_latest_version(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        self.driver.find_element(
            By.XPATH, '//*[@id="node-78"]/div/ol[2]/li[1]/a'
        ).click()
        self.assertEqual(self.driver.current_url, "https://www.python.org/downloads/")

    @unittest.skip("test skipped")
    def test_run_code(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        self.driver.find_element(
            By.XPATH, '//*[@id="node-78"]/div/div[3]/div[2]/a'
        ).click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[1]/div[2]/h1/a/span/span'
            ).text,
            "Python Online Compiler",
        )

    @unittest.skip("test skipped")
    def test_happy_face_emoji(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        # time.sleep(5)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/section/div[2]/div/div[1]",
        ).click()
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/section/div[4]",
            ).text,
            "We are glad you liked the article. Share with your friends.",
        )

    @unittest.skip("test skipped")
    def test_sad_face_emoji(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        # self.driver.execute_script("window.scrollTo(0, 3000)")
        # time.sleep(3)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/section/div[2]/div/div[2]",
        ).click()
        time.sleep(2)

        self.driver.find_element(
            By.XPATH, '//*[@id="edit-submitted-dislike-feedback"]'
        ).send_keys("asdasdasdasdasdas")
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="edit-submit"]').click()

        time.sleep(3)
        self.assertTrue(
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/section/div[3]/div",
            ).is_displayed()
        )
        time.sleep(3)

    @unittest.skip("test skipped")
    def test_error_message(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        # self.driver.execute_script("window.scrollTo(0, 3000)")
        # time.sleep(3)
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/section/div[2]/div/div[2]",
        ).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="edit-submit"]').click()
        time.sleep(2)
        self.assertTrue(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="webform-client-form-1680"]/div[2]/div[2]/div/div/div/div/div[1]',
            ).is_displayed()
        )

    @unittest.skip("test skipped")
    def test_next_tutorial(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[1]/div[2]/div/div[2]/div[5]/div[1]/div/a",
        ).click()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[2]/div/div[2]/div[4]/h1"
            ).text,
            "Python Keywords and Identifiers",
        )

    # @unittest.skip("test skipped")
    def test_facebook_share(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")
        time.sleep(3)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents > div.container > div.row > div > div.right-bar > div.block > section > div.share-wrapper > div > div:nth-child(1)",
        ).click()
        time.sleep(3)

        self.assertEqual(self.driver.title, "Facebook")

    # @unittest.skip("test skipped")
    def test_related_tutorials(self):
        self.driver.get("https://dev.programiz.com/python-programming/first-program")

        time.sleep(3)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents > div.container > div.view.view-tutorials-related-articles.view-id-tutorials_related_articles.view-display-id-block.above-bottom-recommended-articles.view-dom-id-00a5442e8032761e143f7333d5f74a22 > div > div > div:nth-child(2)",
        ).click()
        time.sleep(3)
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div[1]/div/div[2]/div[4]/h1"
            ).text,
            "Python IDEs and Code Editors",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
