# 正则表达式补充作业
import os
import re

# 目标目录
targetDir = r'day16/prac_re'

files = []
dirs = []
fpathList = []


for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        # 把dirpath 和 每个文件名拼接起来
        fpath = os.path.join(dirpath, fn)
        fpathList.append(fpath)


for fpath in fpathList:
    linesList = []
    with open(fpath, encoding="utf8") as f:
        linesList = f.readlines()

    updateText = ''
    for line in linesList:
        for nu in re.findall(r'.+=([\d]+)', line):
            oNu = nu
            nNu = int(nu)+3
 
        if "https://www.bilibili.com/video/av74106411/?p" in line:
            line = line.replace(str(oNu),str(nNu))
        updateText += line 

    with open(fpath, "w", encoding="utf8") as f:
        f.write(updateText)