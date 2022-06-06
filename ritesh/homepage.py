from cgitb import html
from lib2to3.pgen2 import driver
from time import time
from turtle import title
import unittest
from webbrowser import Chrome
# from unittest.main import _TestRunner
import HtmlTestRunner
from pytest import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        


    def test_homepage_logo(self):
        
        self.driver.get('https://dev.programiz.com')
        title = self.driver.title
        self.driver.refresh()
        title2 = self.driver.title
        self.assertEqual(title, title2)
        

    
    def test_search(self):
        
        self.driver.get('https://dev.programiz.com')
        self.driver.find_element(By.XPATH,'//*[@id="edit-keys-2"]').send_keys('python',Keys.ENTER)
        if "Learn Python With 100+ Challenges — Enroll for Free" in self.driver.page_source:
            print('Search Test Successful')
        else:
            print('Search Test Failed')
         
        #  self.assertNotIn("No results found.", self.driver.page_source)



    def test_tutorials(self):
        
        self.driver.get('https://dev.programiz.com')
        self.driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[2]/a[2]/span').click()
        list_new = self.driver.find_elements_by_xpath(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div')
        self.assertEqual(10,len(list_new))



    def learn_to_code_for_free(self):
        
        self.driver.get('https://dev.programiz.com')
        if "Learn to Code for Free Learn to code with our beginner-friendly tutorials and examples. Read tutorials and examples, write programs, run code and learn to code." in self.driver.page_source:
            print('h1 and para are present in the homepage')
        else:
            print('h1 and para are not present in the homepage')
        


    def homepage_image(self):
        
        self.driver.get('https://dev.programiz.com')
        img = self.driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[1]/div[2]/img')
        if(img.is_displayed()):
            print("Image is displayed")
        else:
            print("Image is not displayed")
        


    def test_latest_updates(self):
        self.driver.get('https://dev.programiz.com')
        self.driver.find_element(By.XPATH,'//*[@id="mauticform_input_generalsubscribersformhomepage_email1"]').send_keys('abc@gmail.com')
        WebDriverWait(Chrome,3)
        self.driver.find_element(By.XPATH,'//*[@id="mauticform_input_generalsubscribersformhomepage_subscribe"]').click()
        if "Thank you for subscribing!" in self.driver.page_source:
            print('email submitted!')
        else:
            print('email not submitted!')



    def choose_what_to_learn_python(self):
        
        self.driver.get('https://dev.programiz.com')
        self.driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div').click()
        if "Learn Python Programming" in self.driver.page_source:
            print('Test Successful')
        else:
            print('Test Unsuccessful')



    def choose_what_to_learn_java(self):
        
        self.driver.get('https://dev.programiz.com')
        self.driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[3]/div').click()
        if "Learn Java Programming" in self.driver.page_source:
            print('Test Successful')
        else:
            print('Test Unsuccessful')






         
    def tearDown(self):

        self.driver.close(testRunner = HtmlTestRunner.HTMLTestRunner(output='D:\Programiz Intern\June 2022\programiz-testing\Reports'))













#html report
# report_TestRunner = HtmlTestRunner.HTMLTestRunner(output='D:\Programiz Intern\June 2022\programiz-testing\Reports')



# def test_homepage_logo1(self):
#          self.driver.get('https://dev.programiz.com')
         
#          beforeTitle = self.driver.title
#          self.driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div/h3').click()
#         #  time.sleep(2)
#          afterTitle = self.driver.title

#          self.assertEqual(beforeTitle, afterTitle)
   
         


if __name__ == '__main__':
    unittest.main()