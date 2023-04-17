# 用 css 选择器在招聘网站上获取信息
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 先输入 python 与 选择 杭州
# 使用 css 选择器

wd = webdriver.Chrome()

wd.get("https://www.51job.com/")

# 输入文本框 一定要看浏览器是否有是该元素
eleInput = wd.find_element(
    By.CSS_SELECTOR, 'p[class="ipt"]>input[id="kwdselectid"]')
# 清空原有的
eleInput.clear()
eleInput.send_keys('python')


# 地区选择框
#! 先点击此框 然后选择城市
wd.find_element(
    By.CSS_SELECTOR, '[id="work_position_click"]').click()

# 最近网站更新了，好像前端处理有滞后，需要sleep 一下
time.sleep(2)

cityList = wd.find_elements(By.CSS_SELECTOR, 'em[id*="work_position_click_center_right"]')
# cityList = wd.find_elements(By.CSS_SELECTOR, '#work_position_click_center_right em')


for city in cityList:
    cityName = city.text
    selected = city.get_attribute('class')

    # * 这里 selected 会显示 js_more 也就是 父的class名
    # print(f'{cityName} \t {selected}')

    if cityName == '杭州':
        if selected != 'on':
            city.click()
    else:
        if selected == 'on':  # 避免漏网之鱼
            city.click()

# 确定城市按钮
wd.find_element(By.CSS_SELECTOR,
                '[id=work_position_click_bottom_save]').click()



# 按钮
eleBut = wd.find_element(
    By.CSS_SELECTOR, """button[onclick="kwdGoSearch($('#kwdselectid').val());"]""").click()

time.sleep(2)

# 岗位名字
jobList = wd.find_elements(
    By.CSS_SELECTOR, 'span[data-v-4f9a87fb][class="jname at"]')
# 发布日期
dateList = wd.find_elements(
    By.CSS_SELECTOR, 'span[data-v-4f9a87fb][class="time"]')
# 薪资
salaryList = wd.find_elements(
    By.CSS_SELECTOR, 'span[data-v-4f9a87fb][class="sal"]')
# 公司名字
companyList = wd.find_elements(
    By.CSS_SELECTOR, 'a[data-v-4f9a87fb][class="cname at"]')



for i in range(0,len(jobList)):
    print(f'{jobList[i].text} | {dateList[i].text} | {salaryList[i].text} | {companyList[i].text}')

input()
