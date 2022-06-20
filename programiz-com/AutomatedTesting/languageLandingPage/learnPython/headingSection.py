import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(3)


class heading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.programiz.com/python-programming")

    @unittest.skip("test skipped")
    def test_python_page_heading(self):
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
            ).text,
            "Learn Python Programming",
        )

    @unittest.skip("test skipped")
    def test_try_pro_for_free_button(self):
        wait()
        time.sleep(10)
        self.driver.find_element(
            By.XPATH, "/html/body/main/header/nav/div/div/div[3]/a/p[1]"
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="__next"]/main/div/section[1]/div/div/div[2]/section/div/h1',
            ).text,
            "Become a Python Master",
        )

    @unittest.skip("test skipped")
    def test_tutorials_button(self):
        wait()
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[1]"
        ).click()
        self.driver.refresh()
        wait()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/h1"
            ).text,
            "Learn Python Programming",
        )

    @unittest.skip("test skipped")
    def test_course_button(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[2]"
        ).click()

        self.assertEqual(
            self.driver.current_url,
            "https://programiz.pro/learn/master-python?utm_source=landing-nav=programiz&utm_medium=referral",
        )

    @unittest.skip("test skipped")
    def test_examples_button(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[3]"
        ).click()

        wait()

        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div.col-sm-12",
            ).is_displayed()
        )

        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div:nth-child(2)",
            ).is_displayed()
        )
        time.sleep(5)
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div:nth-child(3)",
            ).is_displayed()
        )
        wait()
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div:nth-child(4)",
            ).is_displayed()
        )
        wait()
        self.assertTrue(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "body > main > div.contents.contents--neg-120 > div > div.row.d-none.d-md-flex > div:nth-child(5)",
            ).is_displayed()
        )

    @unittest.skip("test skipped")
    def test_examples_button_all_examples(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[3]"
        ).click()

        wait()
        a = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > main > div.contents.contents--neg-120 > div > div.example-contents > div > div",
        )
        a = a.find_elements(By.TAG_NAME, "li")
        l = []
        for i in a:
            i = i.find_element(By.TAG_NAME, "a")
            l.append(i.text)
        all_example_list = [
            "Python Program to Print Hello world!",
            "Python Program to Add Two Numbers",
            "Python Program to Find the Square Root",
            "Python Program to Calculate the Area of a Triangle",
            "Python Program to Solve Quadratic Equation",
            "Python Program to Swap Two Variables",
            "Python Program to Generate a Random Number",
            "Python Program to Convert Kilometers to Miles",
            "Python Program to Convert Celsius To Fahrenheit",
            "Python Program to Check if a Number is Positive, Negative or 0",
            "Python Program to Check if a Number is Odd or Even",
            "Python Program to Check Leap Year",
            "Python Program to Find the Largest Among Three Numbers",
            "Python Program to Check Prime Number",
            "Python Program to Print all Prime Numbers in an Interval",
            "Python Program to Find the Factorial of a Number",
            "Python Program to Display the multiplication Table",
            "Python Program to Print the Fibonacci sequence",
            "Python Program to Check Armstrong Number",
            "Python Program to Find Armstrong Number in an Interval",
            "Python Program to Find the Sum of Natural Numbers",
            "Python Program to Display Powers of 2 Using Anonymous Function",
            "Python Program to Find Numbers Divisible by Another Number",
            "Python Program to Convert Decimal to Binary, Octal and Hexadecimal",
            "Python Program to Find ASCII Value of Character",
            "Python Program to Find HCF or GCD",
            "Python Program to Find LCM",
            "Python Program to Find the Factors of a Number",
            "Python Program to Make a Simple Calculator",
            "Python Program to Shuffle Deck of Cards",
            "Python Program to Display Calendar",
            "Python Program to Display Fibonacci Sequence Using Recursion",
            "Python Program to Find Sum of Natural Numbers Using Recursion",
            "Python Program to Find Factorial of Number Using Recursion",
            "Python Program to Convert Decimal to Binary Using Recursion",
            "Python Program to Add Two Matrices",
            "Python Program to Transpose a Matrix",
            "Python Program to Multiply Two Matrices",
            "Python Program to Check Whether a String is Palindrome or Not",
            "Python Program to Remove Punctuations From a String",
            "Python Program to Sort Words in Alphabetic Order",
            "Python Program to Illustrate Different Set Operations",
            "Python Program to Count the Number of Each Vowel",
            "Python Program to Merge Mails",
            "Python Program to Find the Size (Resolution) of a Image",
            "Python Program to Find Hash of File",
            "Python Program to Create Pyramid Patterns",
            "Python Program to Merge Two Dictionaries",
            "Python Program to Safely Create a Nested Directory",
            "Python Program to Access Index of a List Using for Loop",
            "Python Program to Flatten a Nested List",
            "Python Program to Slice Lists",
            "Python Program to Iterate Over Dictionaries Using for Loop",
            "Python Program to Sort a Dictionary by Value",
            "Python Program to Check If a List is Empty",
            "Python Program to Catch Multiple Exceptions in One Line",
            "Python Program to Copy a File",
            "Python Program to Concatenate Two Lists",
            "Python Program to Check if a Key is Already Present in a Dictionary",
            "Python Program to Split a List Into Evenly Sized Chunks",
            "Python Program to Parse a String to a Float or Int",
            "Python Program to Print Colored Text to the Terminal",
            "Python Program to Convert String to Datetime",
            "Python Program to Get the Last Element of the List",
            "Python Program to Get a Substring of a String",
            "Python Program to Print Output Without a Newline",
            "Python Program Read a File Line by Line Into a List",
            "Python Program to Randomly Select an Element From the List",
            "Python Program to Check If a String Is a Number (Float)",
            "Python Program to Count the Occurrence of an Item in a List",
            "Python Program to Append to a File",
            "Python Program to Delete an Element From a Dictionary",
            "Python Program to Create a Long Multiline String",
            "Python Program to Extract Extension From the File Name",
            "Python Program to Measure the Elapsed Time in Python",
            "Python Program to Get the Class Name of an Instance",
            "Python Program to Convert Two Lists Into a Dictionary",
            "Python Program to Differentiate Between type() and isinstance()",
            "Python Program to Trim Whitespace From a String",
            "Python Program to Get the File Name From the File Path",
            "Python Program to Represent enum",
            "Python Program to Return Multiple Values From a Function",
            "Python Program to Get Line Count of a File",
            "Python Program to Find All File with .txt Extension Present Inside a Directory",
            "Python Program to Get File Creation and Modification Date",
            "Python Program to Get the Full Path of the Current Working Directory",
            "Python Program to Iterate Through Two Lists in Parallel",
            "Python Program to Check the File Size",
            "Python Program to Reverse a Number",
            "Python Program to Compute the Power of a Number",
            "Python Program to Count the Number of Digits Present In a Number",
            "Python Program to Check If Two Strings are Anagram",
            "Python Program to Capitalize the First Character of a String",
            "Python Program to Compute all the Permutation of the String",
            "Python Program to Create a Countdown Timer",
            "Python Program to Count the Number of Occurrence of a Character in String",
            "Python Program to Remove Duplicate Element From a List",
            "Python Program to Convert Bytes to a String",
        ]

        self.assertEqual(l, all_example_list)

    # @unittest.skip("test skipped")
    def test_references_button(self):
        wait()
        print("asdasd")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[6]/div[1]/div[1]/div/div/div/div[1]/div/div/a[4]",
        ).click()
        time.sleep(5)

        self.assertTrue(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="views-exposed-form-python-methods-reference-page"]/div/div/div[2]',
            ).is_displayed()
        )

        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[1]/div/h3/a"
            ).text,
            "Python Built-in Functions",
        )

        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[2]/div/h3/a"
            ).text,
            "Python Dictionary Methods",
        )
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[3]/div/h3/a"
            ).text,
            "Python List Methods",
        )
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[4]/div/h3/a"
            ).text,
            "Python Set Methods",
        )
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[5]/div/h3/a"
            ).text,
            "Python String Methods",
        )
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, "/html/body/main/div[6]/div[2]/div/div/div/div[6]/div/h3/a"
            ).text,
            "Python Tuple Methods",
        )

    @unittest.skip("test skipped")
    def test_compiler_button(self):
        self.driver.find_element(
            By.XPATH, "/html/body/main/div[6]/div/div/div/div[1]/div/div/a[5]"
        ).click()
        self.assertEqual(
            self.driver.find_element(
                By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[1]/div[2]/h1/a/span/span'
            ).text,
            "Python Online Compiler",
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
