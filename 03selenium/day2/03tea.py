# 老师代码
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get("https://y.qq.com/n/ryqq/toplist/27")

elements = (wd.find_element(By.CLASS_NAME('songlist__list')))