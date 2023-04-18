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


eles = wd.find_elements(By.CSS_SELECTOR, "tbody > tr")
# 循环10次
i = 0
# * 读取的是10页
# ele 是每一行
for ele in eles:
    # stock 是股票代码和名称
    stock = ele.find_elements(
        By.CSS_SELECTOR, 'td:nth-child(2),td:nth-child(3)')
    # k是股票名称 v是股票代码
    stock_dict[stock[1].text] = stock[0].text
    i = i+1

    #* 执行点击代码

    # 10 次跳出循环
    if i == 10:
        break

print(stock_dict)
    
wd.quit()


# # 引用 csv 模块
# csv_file = open('03selenium/day5/test.csv', 'w', newline='', encoding='gbk')
# # 调用open函数打开csv文件
# writer = csv.writer(csv_file)
