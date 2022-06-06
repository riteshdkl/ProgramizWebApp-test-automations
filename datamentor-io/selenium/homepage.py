import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def test_function_one(self):
        print("Function One Tested")


def setUp(self):
    self.driver = webdriver.Chrome()

def test_google(self):
    self.driver.get("C:\Users\Anisha\Desktop\DMQA\homePage.feature")
    print(self.driver.title)

if __name__ == "__main__":
    unittest.main()
