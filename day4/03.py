# 10 循环 题目2

ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''


def getNameList(ageTableStr):
    tmp = ageTableStr.splitlines()

    # 去掉空格
    ageTableList = []
    for name in tmp:
        name = name.strip()
        if name == '':
            continue

        ageTableList.append(name)

    return ageTableList


g30 = []  # 大于30岁人员列表
l30 = []  # 小于30岁人员列表
nAList = getNameList(ageTable)
for oneman in nAList:
    name, age = oneman.split(',') #* 可以用两个元素来接收分割开的字符
    if int(age) >= 30:
        g30.append(name)
    else:
        l30.append(name)

print('大于等于30岁的人有：')
for man in g30:
    print(man)


print('\n小于30岁的人有：')
for man in l30:
    print(man)