# frame 补充练习
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    stockName = stock[1].text
    stodeCode = stock[0].text
    totalNu = totalNu+1

    # * 执行点击代码
    oldWin = wd.current_window_handle
    # 点击数据按钮
    ele.find_element(
        By.CSS_SELECTOR, 'td:nth-child(4) > a:nth-child(3)').click()
    sleep(2)

    # 切换新窗口
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        # 得到标题栏字符串 判断是否是需操作的窗口
        if stockName in wd.title:

            # 因为都是简介信息都可以显示的 直接用列表推导式 + text 获取
            companyInfo = [ele.text for ele in wd.find_elements(By.CSS_SELECTOR, '#m_gsjj td')]
            companyInfoStr = ' '.join(companyInfo)
            companyInfoStr = f'{stockName} {stodeCode} {companyInfoStr}'

            with open('03selenium/day5/test.csv','a',encoding='gbk',newline='')as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(companyInfoStr)

            break

    wd.close()
    # 回到旧窗口
    wd.switch_to.window(oldWin)
    sleep(1)

    # 10 次跳出循环
    if totalNu == 2:
        break

wd.quit()