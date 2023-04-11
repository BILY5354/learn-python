fileName = input("请输入新文件的名称")

resultStr = ""
with open("day6/gbk编码.txt", encoding="gbk") as f:
    lineList1 = f.readlines()
    for line1 in lineList1:
        # resultStr = resultStr.join(line1)  # !错误代码
        resultStr = resultStr+line1+" "


with open("day6/utf8编码.txt", encoding="utf8") as f:
    lineList2 = f.readlines()
    for line2 in lineList2:
        # resultStr = resultStr.join(line2)  # !错误代码
        resultStr = resultStr+line2+" "
print(resultStr)

print(type(resultStr))

fileName=fileName+'.txt'
fp = open(fileName, 'wb+')  # * w方式打开 如果不存在则创建
fp.write(str(resultStr).encode('utf8'))
fp.close()
