# 选择框 补充作业 取前 10条的股票 名称和代码
# 并且点开每一个股票公司的 相关链接栏目 里面的 数据 链接
# 切换到新打开的页面，点击公司概况，获取公司简介相关信息
# 最终以csv格式存储在文件中。（请自行网上搜索python如何以csv格式存储文件
import csv
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 记录所有股票与代码
stock_dict = {}
# 记录一个股票的信息
info_dict = {}
# 记录全有股票的
stock_info_dict = {}

wd = webdriver.Chrome()
wd.implicitly_wait(5)
# 股票网址
wd.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")
sleep(2)


eles = wd.find_elements(By.CSS_SELECTOR, "tbody > tr")
# 循环10次
totalNu = 0
# * 读取的是10页
# ele 是每一行
for ele in eles:
    # stock 是股票代码和名称
    stock = ele.find_elements(
        By.CSS_SELECTOR, 'td:nth-child(2),td:nth-child(3)')
    # k是股票名称 v是股票代码
    stock_dict[stock[1].text] = stock[0].text
    totalNu = totalNu+1

    # * 执行点击代码
    oldWin = wd.current_window_handle
    # 点击数据按钮
    ele.find_element(
        By.CSS_SELECTOR, 'td:nth-child(4) > a:nth-child(3)').click()
    sleep(2)
    # 切换新窗口
    stockName = stock[1].text
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        # 得到标题栏字符串 判断是否是需操作的窗口
        if stockName in wd.title:
            # print(wd.title)
            # 执行点击公司概况
            wd.find_element(By.CSS_SELECTOR, 'li[data-href="gsgk"]').click()
            sleep(2)

            # 简介中所有标题 8个
            titles = wd.find_elements(By.CSS_SELECTOR, '#gsgk tbody .bg')
            contents = wd.find_elements(
                By.CSS_SELECTOR, '#gsgk #gsjj_ggmc,#gsjj_frdb,#gsjj_zcdz,#gsjj_zczb,#gsjj_clrq,#gsjj_ssrq,#gsjj_zyfw,#gsjj_gsjj')

            # 信息有8个
            for i in range(0, 8):
                info_dict[titles[i].text] = contents[i].text

            stock_info_dict[stockName] = info_dict

            break

    # 回到旧窗口
    wd.switch_to.window(oldWin)
    sleep(1)

    # 10 次跳出循环
    if totalNu == 2:
        break

for k,v in stock_dict.items():
    print(f'{k}\t{v}')

for k,v in stock_info_dict.items():
    print(f'{k}\t{v}')

wd.quit()



# 引用 csv 模块
with open('03selenium/day5/test.csv','w',newline='',encoding='gbk') as f:
    writer = csv.writer(f)
    writer.writerow(str(stock_dict))
    writer.writerow(str(info_dict))
    writer.writerow(str(stock_info_dict))
