import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class footerSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com")
        self.driver.execute_script("window.scrollTo(0, 3500)")

    # @unittest.skip("test skipped")
    def test_footer_tutorial(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[2]/div/ul/li[8]/a"
        ).click()
        time.sleep(3)
        current_title = self.driver.title
        expected_title = "Learn Swift Programming"

        self.assertEqual(current_title, expected_title)

    # @unittest.skip("test skipped")
    def test_foter_examples(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[3]/div/ul/li[2]/a"
        ).click()
        time.sleep(3)
        current_url = self.driver.current_url
        expected_url = "https://dev.programiz.com/javascript/examples"

        self.assertEqual(current_url, expected_url)

    # @unittest.skip("test skipped")
    def test_footer_companny_about(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[4]/div/ul/li[3]/a"
        ).click()
        time.sleep(3)
        a = self.driver.title
        b = "About Us"

        self.assertEqual(a, b)

    # @unittest.skip("test skipped")
    def test_footer_company_contact(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[4]/div/ul/li[3]/a"
        ).click()
        time.sleep(3)
        title = self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/h1"
        ).is_displayed()

        self.assertTrue(title)

    # @unittest.skip("test skipped")
    def test_footer_company_youtube(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[4]/div/ul/li[9]/a"
        ).click()
        time.sleep(2)
        get_url = self.driver.current_url
        expectedUrl = "https://www.youtube.com/channel/UCREFp3D_n8JfcDonlm7Mpyw"

        self.assertEqual(get_url, expectedUrl)

    # @unittest.skip("test skipped")
    def test_footer_Apps(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[2]/div[5]/div/ul/li[3]/a"
        ).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertTrue(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="node-2319"]/div/div[1]/div/div/div[1]/div/div/div[2]/img',
            ).is_displayed()
        )

    def test_footer_facebook_icon(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[4]/div/a[1]"
        ).click()
        time.sleep(2)
        facebook_url = self.driver.current_url
        expected_facebook_url = "https://www.facebook.com/programiz"

        self.assertEqual(facebook_url, expected_facebook_url)

    def test_footer_linkedin_icon(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/footer/div[1]/div[4]/div/a[3]"
        ).click()
        time.sleep(2)
        linkedin_url = self.driver.current_url
        expected_linkedin_url = "https://www.linkedin.com/company/programiz"

        self.assertEqual(linkedin_url, expected_linkedin_url)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
