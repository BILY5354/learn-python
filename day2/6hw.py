def askInfo(i):
    hei = int(input("请输入学员"+str(i)+"身高"))
    wei = int(input("请输入学员"+str(i)+"体重"))
    return [hei,wei]

sumHei=0
sumWei=0
val=[0,0]
for n in range(3):
    val=askInfo(n)
    sumHei+=val[0]
    sumWei+=val[1]
print("平均身高是："+str(sumHei/3))
print("\n平均体重是："+str(sumWei/3))
