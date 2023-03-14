# 10 循环 列出质数


for i in range(2, 1000):
     #* ∵py不像c的for 这里j是不可能取到i的 那么怎么判断j==i呢
     #* 将 i+1 即可
    for j in range(2, i+1): 
        if (i % j == 0):
            break
    if j == i:
        print(j)
