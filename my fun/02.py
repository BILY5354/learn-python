# 读取文件夹下的所有文件名并输出到excel中
from openpyxl import Workbook
import os
path = "C:/Users/home/Desktop/劳动教育实践报告"
outwb = Workbook()
outws = outwb.worksheets[0]


outws.append(['姓名',"学号"]) # 先添加家一行表头

namesList = os.listdir(path)  # 获取文件夹下所有文件名
for userInf in namesList:
    userInf = userInf.replace("劳动教育实践报告.docx", "")  # 将多余删去
    userInf = userInf.replace("劳动教育实践报告.doc", "")  # 将多余删去
    aList = []
    tList = userInf.split('3', 1)  # 以学号首位3做分割 并只做一次分割
    # print(tList)

    for item in tList:
        if (item.isdigit()):  # 如果是数字重新加回被删除的3
            item = '3'+item
            # print(item)
        aList.append(item)
    outws.append(aList)
    # print(aList)


outwb.save(r'test.xlsx')
print("数据存入excel成功")
