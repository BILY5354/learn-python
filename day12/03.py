# 统计参数中重复的数字
# !有bug
""" def equals(*numbers):
    tNus = list(numbers)
    for nu in tNus:
        i=0
        #! 在遍历的过程中 是不能删除或添加元素 否则导致遍历混乱
        while(nu in tNus):
            tNus.remove(nu)
            i+=1
        print(f'{nu}出现的次数为{i}次')

equals(3, 4, 3, 4, 1, 6, 2)  """


def equals(*numbers):
    tDict = {}
    for nu in numbers:
        if nu not in tDict:
            tDict[nu] = 1
        else: # 如果存在
            tDict[nu] += 1
    
    # 显示函数
    for t,v in tDict.items():
        print(f'数字 {t} 出现了 {v} 次')

equals(3, 4, 3, 4, 1, 6, 2)
