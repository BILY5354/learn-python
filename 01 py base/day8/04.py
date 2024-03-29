# 打印出股票和代码

# * 准备函数将数据全部保存到字典里面
def prepare():
    t1 = {}  # 股票在前 代码在后
    t2 = {}  # 代码在前 股票在后
    # * 读取全部的数据
    with open('day8/stock.txt', encoding="utf8") as f:
        linesList = f.readlines()
    for line in linesList:
        line = line.replace("\n", "")  # 去掉 \n
        tList = line.split(" | ")  # 用于存在 键值对的列表 随便将空格删去
        t1[tList[0]] = tList[1]  # 存入字典
        t2[tList[1]] = tList[0]
    return t1, t2


def Memu():
    print(f'1 进入股票查询\n0 退出')
    i = input("你的选择是")
    return i


def fun1(total1, total2):
    # print(total['九典制药'])
    mess = input("请输入要查询的股票名称或代码\n")
    # print(mess)
    # 快速判断 是否存在键
    if mess in total1:
        print(f'股票名称：{mess}，股票代码：{total1[mess]}')
        return  # 不需要再判断了
    # 逐一判断是都存在值
    elif mess in total2:
        print(f'股票名称：{total2[mess]}，股票代码：{mess}')
        return  # 不需要再判断了
    else:
        print("无法判断")
        return


total1, total2 = prepare()  # 键为 股票名称  值为 代码
# print(total)
while (True):
    i = int(Memu())
    if i == 0:
        break
    elif i == 1:
        fun1(total1, total2)
