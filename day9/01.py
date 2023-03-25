# 自定义类课后作业
from random import randrange

# todo 假定现在怪物定死
enemies = []  # 森林中7个敌人列表
coins = 1000  # 总共金币数
forestNu = 1  # 第几座森林
# * 列表有两个 一个专门存弓箭 一个专门存斧头 且还有一个全局军队的数量
armyArcher = {}  # 玩家军队 字典 {名字:hp值}
armyAxeman = {}
armyTotalNu = 0  # 用于玩家军队数量

""" #! 测试用数据
armyArcher = {'佩里骑士': 100, '青蛙王子': 100}
armyAxeman = {'瓦德里屠夫': 10}
armyTotalNu = 3 """


# 自定义类 弓箭手
class Archer:
    # typeC = '弓箭手' #!感觉没用
    price = 100
    maxHp = 100

    def __init__(self, nickName):
        self.nickName = nickName
        self.hp = 100  # 血量初始值


# 自定义类 斧头帮
class Axeman:
    # typeC = '斧头帮'
    price = 120
    maxHp = 120

    def __init__(self, nickName):
        self.nickName = nickName
        self.hp = 120  # 血量初始值


# 生成敌人函数
def generateEnemies():
    global enemies
    for j in range(1, 8):
        i = randrange(1, 100)
        if i % 2 == 0:  # 偶数狼妖
            enemies.append('狼妖')
        elif i % 2 == 1:  # 奇数鹰妖
            enemies.append('鹰妖')
    print(f'敌人配置如下：\n{enemies}')


# 购买函数
def papment():
    # !记得 py 中全局变量用法 先声明 再使用 只需定义一次
    global armyTotalNu, coins, armyArcher, armyAxeman
    while True:
        print(
            f'现有金币{coins}，弓兵100，斧兵120\n现有弓兵{len(armyArcher)}名，斧兵{len(armyAxeman)}名\n1.购买弓兵\n2.购买斧兵\n0.退出购买进入森林')
        i = int(input("你的选择是"))
        if i == 0:  # 退出
            break
        elif i == 1:  # 买弓兵
            # * 价格判断 没钱下次循环
            if coins - Archer.price >= 0:
                name1 = input("该弓兵名字是")
                while True:  # * 判断是否有重名
                    if name1 not in armyArcher and name1 not in armyAxeman:
                        break
                    else:
                        name1 = input("存在重名，请重新输入")
                tArcher = Archer(name1)
                armyArcher[tArcher.nickName] = tArcher.hp

                coins -= tArcher.price  # 减去价格
                armyTotalNu += 1  # 玩家军队数量总数+1
            else:
                print("金币不够 请重新选择")
                continue
        elif i == 2:  # 买斧兵
            if coins - Axeman.price >= 0:
                name2 = input("该斧兵名字是")
                while True:  # * 判断是否有重名
                    if name2 not in armyArcher and name2 not in armyAxeman:
                        break
                    else:
                        name2 = input("存在重名，请重新输入")
                tAxeman = Axeman(name2)
                armyAxeman[tAxeman.nickName] = tAxeman.hp

                coins -= tAxeman.price  # 减去价格
                armyTotalNu += 1  # 玩家军队数量总数+1
            else:
                print("金币不够 请重新选择")
                continue
        elif i == 4:  # * 测试用 看字典情况
            print(armyArcher)
            print(armyAxeman)
            print(f"现在总数为{armyTotalNu}\n")


# 战斗与恢复函数：血够就能打死怪物 不够下一个 怪物是无血的
def battle(enemy):
    global forestNu, armyArcher, armyAxeman, armyTotalNu
    print(f'进入第{forestNu}座森林，现队伍情况如下\n弓兵：{armyArcher}\n斧兵：{armyAxeman}')
    name = input("选择派出（打出名字）：")
    if name in armyArcher:  # 弓箭兵战斗判断
        if enemy == '鹰妖':
            armyArcher[name] = armyArcher[name] - 20
        elif enemy == '狼妖':
            armyArcher[name] = armyArcher[name] - 80

        # 打完了 判断血够不够
        if armyArcher[name] > 0:
            print(f'挑战第{forestNu}座森林成功')
            forestNu += 1  # 去下一座森林
            return True
        else:  # 没有血了
            print(f'挑战第{forestNu}座森林失败，请重来')
            del armyArcher[name]
            armyTotalNu -= 1  # 队伍总人数减1
            return False
    elif name in armyAxeman:
        if enemy == '鹰妖':  # 斧头兵战斗判断
            armyAxeman[name] = armyAxeman[name] - 80
        elif enemy == '狼妖':
            armyAxeman[name] = armyAxeman[name] - 20

        # 打完了 判断血够不够
        if armyAxeman[name] > 0:
            print(f'挑战第{forestNu}座森林成功')
            forestNu += 1  # 去下一座森林
            return True
        else:  # 没有血了
            print(f'挑战第{forestNu}座森林失败，请重来')
            del armyAxeman[name]
            armyTotalNu -= 1  # 队伍总人数减1
            return False
    else:
        print("没有此角色请重新输入")
        battle(enemy)  # 重新进入


# 恢复函数
def recover():
    global coins, armyArcher, armyAxeman

    print(f'剩余金币{coins}，队伍情况：弓兵：{armyArcher}，斧兵：{armyAxeman}')
    while True:
        i = int(input("1.选择治疗\n0.进入下一森林"))
        if i == 0:
            break
        elif i == 1:
            name = input("选择治疗的名字为\n")
            if name in armyArcher:
                pay = int(input("你要花费的金额是"))
                if armyArcher[name]+pay > Archer.maxHp:
                    print("输入的数值大于上限 重来")
                    continue
                elif coins < pay:
                    print("金币不足 重来")
                    continue
                elif armyArcher[name]+pay <= Archer.maxHp and coins > pay:  # 不能超过最大hp值
                    coins = coins-pay
                    armyArcher[name] = armyArcher[name] + pay
            elif name in armyAxeman:
                pay = int(input("你要花费的金额是"))
                if armyAxeman[name]+pay > Axeman.maxHp:
                    print("输入的数值大于上限 重来")
                    continue
                elif coins < pay:
                    print("金币不足 重来")
                    continue
                elif armyAxeman[name]+pay <= Axeman.maxHp and coins > pay:
                    coins = coins-pay
                    armyAxeman[name] = armyAxeman[name] + pay
            else:
                print("查无此人 重来")
                continue
        else:
            print("重新输入")


# * 主函数
generateEnemies()
papment()
while True:
    if armyTotalNu == 0: # ∵有可能出现没买任何队员情况
        print(f'游戏失败！全员阵亡')
        break
    tag = battle(enemies[forestNu-1])  # 敌人列表不用删除 直接用全局变量 森林序号
    if forestNu == 8:
        print(f'恭喜！通过森林，剩余金币{coins}')
        break
    if tag == True:  # 如果返回真 则打怪成功 可以补血
        recover()

    # print(f'{armyArcher}\n{armyAxeman}')
