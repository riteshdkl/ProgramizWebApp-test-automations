# This is the automation file for the Online compiler
# The actual testing is to be done in the other python file

from selenium import webdriver

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary(
#     "F:\Web drivers for selenium\FireFox\geckodriver-v0.31.0-win64\geckodriver.exe"
# )

# used to initialize the path of edge browser
driver = webdriver.Edge(
    executable_path="F:\Web drivers for selenium\Edge\edgedriver_win64\msedgedriver.exe"
)

driver.get("https://www.programiz.com/c-programming/online-compiler/")

driver.close()
