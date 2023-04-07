# 设置一个可以显示主菜单的程序
members = {
    1: {'name': '白月黑羽', 'level': 3, 'coins': 300},
    2: {'name': '短笛魔王', 'level': 5, 'coins': 330},
    3: {'name': '紫气一元', 'level': 6, 'coins': 340},
    4: {'name': '拜月主',   'level': 3, 'coins': 32200},
    5: {'name': '诸法空',   'level': 4, 'coins': 330},
    6: {'name': '暗光城主', 'level': 3, 'coins': 320},
    7: {'name': '心魔尊',   'level': 3, 'coins': 2300},
    8: {'name': '日月童子', 'level': 8, 'coins': 3450},
    9: {'name': '不死尸王', 'level': 3, 'coins': 324},
    10: {'name': '天池剑尊', 'level': 9, 'coins': 13100},
}


def Memu():
    print(f'1 查看用户账号信息\n2 添加用户\n3 删除用户\n4 列出所有用户信息\n0 退出')
    i = input("你的选择是")
    return i


def fun1():
    nickname = input("请输入账号名")
    for t, tt in members.items():  # t为外层字典键 tt为外层字典值 同样为字典
        if nickname == tt['name']:
            uLevel = tt['level']
            uCoins = tt['coins']
            print(f'用户ID：{nickname}，等级：{uLevel}，金币数量：{uCoins}')
        else:
            continue


def fun2():
    nickname = input("请输入添加的账号名")
    for t, tt in members.items():  # t为外层字典键 tt为外层字典值 同样为字典
        if nickname == tt['name']:
            print("存在相同用户名！")
            return False  # 如果存在相同用户名 退出重新执行
        else:
            continue  # 遍历一次 member 看是否存在同名
    nLevel = input("请输入等级")
    nCoins = input("请输入金币数量")
    dictLen = list(members)[-1]+1  # 得到最后一个键的数值
    newInfo = {'name': nickname, 'level': nLevel, 'coins': nCoins}
    members[dictLen] = newInfo


def fun3():
    nickname = input("请输入添加的账号名")
    for t, tt in members.items():  # t为外层字典键 tt为外层字典值 同样为字典
        if nickname != tt['name']:  # 与fun2 不同
            continue
        elif nickname == tt['name']:
            del members[t]
            return True
    print("改账户不存在")
    return False


def fun4():
    for mTag, mInfo in members.items():
        #* 注意用 " " ‘’表示键
        print(f'{mTag} : {mInfo["name"]}, {mInfo["level"]}, {mInfo["coins"]}')


while (1):
    i = int(Memu())
    if i == 0:
        break
    elif i == 1:
        fun1()
    elif i == 2:
        fun2()
    elif i == 3:
        fun3()
    elif i == 4:
        fun4()

""" # * 测试用数据 
i=members[1]
print(f'{i}')
t=i['name']
print(f'{t}')
print(f'{i.values()}')
tt=i.values()
print(f'{type(tt)}') """
