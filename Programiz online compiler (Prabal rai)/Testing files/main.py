# This is the main python file for automation and testing

import unittest

import buttonOperations
from selenium import webdriver


class OnlinecompilerTesting(unittest.TestCase):
    def setUp(self):
        # used to initialize the path of edge browser
        self.driver = webdriver.Firefox(
            # executable_path="F:\Web drivers for selenium\Edge\edgedriver_win64\msedgedriver.exe"
        )
        self.driver.get("https://www.programiz.com/c-programming/online-compiler/")
        self.driver.maximize_window()

    # Scenario 1 Completed
    # def test_homepage_link_click(self):
    #     homeButtonClick = buttonOperations.CompilerButtonClick(self.driver)
    #     self.assertEqual(
    #         homeButtonClick.click_compiler_text_link(),
    #         "Programiz: Learn to Code for Free",
    #         "This is not the home page",
    #     )

    # Scenario 3
    def test_buttonClick(self):
        buttonClick = buttonOperations.CompilerButtonClick(self.driver)
        buttonClick.click_compiler_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
