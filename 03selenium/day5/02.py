# 选择框 补充作业 取前 10条的股票 名称和代码
# 并且点开每一个股票公司的 相关链接栏目 里面的 数据 链接
# 切换到新打开的页面，点击公司概况，获取公司简介相关信息
# 最终以csv格式存储在文件中。（请自行网上搜索python如何以csv格式存储文件
import csv
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

stock_dict = {}

wd = webdriver.Chrome()
wd.implicitly_wait(5)
# 股票网址
wd.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")
sleep(2)

# 获取10条数据
for i in range(1,11):
    pass

page = wd.find_element(By.CSS_SELECTOR, '.paginate_button.current').text
while int(page) <= 10:
    # tables 是由20行组成的表格
    tables = wd.find_elements(By.CSS_SELECTOR, 'tbody tr')
    # table 是每一行
    for table in tables:
        # stock 是股票代码和名称
        stock = table.find_elements(
            By.CSS_SELECTOR, 'td:nth-child(2),td:nth-child(3)')
        # k是股票名称 v是股票代码
        stock_dict[stock[1].text] = stock[0].text
    # 点击下一页
    wd.find_element(By.CSS_SELECTOR, '.paginate_button.current + a').click()
    # 等待刷新 判断目前页数
    sleep(2)
    page = wd.find_element(By.CSS_SELECTOR, '.paginate_button.current').text
wd.quit()



# 引用 csv 模块
csv_file = open('03selenium/day5/test.csv', 'w', newline='', encoding='gbk')
# 调用open函数打开csv文件
writer = csv.writer(csv_file)