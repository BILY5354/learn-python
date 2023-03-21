# 打印出股票和代码

# * 准备函数将数据全部保存到字典里面
def prepare():
    t = {}
    # * 读取全部的数据
    with open('day8/stock.txt', encoding="utf8") as f:
        linesList = f.readlines()
    for line in linesList:
        line = line.replace("\n", "")  # 去掉 \n
        tList = line.split(" | ")  # 用于存在 键值对的列表 随便将空格删去
        t[tList[0]] = tList[1]  # 存入字典
    return t


def Memu():
    print(f'1 进入股票查询\n0 退出')
    i = input("你的选择是")
    return i


def fun1(total):
    # print(total['九典制药'])
    mess = input("请输入要查询的股票名称或代码\n")
    print(mess)
    # 快速判断 是否存在键
    if mess in total:
        print(f'股票名称：{mess}，股票代码：{total[mess]}')
        return  # 不需要再判断了
    # 逐一判断是都存在值
    for k, v in total.items():
        if mess == v:
            print(f'股票名称：{k}，股票代码：{v}')


total = prepare()  # 键为 股票名称  值为 代码
# print(total)
while (True):
    i = int(Memu())
    if i == 0:
        break
    elif i == 1:
        fun1(total)
