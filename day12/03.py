# 统计参数中重复的数字

def equals(*numbers):
    tNus = list(numbers)
    for nu in tNus:
        i=0
        while(nu in tNus):
            tNus.remove(nu)
            i+=1
        print(f'{nu}出现的次数为{i}次')

equals(3, 4, 3, 4, 1, 6, 2) 