# 操控元素的基本方法 补充练习
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
# qq音乐网址
wd.get("https://y.qq.com/n/ryqq/toplist/27")

# 限制范围寻找元素
songListItem = wd.find_element(By.CLASS_NAME, 'songlist__list')
songList = songListItem.find_elements(By.CLASS_NAME,'songlist__cover')
# print(songList.get_attribute("title"))
artistList = songListItem.find_elements(By.CLASS_NAME,'playlist__author')


for i in range(0,len(songList)):
    print(f'{songList[i].get_attribute("title")} : {artistList[i].text}')

input()