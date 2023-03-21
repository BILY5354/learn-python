# 字典课后练习1

with open("day8/0016_1.txt", encoding="utf8") as f:
    lineList = f.readlines()

people = {}
for line in lineList:
    
    if line =='\n': # 如果是空行则跳过
        continue
    tInfo = line.split(" ") # 根据空格切割每一行
    print(tInfo)    
    for t in tInfo: # ex. ['薛蟠', '', '', '', '', '4560', '42\n'] 然后找出用户积分
        if t.isdigit(): # 第一个纯数字便为用户积分
            if line[0] not in people: # 如果字典没有这个 键 则加入
                people[line[0]] = t
                break   # 可以跳出了 
            else:
                # 如果字典有这个键 则将其相加
                people[line[0]] = str(int(people[line[0]])+int(t)) # people[line[0]]姓所对应的键
                break

for surname, score in people.items():
    print(f'{surname} : {score}')