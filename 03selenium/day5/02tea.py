import time,csv
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

mainHtml = wd.current_window_handle

wd.get('http://quote.eastmoney.com/center/gridlist.html#sh_a_board')
time.sleep(1)

for i in range(1,11):
    # 用 i 来代表精准获取第一行
    trEle = wd.find_element(By.CSS_SELECTOR,f'#table_wrapper-table tbody tr:nth-of-type({i})')
    infolist = trEle.find_elements(By.CSS_SELECTOR, 'td:nth-of-type(2),td:nth-of-type(3),td:nth-of-type(4)')
    # 股票代码
    code = infolist[0].text
    # 股票名称
    name = infolist[1].text
    # 对应的数据按键
    infolist[2].find_element(By.CSS_SELECTOR, 'a:nth-of-type(3)').click()
    for handle in wd.window_handles:
        # 先切换到该窗口
        wd.switch_to.window(handle)
        if name in wd.title:
            # 如果是对应的窗口
            break
    companyInfo = [ele.text for ele in wd.find_elements(By.CSS_SELECTOR, '#m_gsjj td')]
    companyInfostr = ' '.join(companyInfo)
    companyInfostr = f'{name} {code} {companyInfostr}'
    print(companyInfostr)
    with open('03selenium/day5/test.csv', 'a', encoding='gbk', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(companyInfostr)
    wd.close()
    # 返回一开始的窗口
    wd.switch_to.window(mainHtml)

wd.quit()