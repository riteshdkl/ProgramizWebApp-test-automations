import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://dev.programiz.com/python-programming")

time.sleep(2)

l = []

a = driver.find_element(By.CLASS_NAME, "list")
for i in a:
    l.append(i.text)


# a = driver.current_url
# print(a)
# driver.find_element_by_xpath(
#     '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div/h3'
# ).click()
# b = driver.current_url
# print(b)


# driver.find_element_by_xpath(
#     "/html/body/main/header/nav/div/div/div[2]/a[2]/span"
# ).click()

# time.sleep(2)

# d = driver.find_element_by_xpath(
#     "/html/body/main/div[4]/div/div/div/div/div/div[1]/div"
# )

# d = d.find_elements_by_class_name("tabbed-link")

# l = []
# for i in d:
#     l.append(i.text)

# print(l)
