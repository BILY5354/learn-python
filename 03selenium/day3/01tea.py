import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#! 记得设置 等待元素出现
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.51job.com')

driver.find_element(By.ID,'kwdselectid').send_keys('python')
# 点击工作地点
driver.find_element(By.ID,'work_position_input').click()

# 需要 sleep 一下 等待页面加载完

# 选择所有城市 去掉非杭州的
cityEles = driver.find_elements(By.CSS_SELECTOR,'')

for one in cityEles:
    cityName = one.text
    selected = one.get_attribute('class')

    if cityName == '杭州':
        if selected != 'on':
            one.click()

    else:
        if selected == 'on':
            one.click()

# 保存城市选择
driver.find_element(By.ID,'').click()

# 点击搜索
driver.find_element(By.CSS_SELECTOR,'').click()

# 等待界面稳定
time.sleep(5)

# 搜索结果分析
jobs = driver.find_elements(By.CSS_SELECTOR,'')

for job in jobs:
    fileIds = job.find_elements(By.CSS_SELECTOR,'')
    strFieId = [fileId.text for fileId in fileIds]
    print(' | '.join(strFieId))

driver.quit()