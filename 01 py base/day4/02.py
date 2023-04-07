# 10 循环练习

# 题目1 找出两个字符串互不存在的人名
str1 = '''
熊宁
杰益

王伟伟

青芳

玉琴
焦候涛
莫福
杨高旺
唐欢欢
韩旭
'''

str2 = '''
焦候涛 
熊宁 
玉琴 

骆龙 

韩旭 
杨高旺

杰益  

莫福  

伟伟

李福  
'''

""" 
从str1中获取每一行：
    如果该行中包含了人名，
        到str2中查看，是否存在同样的人名
        如果str2中有该人名，记录下来
"""

# ! 错误写法
""" liststr1=str1.splitlines()
liststr2=str2.splitlines()
print(liststr2)
if '熊宁'  in liststr2: # 为什么这样判断说没有 因为在给定的字符串中 熊宁前后有可能是有空格的
    print("yes")
else:
    print("no") """

# * 一定要去除多余的内容


def getNameList(namesStr):
    tmp = namesStr.splitlines()

    # 去掉其中的空行和人名前后的空格
    names = []
    for name in tmp:
        name = name.strip()  # strip方法可以将 字符串前面和后面的空格删除
        if name == '':
            continue
        names.append(name)
    return names


names1 = getNameList(str1)
names2 = getNameList(str2)

print('str1中独有的人名是：')
for name in names1:
    if name not in names2:
        print(name)

print('str2中独有的人名是：')
for name in names2:
    if name not in names1:
        print(name)