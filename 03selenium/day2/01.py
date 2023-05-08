from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 webdriver 对象
wd = webdriver.Chrome()

# 调用 webdriver 对象 打开指定网址
wd.get("http://127.0.0.1/mgr/sign.html")

element = wd.find_element(By.ID,'username')

element.send_keys('byhy')

wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

input() 