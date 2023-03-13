# 10 循环 列出质数

i = 0
j = 0
for i in range(2, 1000):
    for j in range(2, i):
        if (i % j == 0):
            break
    if j == i:
        print(j)
