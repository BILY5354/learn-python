# frame `UI-0107` 新窗口练习
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


wd = webdriver.Chrome()
wd.get("https://kyfw.12306.cn/otn/leftTicket/init")
sleep(1)

wd.find_element(By.ID,'fromStationText').click() # 先点击一下
wd.find_element(By.ID,'fromStationText').send_keys(f'南京南\n') # 填写出发城市
wd.find_element(By.ID,'toStationText').click() # 先点击一下
wd.find_element(By.ID,'toStationText').send_keys(f'杭州东\n') # 填写到达城市

select = Select(wd.find_element(By.CSS_SELECTOR,'.pos-top select')) # 选择发车时间
select.select_by_value("06001200")

wd.find_element(By.CSS_SELECTOR,'.sear-sel-hd li:nth-child(2)').click() # 选择时间
sleep(1)

trainList = []

# 58条数据 
eles = wd.find_elements(By.XPATH,'//*[@id="queryLeftTable"]/*[@class]')
#! 最后一条数据没用 一页只有57条列车数据
eles.pop(57)
for ele in eles:
    tText = ele.find_element(By.XPATH,'./*[4]').text
    # 查看是否有座 //*[@id="queryLeftTable"]/*[@class]/*[4]
    # 有票有两种情况 有和数字
    if '有' == tText or tText.isdigit():
        trainList.append(ele.find_element(By.XPATH,'.//*[@class="train"]//a').text)
    
print(trainList)

input()