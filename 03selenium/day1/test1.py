from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Chrome()

# 调用 WebDriver 对象的 get 方法 让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

# 根据 ID 选择元素 返回的是该元素对应的 webWlement 对象
element = wd.find_element(By.ID,'kw')

element.send_keys('通讯\n')

input("按回车结束")  