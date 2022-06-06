from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://dev.programiz.com")

driver.maximize_window()

title = driver.title
print(title)


#tutorials_dropdown

driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[2]/a[2]/span').click()

sleep(2)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[2]/a').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[3]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[4]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[5]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[6]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[7]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[8]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[9]/a/span').click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div/div/div/div[1]/div/div[10]/a/span').click()
sleep(1)

driver.find_element(By.XPATH,'//*[@id="t-dsa"]/div/div/a[2]/span').click()
sleep(2)

driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[1]/a/img[2]').click()
sleep(2)


#course_search

driver.find_element(By.XPATH,'//*[@id="edit-keys-2"]').send_keys('python',Keys.ENTER)
sleep(2)
driver.find_element(By.XPATH,'//*[@id="search-api-page-search-form-simplest-programming-tutorials-f"]/div/div/button[2]').click()
sleep(2)
driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[1]/a').click()
sleep(2)


#tutorials and updates

driver.find_element(By.XPATH,'//*[@id="mauticform_input_generalsubscribersformhomepage_email1"]').send_keys('abcde@gmail.com')
sleep(2)
driver.find_element(By.XPATH,'//*[@id="mauticform_input_generalsubscribersformhomepage_subscribe"]').click()
sleep(2)



#choose what to learn

driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div/h3').click()
sleep(2)
driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[1]/a').click()
sleep(2)
driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/div/div[1]').click()
sleep(2)
driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/div/div[1]').click()



#join for free

sleep(2)
driver.execute_script("window.scrollTo(0, 950)")
driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[2]/div/div[1]/div[1]/a/button').click()
sleep(2)
driver.get("https://dev.programiz.com")
sleep(2)
driver.execute_script("window.scrollTo(0, 950)")


driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[2]/div/div[2]/div/div[2]/a[1]/div/h3').click()
sleep(2)
driver.get("https://dev.programiz.com")


#online compilers

sleep(2)
driver.execute_script("window.scrollTo(0, 1800)")


driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[3]/div/div/div[2]/div/a[1]').click()
sleep(2)
driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[1]/a').click()



#mobile app

sleep(2)
driver.execute_script("window.scrollTo(0, 3000)")
sleep(2)
driver.find_element(By.XPATH,'//*[@id="node-368"]/div/div[5]/div/div/div[2]/div/div[2]/a[1]/div').click()
sleep(2)
driver.get("https://dev.programiz.com")


#footer

sleep(2)
driver.execute_script("window.scrollTo(0, 3500)")
sleep(2)
driver.find_element(By.XPATH,'/html/body/main/footer/div/div[2]/div[1]/div/div[2]/div[1]/a/img').click()
sleep(2)
driver.get("https://dev.programiz.com")

