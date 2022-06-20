import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class navbar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com")

    # @unittest.skip("test skipped")
    def test_homepage_logo(self):

        title = self.driver.title
        self.driver.refresh()
        title2 = self.driver.title
        self.assertEqual(title, title2)

    # @unittest.skip("test skipped")
    def test_search(self):

        self.driver.find_element(By.XPATH, '//*[@id="edit-keys-2"]').send_keys(
            "python", Keys.ENTER
        )
        count_element = self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div/p"
        ).text
        data = count_element
        data = data.replace("results found", "")
        data = int(data)

        self.assertGreater(data, 1)

    # @unittest.skip("test skipped")
    def test_tutorials_dropdown(self):

        self.driver.find_element(
            By.XPATH, "/html/body/main/header/nav/div/div/div[2]/a[2]/span"
        ).click()
        element = self.driver.find_element(
            By.XPATH, "/html/body/main/div[4]/div/div/div/div/div/div[1]/div"
        )

        element = element.find_elements(By.CLASS_NAME, "tabbed-link")

        list_new = []

        for i in element:
            list_new.append(i.text)

        actual_list = [
            "Python",
            "JavaScript",
            "SQL",
            "C",
            "C++",
            "Java",
            "Kotlin",
            "Swift",
            "C#",
            "DSA",
        ]

        self.assertEqual(len(actual_list), len(list_new))

    def test_summer_sale_(self):
        a = self.driver.find_element(
            By.XPATH, "/html/body/main/header/div/div/a/div/p/span[1]"
        ).is_displayed()
        self.assertTrue(a)

        self.driver.find_element(
            By.XPATH, "/html/body/main/header/div/div/a/div/p/span[1]"
        ).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        expectedHeading = "Summer Sale! Save $86"
        actualHeading = self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/main/section[1]/div[2]/h2'
        )
        self.assertEqual(expectedHeading, actualHeading.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="D:\Programiz Intern\June 2022\programiz-testing\programiz-test-automations\programiz-com\Reports\homepageTestReports"
        )
    )
