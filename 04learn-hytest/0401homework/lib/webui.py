from hytest import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# * 将一些共通的操作写在次文件
def open_browser():
    INFO('打开浏览器')
    # 关闭 chrome 浏览器的日志输出
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)

    GSTORE['wd'] = wd  # 存储全局变量
    GSTORE['By'] = By


def mgr_login():
    wd = GSTORE['wd']

    wd.get('http://127.0.0.1/mgr/sign.html')

    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    wd.find_element_by_tag_name('button').click()

# 创建药品或客户


def insertData(tList):
    wd = GSTORE['wd']
    for j in range(0, 3):
        # input
        eles = wd.find_elements(
            By.CSS_SELECTOR, '.add-one-area .form-control')
        for i in range(0, len(eles)):
            eles[i].send_keys(f'{tList[j][i]}')
        # * 不需要唯一 此处的选择器能找到两个元素
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn-xs').click()
        sleep(1)


def deleteItems(name):
    wd = GSTORE['wd']
    # 判断 是否还有元素 有的话一直删删删
    while wd.find_elements(By.CSS_SELECTOR, '.content .search-result-item'):
        results = wd.find_elements(
            By.CSS_SELECTOR, '.content .search-result-item')

        for res in results:
            # res 是每一个框
            eles = res.find_elements(
                By.CSS_SELECTOR, '.search-result-item-field')

            eleStr = ""
            # 将 每一个框里的文字遍历 添加到字符串中 再根据是否包含来删除
            for ele in eles:
                eleStr += ele.text

            # * 两种情况 name 包含空格即删除订单 不包含即删除药品或客户
            if " " in name:
                if name.split(" ")[0] in eleStr and name.split(" ")[1] in eleStr:
                    #! 订单只有一个按钮即删除 所以下标为0
                    wd.find_elements(
                        By.CSS_SELECTOR, '.content .btn-xs')[0].click()
                    wd.switch_to.alert.accept()  # 点击确认按钮
                    sleep(1)
                    continue  # 继续下一个框
            else:
                if name in eleStr:
                    # 如果存在该名字 则删除 并跳出循环 删除为第二个
                    wd.find_elements(
                        By.CSS_SELECTOR, '.content .btn-xs')[1].click()
                    wd.switch_to.alert.accept()  # 点击确认按钮
                    sleep(1)
                    continue  # 继续下一个框

        # 找不到 name 跳出循环
        break