from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get("http://127.0.0.1/mgr/sign.html")

element = wd.find_element(By.ID,'username')
element.send_keys('byh')

element = wd.find_element(By.ID,'password')
element.send_keys('88888888')

wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

input() 