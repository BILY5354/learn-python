# frame `UI-0106` 新窗口练习
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
sleep(2)

# 保存旧窗口句柄
oldWin = wd.current_window_handle

wd.find_element(By.CSS_SELECTOR,
                'div[class="pull-right hidden-xs"] > a:nth-child(1)').click()
sleep(2)

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 判断是否是需要操作的窗口
    if '白月黑羽' in wd.title:
        # 使窗口最大化
        wd.maximize_window()
        eles = wd.find_elements(By.CSS_SELECTOR,'ul[class="navbar-nav d-md-inline-flex"] > li')
        for ele in eles:
            print(ele.find_element(By.CSS_SELECTOR,'span').text)
        break

# 切换会一开始的窗口
wd.switch_to.window(oldWin)
sleep(2)
# 点击右上角 管理员 
wd.find_element(By.CSS_SELECTOR,'.dropdown.user>a:nth-child(1)').click()
sleep(2)
wd.find_element(By.CSS_SELECTOR,'.pull-right>a[class="btn btn-default btn-flat"]').click()
wd.quit()
input()