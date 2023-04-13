# 操控元素的基本方法 补充练习
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
# qq音乐网址
wd.get("https://y.qq.com/n/ryqq/toplist/27")

# 限制范围寻找元素
songListItem = wd.find_element(By.CLASS_NAME, 'songlist__list')
songInfoList = songListItem.find_elements(
    By.TAG_NAME, 'li')

print(len(songInfoList))

#! 注意是找上升的歌
for i in range(0, len(songInfoList)):
    t = songInfoList[i].find_element(By.CLASS_NAME, "songlist__rank").find_element(By.TAG_NAME,"i").get_attribute("class")
    if t == "icon_rank_up":
        print(f'{songInfoList[i].find_element(By.CLASS_NAME,"songlist__cover").get_attribute("title")} : {songInfoList[i].find_element(By.CLASS_NAME,"playlist__author").text}')


input()
