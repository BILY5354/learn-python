from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get("http://127.0.0.1/mgr/sign.html")

element = wd.find_element(By.CSS_SELECTOR, 'input[id="username"]')
element.send_keys('byh')

element = wd.find_element(By.CSS_SELECTOR,'input[id="password"]')
element.send_keys('88888888')

wd.find_element(By.CSS_SELECTOR,'button[class="btn btn-primary btn-block btn-flat"]').click()

input()