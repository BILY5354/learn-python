# 正则表达式课后作业
url = "http://www.listeningexpress.com/studioclassroom/ad/"

import os

wgetpath = r'E:\01codeenvirment\wget\wget.exe'

# os.system(f'{wgetpath} {url} -P E:\learn-python\learn-python\day16')

with open("day16/index.html",encoding="gbk") as f:
    lineList = f.readlines()

print(lineList)