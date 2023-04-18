# css 下篇  `UI-0105` 登陆并添加药品
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = webdriver.Chrome()

wd.get("http://127.0.0.1/mgr/sign.html")

ele = wd.find_element(By.CSS_SELECTOR, 'input[id="username"]')
ele.send_keys('byhy')
ele = wd.find_element(By.CSS_SELECTOR, 'input[id="password"]')
ele.send_keys('88888888')

wd.find_element(By.CSS_SELECTOR,
                'button[class="btn btn-primary btn-block btn-flat"]').click()

# * 防止代码运行比浏览器反应快 让它等等
sleep(2)
wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]').click()
sleep(2)
wd.find_element(By.CSS_SELECTOR,
                'button[class="btn btn-green btn-outlined btn-md"]').click()

# * 用css 下篇的内容找元素
sleep(2)
eles = wd.find_elements(By.CSS_SELECTOR, ".col-lg-8  input:nth-child(1)")
eles[0].send_keys('新的药')
sleep(2)
eles[1].send_keys('新的编号')
sleep(2)
wd.find_element(By.CSS_SELECTOR,
                'div[class="col-lg-12 col-md-12 col-sm-12"] > :nth-child(1)').click()

input()
