# 课后作业 老师代码
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cdn2.byhy.net/files/selenium/jsweather.html')

ele = driver.find_element(By.ID, "forecastID")
print(ele.text)

citysWeather = ele.text.split('°C\n')

lowest = None  # 记录目前最低温 先设置为 None
lowestCitys = []  # 温度最低城市列表
for one in citysWeather:
    one = one.replace("℃/", "")
    print(one)
    parts = one.split('\n')
    curcity = parts[0]

    # 找出 列表中的两个最小值
    loweather = min([int(one) for one in parts[1].split('/')])

    # 还没有最低温记录 或者发现气温更低的城市
    # 注意条件不能写反
    if lowest == None or loweather < lowest:
        lowest = loweather
        lowestCity = [curcity] # 新建一个列表
    # 温度和当前最低相同 加入列表
    elif loweather == lowest:
        lowestCity.append(curcity)

print("温度最低为%s,城市有%s" %(lowest,''.join(lowestCity)))