# 字典课后作业1

# * 读取全部的数据
with open('day8/2019-10-22_11.05.40.log', encoding="utf8") as f:
    linesList = f.readlines()


# * 主要函数
total = {}  # 键为 API list_order >?s 值为 个数
for line in linesList:
    line = line.replace("\n", "")  # 去掉 \n
    lineList = line.split("|")

    if "API list_order >" in lineList[1]: # lineList[1]例子 API list_order >1s
        if lineList[1] not in total:
            total[lineList[1]] = 1    # 首次
        elif lineList[1] in total:
            total[lineList[1]] = int(total[lineList[1]])+1
    elif lineList[2]=="响应超时":
        if "响应超时" not in total: # 首次
            total[lineList[2]] = 1
        elif "响应超时" in total:
            total[lineList[2]] = int(total[lineList[2]])+1

for k,v in total.items():
    print(f'{k} : {v}')

""" lineList = line.split('|')
print(lineList) """
