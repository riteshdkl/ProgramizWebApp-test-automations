import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(10)


class contents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/python-programming")

    @unittest.skip("test skipped")
    def test_page_index_card(self):
        a = self.driver.find_element(
            By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div"
        )
        a = a.find_elements(By.TAG_NAME, "li")
        index_li = []
        for i in a:
            index_li.append(i.text)
        index_list = [
            "Introduction",
            "Flow Control",
            "Function",
            "Data Types",
            "File Handling",
            "Object & Class",
            "Advanced Tutorials",
            "Date and Time",
            "About Python Programming",
            "Why learn Python ?",
            "How to learn Python?",
            "Python Resources",
        ]
        self.assertEqual(index_li, index_list)

    @unittest.skip("test skipped")
    def test_introduction_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="introduction"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        intro_li = []
        for i in a:
            intro_li.append(i.text)

        intro_list = [
            "Getting Started",
            "Keywords and Identifiers",
            "Statements & Comments",
            "Python Variables",
            "Python Datatypes",
            "Python Type Conversion",
            "Python I/O and import",
            "Python Operators",
            "Python Namespace",
        ]

        self.assertEqual(intro_li, intro_list)

    @unittest.skip("test skipped")
    def test_python_flow_control_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="flow-control"]/div')
        a = a.find_elements(By.TAG_NAME, "li")
        flow_li = []
        for i in a:
            flow_li.append(i.text)

        flow_list = [
            "Python if...else",
            "Python for Loop",
            "Python while Loop",
            "Python break and continue",
            "Python Pass",
        ]

        self.assertEqual(flow_li, flow_list)

    @unittest.skip("test skipped")
    def test_python_function_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="functions"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        func_li = []
        for i in a:
            func_li.append(i.text)

        func_list = [
            "Python Functions",
            "Function Argument",
            "Python Recursion",
            "Anonymous Function",
            "Global, Local and Nonlocal",
            "Python Global Keyword",
            "Python Modules",
            "Python Package",
        ]

        self.assertEqual(func_li, func_list)

    @unittest.skip("test skipped")
    def test_python_datatypes_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="datatypes"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        datatypes_li = []
        for i in a:
            datatypes_li.append(i.text)

        datatypes_list = [
            "Python Numbers",
            "Python List",
            "Python Tuple",
            "Python String",
            "Python Set",
            "Python Dictionary",
        ]

        self.assertCountEqual(datatypes_li, datatypes_list)

    @unittest.skip("test skipped")
    def test_python_files_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="files"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        files_li = []
        for i in a:
            files_li.append(i.text)

        files_list = [
            "Python File Operation",
            "Python Directory",
            "Python Exception",
            "Python Exception Handling",
            "Python User-defined Exception",
        ]

        self.assertEqual(files_li, files_list)

    @unittest.skip("test skipped")
    def test_python_obj_class_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="object-class"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        objcls_li = []
        for i in a:
            objcls_li.append(i.text)

        objcls_list = [
            "Python OOP",
            "Python Class",
            "Python Inheritance",
            "Multiple Inheritance",
            "Operator Overloading",
        ]

        self.assertEqual(objcls_li, objcls_list)

    @unittest.skip("test skipped")
    def test_python_advanced_topics_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="advanced-topic"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        advanced_li = []
        for i in a:
            advanced_li.append(i.text)

        advanced_list = [
            "Python Iterator",
            "Python Generator",
            "Python Closure",
            "Python Decorators",
            "Python Property",
            "Python RegEx",
            "Python Examples",
        ]
        self.assertEqual(advanced_li, advanced_list)

    @unittest.skip("test skipped")
    def test_python_date_time_card(self):
        a = self.driver.find_element(By.XPATH, '//*[@id="date-time"]/div/div')
        a = a.find_elements(By.TAG_NAME, "li")
        date_time_li = []
        for i in a:
            date_time_li.append(i.text)

        date_time_list = [
            "Python datetime Module",
            "Python datetime.strftime()",
            "Python datetime.strptime()",
            "Current date & time",
            "Get current time",
            "Timestamp to datetime",
            "Python time Module",
            "Python time.sleep()",
        ]

        self.assertEqual(date_time_li, date_time_list)

    @unittest.skip("test skipped")
    def test_about_python_programming(self):
        self.assertEqual(
            self.driver.find_element(By.XPATH, '//*[@id="about"]').text,
            "About Python Programming",
        )
        li = [
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[1]/li[1]",
            ).text,
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[1]/li[2]",
            ).text,
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[1]/li[3]",
            ).text,
        ]
        list_new = [
            "Free and open-source - You can freely use and distribute Python, even for commercial use.",
            "Easy to learn - Python has a very simple and elegant syntax. It's much easier to read and write Python programs compared to other languages like C++, Java, C#.",
            "Portable - You can move Python programs from one platform to another, and run it without any changes.",
        ]

        self.assertEqual(li, list_new)

    @unittest.skip("test skipped")
    def test_why_learn_python(self):
        self.assertEqual(
            self.driver.find_element(By.XPATH, '//*[@id="why"]').text,
            "Why Learn Python?",
        )

        li = [
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[2]/li[1]",
            ).text,
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[2]/li[2]",
            ).text,
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[2]/li[3]",
            ).text,
            self.driver.find_element(
                By.XPATH,
                "/html/body/main/div[7]/div/div/div/div/div[2]/div[13]/ul[2]/li[4]",
            ).text,
        ]

        list_new = [
            "Python is easy to learn. Its syntax is easy and code is very readable.",
            "Python has a lot of applications. It's used for developing web applications, data science, rapid application development, and so on.",
            "Python allows you to write programs in fewer lines of code than most of the programming languages.",
            "The popularity of Python is growing rapidly. Now it's one of the most popular programming languages.",
        ]

        self.assertEqual(li, list_new)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
