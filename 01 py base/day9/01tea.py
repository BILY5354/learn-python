from random import  randint
import time

# 鹰妖
# 属性：类型名 typename

class Eagle:
    typeName = '鹰妖'

# 狼妖
# 属性：类型名 typename
class Wolf:
    typeName = '狼妖'

# 父类：战士 
class Warrior:

    #* 父类没有 strength 没有关系 因为不会实例父类的对象
    #* 子类会直接传入这些属性
    def __init__(self,name):
        self.strength = self.maxStrength
        self.name = name

    def heal(self,stoneCount,player):
        if player.stoneNumber < stoneCount:
            print('剩余灵石不足')
            return

        self.strength += stoneCount
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength

        player.stoneNumber -= stoneCount


    def fightWithMonster(self,monster):
        #* 创建战斗规则 根据相应的字典去拿扣多少血的值
        if monster.typeName in self.fightRule:
            self.strength -= self.fightRule[monster.typeName]
        else:
            print('不支持的妖怪类型')


# 弓箭兵
# 属性：类型名 typename
#       雇佣价： 100灵石
#       最大生命值： 100
#       生命值
#        名字
#      和妖怪战斗 fightWithMonster
class Archer(Warrior):
    typeName = '弓箭兵'
    price         = 100
    maxStrength   = 100
    fightRule     = {
        '鹰妖' : 20,
        '狼妖' : 80,
    }


# 斧头兵
# 属性：类型名 typename
#     雇佣价： 120 灵石
#     最大生命值： 120
#       生命值
#        名字
#      和妖怪战斗 fightWithMonster

class Axeman(Warrior):
    typeName = '斧头兵'
    price         = 120
    maxStrength   = 120
    fightRule     = {
        '鹰妖' : 80,
        '狼妖' : 20,
    }


# 玩家
# 属性： 灵石数量

class Player:
    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber
        self.warriors = {}

    def hireOne(self, WarriorType):
        if self.stoneNumber < WarriorType.price:
            print(f'灵石不足，您只有 {player.stoneNumber} 灵石')
            return

        while True:
            name = input('请给雇佣战士起一个名字')
            name = name.strip()
            if len(name) == 0:
                print('名字无效')
                continue
            if name in self.warriors:
                print('这个名字已经被用了')
            else:
                break

        self.warriors[name] = WarriorType(name)

        self.stoneNumber -= WarriorType.price

    # 雇佣战士
    def hireWarriors(self):
        menu = '''
        请选择雇佣操作
        1 - 雇佣弓箭兵
        2 - 雇佣斧头兵
        3 - 退出 
        : '''


        while True:
            choice = input(menu)
            if choice not in ['1','2','3']:
                print('输入错误')
                continue

            if choice == '3':
                break

            # 雇佣弓箭兵
            if choice == '1':
                self.hireOne(Archer)
            # 雇佣斧头兵
            else:
                self.hireOne(Axeman)

        self.printInfo()

    def printInfo(self):
        print('\n您麾下战士情况如下')
        for name,warrior in self.warriors.items():
            print(f'{name}: {warrior.typeName} 生命值 {warrior.strength}')

        print(f'您的灵石还剩余{self.stoneNumber}')



# 森林
# 属性： 妖怪
class Forest:
    def __init__(self,monster):
        self.monster = monster


# 森林 列表
forestList = []
for i in range(7):
    if randint(0,1) == 0:
        monster = Eagle()
    else:
        monster = Wolf()

    forestList.append(Forest(monster))

print('\n前方森林里的妖怪是：')
for f in forestList:
    print(f.monster.typeName)

time.sleep(10)

print('\n'*20)


#创建玩家
player = Player(1000)

player.hireWarriors()


print('\n\n ****** 出发啦 *******')


for no,forest in enumerate(forestList):
    # 战斗
    while True:
        print(f'\n\n ### 现在到了第 {no+1} 座森林 ### ')

        while True:
            warriorName  = input('您要派出的战士是？')
            if warriorName not in player.warriors:
                print('没有这个战士')
                continue
            break

        warrior = player.warriors[warriorName]

        print(f'当前森林里面是 {forest.monster.typeName}')

        warrior.fightWithMonster(forest.monster)

        print(f'经过战斗，你的战士{warriorName}，生命值还有{warrior.strength}')

        if warrior.strength <= 0:
            print('他，光荣牺牲了')
            player.warriors.pop(warriorName)
            continue
        else:
            break

    # 疗伤处理
    while True:
        player.printInfo()

        op = input('''\n请输入疗伤战士名字和灵石数量，格式如为：姓名+20
        直接回车退出疗伤：''')

        if op == '':
            break

        name,stoneCount = op.split('+')
        stoneCount = int(stoneCount)

        player.warriors[name].heal(stoneCount,player)


player.printInfo()