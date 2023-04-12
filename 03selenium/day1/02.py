# 选择元素的基本方法补充练习
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/jsweather.html')

# 因为有 dl 元素有很多 所以需要限制范围
forecastBox = wd.find_element(By.CLASS_NAME, 'forecastBox')

# 限制范围为 forecastBox 内部
cityList = forecastBox.find_elements(By.TAG_NAME, 'dt')
weatherList = forecastBox.find_elements(By.TAG_NAME, 'dd')


cityWeatherDict = {}
if len(cityList) == len(weatherList):  # 如果两者数量相同则加图字典
    i = 0
    for i in range(len(cityList)):
        cityWeatherDict[cityList[i].text] = int(
            weatherList[i].text[:2])  # ! 记得加 text

print(cityWeatherDict)



city = list(cityWeatherDict.keys())[0]
min = list(cityWeatherDict.values())[0]
# city = cityWeatherDict[cityWeatherDict.keys()[0]] #! 写法错误 keys() 返回的是一个 dict_keys 对象
for t, v in cityWeatherDict.items():
    if v < min:
        min = v
        city = t

print(f'最低温度的城市为{city}，温度为{min}')

input("")
