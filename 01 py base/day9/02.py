# 喂动物吃东西 http://v3.byhy.net/prac/pri546/py/018a0y/
from random import randrange
from datetime import datetime

animalsDict = {}  # 字典内容{房间号 : 动物}


class tiger:
    typeA = '老虎'
    weight = 200  # 老虎的初始体重
    diet = 'meat'

    def __init__(self):
        self.nowWeight = 200  # 每只老虎自己的体重

    def bark(self):
        print("Wow !!")
        self.nowWeight -= 5

    def changeweight(self, value):
        self.nowWeight += value


class sheep:
    typeA = '绵羊'
    weight = 100  # 绵羊的初始体重
    diet = 'grass'

    def __init__(self):
        self.nowWeight = 100  # 每只绵羊自己的体重

    def bark(self):
        print("mie~~")
        self.nowWeight -= 5

    def changeweight(self, value):
        self.nowWeight += value


# 生成老虎或绵羊
def generateAnimals():
    global animalsDict
    for j in range(1, 11):
        i = randrange(1, 100)
        if i % 2 == 0:  # 偶数老虎
            tT = tiger()
            animalsDict[len(animalsDict)+1] = tT
        elif i % 2 == 1:  # 奇数绵羊
            tS = sheep()
            animalsDict[len(animalsDict)+1] = tS


# todo 投喂函数 animal 为 animalsDict[房间号（整形）]
def feed(animal):
    food = input("本次喂的食物为（meat或grass）")
    if food == animal.diet:
        animal.changeweight(10)
    elif food != animal.diet:
        animal.changeweight(-10)
    else:
        print("你代码写错了")


generateAnimals()
for k, v in animalsDict.items():
    print(f'第{k}个房间的动物是{v.typeA}，其体重是{v.nowWeight}')

roomNu = int(input("本次投喂的房间是"))
option = int(input("需要敲门吗\n1.需要2.直接投喂"))
if option == 1:
    animalsDict[roomNu].bark()
elif option == 2:
    pass
feed(animalsDict[roomNu])
startDate = datetime.now().time()  # 返回例子： 17:00:43.207608 需要切
startTime = str(startDate).split(':')  # startTime[0]为时 [1]为分 [2]为秒
while True:
    nowDate = str(datetime.now().time()).split(':')
    if int(nowDate[1]) - int(startTime[1]) >= 1:
        print("1分钟到退出程序")
        break
    else:
        roomNu = int(input("本次投喂的房间是"))
        option = int(input("需要敲门吗\n1.需要2.直接投喂"))
        if option == 1:
            animalsDict[roomNu].bark()
        elif option == 2:
            pass    
        feed(animalsDict[roomNu])

for k, v in animalsDict.items():
    print(f'第{k}个房间的动物是{v.typeA}，其体重是{v.nowWeight}')
