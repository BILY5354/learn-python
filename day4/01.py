# 9 字符串格式化 课后习题

#题目1 

str1 = '大家好，我的名字叫：'
str2 = '黑羽白月'

print("%s%s"%(str1,str2)) # 注意 不像C语言有逗号的
print('{}{}'.format(str1,str2)) # 注意 format 用()
print(f'{str1}{str2}')


# 题目2
""" str1=input("输入你的名字")
str2=input("输入你的年龄")
print("你的名字是：%s，你的年龄是%s"%(str1,str2)) """

# 题目3
""" info = [
    ['user1', 345.6, 12, '黄金'],
    ['user2', 2345.6, 8, '白银'],
    ['user3555', 55345.6, 22, '钻石'],
]

for user in info:
    print("用户：%10s，积分：%10s，等级：%10s，头衔：%10s"%(user[0],user[1],user[2],user[3])) """