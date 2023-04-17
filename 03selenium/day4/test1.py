# 
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

wd.switch_to.frame('innerFrame')

elements = wd.find_elements(By.CLASS_NAME,'plant')

for element in elements:
    print(element.text)

input()