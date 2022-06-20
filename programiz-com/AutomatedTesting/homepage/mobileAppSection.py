import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class mobileApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com")
        self.driver.execute_script("window.scrollTo(0, 3000)")

    # @unittest.skip("test skipped")
    def test_learn_on_the_go(self):
        expectedHeading = "Learn on the Go: Programiz for iOS & Android"
        actualHeading = self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[5]/div/div/div[1]/h2'
        )

        self.assertEqual(expectedHeading, actualHeading.text)

    # @unittest.skip("test skipped")
    def test_google_play_button(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="node-368"]/div/div[5]/div/div/div[2]/div/div[1]/div/a[1]',
        ).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        get_url = self.driver.current_url
        # print(get_url)
        actual_url = "https://play.google.com/store/apps/dev?id=8227237868464522664"

        self.assertEqual(get_url, actual_url)

    # @unittest.skip("test skipped")
    def test_learn_python_App(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="node-368"]/div/div[5]/div/div/div[2]/div/div[2]/a[2]/div/div[1]/h3',
        ).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        appstore = self.driver.find_element(
            By.XPATH,
            '//*[@id="node-2193"]/div/div[1]/div/div/div[1]/div/div/div[1]/a[2]/img',
        ).is_displayed()
        time.sleep(2)
        self.assertTrue(appstore)

    def test_view_all_mobile_apps(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="node-368"]/div/div[5]/div/div/div[2]/div/div[2]/a[5]'
        ).click()
        time.sleep(2)
        learn_java_app = self.driver.find_element(
            By.XPATH,
            '//*[@id="node-368"]/div/div[5]/div/div/div[2]/div/div[2]/a[5]/span',
        ).is_displayed()
        time.sleep(2)
        self.assertTrue(learn_java_app)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
