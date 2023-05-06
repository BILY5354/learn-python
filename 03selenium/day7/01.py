# 获取所有教程所有信息
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


wd = webdriver.Chrome()
wd.get("http://v3.byhy.net/tut/py/extra/file_dir/")
sleep(1)

titles = wd.find_elements(By.CSS_SELECTOR, '.docs-sidenav li')
i=21
for title in titles:
    print (f'## {i}.{title.text}')
    i+=1

input()