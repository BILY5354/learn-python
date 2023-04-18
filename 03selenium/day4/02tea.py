# css 下篇老师代码
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

stock_dict = {}

wd = webdriver.Chrome()
wd.implicitly_wait(5)
# 股票网址
wd.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")

# 获取页数
page = wd.find_element(By.CSS_SELECTOR, '.paginate_button.current').text
sleep(2)
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

with open('03selenium/day4/stock.txt', 'w', encoding='utf8') as f:
    # indent=6 代表缩进6位 另一个是保证原样输出 不转义
    f.write(json.dumps(stock_dict, indent=6, ensure_ascii=False))
