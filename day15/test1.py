# 正则表达式尝试获取文本薪资信息

textPath = "day15/jobinfo.txt"

with open(textPath, "r", encoding="utf8") as f:
    lineList = f.readlines()

for line in lineList:
    tt = line.split("上海-")[1] # tt是 -？？区？万 这部分的内容 
    # 这么做是防止 前面有python区分工程师\

    s1=tt.find("区")
    s2=tt.find("万")
    print(tt[s1+1:s2])
