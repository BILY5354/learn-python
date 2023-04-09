# 正则表达式课后作业
import requests,os
import re as RegularExp 
url = "http://www.listeningexpress.com/studioclassroom/ad/"


res = requests.get(url)
content = res.text


# 正则表达式 sc-ad [\d-]+ [aA-zZ ]+.mp3
# 也可以 (.*?\.mp3) 用组
downList = []
for one in RegularExp.findall(r'sc-ad [\d-]+ [aA-zZ ]+.mp3', content):
   if url+one in downList:
       continue
   downList.append(url+one)

# 定义 wget 位置
wgetpath = r'E:\01codeenvirment\wget\wget.exe'
print(downList)

#* 网址有空格 一定要加上双引号
for d in downList:
    # print(f'{wgetpath} "{d}" -P E:\learn-python\learn-python\day16')
    os.system(f'{wgetpath} "{d}" -P E:\learn-python\learn-python\day16')