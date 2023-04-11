# 将0013_a1.txt 中年龄段大于50岁的找出来

f = open('day5/0013_a1.txt', encoding='utf-8')
userList = f.readlines()
f.close()
""" for line in linelist:
    print(line) """

nList = []
for user in userList:
    if user != "\n":
        nList.append(user)

# print(nList)

nL1 = []
for u in nList:
    u = u.replace("\n", "")
    nL1.append(u)

# print(nL1)

nList = []
for u2 in nL1:
    name, age = u2.split(":")
    name = name.strip()
    age = age.strip()

    if int(age) > 50:
        print(name+age)
        nList.append(name)

print(nList)
