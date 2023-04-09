# 文件课后作业 遍历目录中所有文件
# 1. 找出所有文件目录
# 2. 逐个遍历文件找出内容
# 3. 写会原文件
import os

# 目标目录
targetDir = r'E:\learn-python\learn-python\day12\prac_re'

fpathList = []

# 下面的三个变量 dirpath, dirnames, filenames   
# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名

# 得到某个目录下所有文件的全路径
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        # 把 dirpath 和 每个文件名拼接起来 就是全路径
        fpath = os.path.join(dirpath, fn)
        fpathList.append(fpath)

for fpath in fpathList:
    linesList = []
    with open(fpath, encoding="utf8") as f:
        linesList = f.readlines()

    updateText = ''
    for line in linesList:
        # 找到目标 替换塞入
        nuStr = ''
        if "https://www.bilibili.com/video/av74106411/?p" in line:
            slitWz = line.split('?p=',1)
            for tt in slitWz[1]:  # 数字肯定在 ?p= 后面第一位
                if tt.isdigit():
                    nuStr = nuStr+tt  # 数字字符串拼接
                else:  # 没有数字 不需要再拼接了
                    break
                nNuStr = str(int(nuStr)+3)  # 题目要求加3
            
            # 执行完 for 才放
            updateText = updateText + slitWz[0] + "?p=" + nNuStr
        # 没有 直接塞入
        else:
            updateText = updateText + line

    with open(fpath, "w", encoding="utf8") as f:
        f.write(updateText)