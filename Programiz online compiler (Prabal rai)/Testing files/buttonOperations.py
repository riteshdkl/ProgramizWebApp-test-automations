# Here all the operations regarding the buttons are carried out

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from locators import ButtonsLocators, HeadingLocators
from selenium.webdriver.common.by import By


class CompilerButtonClick(object):
    def __init__(self, driver):
        self.driver = driver

    # Secnario 1
    def click_compiler_text_link(self):
        homepage = self.driver.find_element(
            By.CLASS_NAME, HeadingLocators.homepage_button
        )
        homepage.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print("Current title is " + self.driver.title) #Debugging
        sleep(10)
        # print("after loading title is " + self.driver.title) #Debugging
        return self.driver.title

    # Scecnario 2
    def click_learn_app(self):
        pass

    # Scenario 3
    # on hold
    def click_compiler_button(self):

        for buttons in ButtonsLocators:
            print("Buttons is " + buttons)
            button = self.driver.find_element(
                By.CSS_SELECTOR, ButtonsLocators.compiler_buttons[buttons]
            )
            button.click()
