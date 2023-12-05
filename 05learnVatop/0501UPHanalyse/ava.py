import re
with open("./test.log", "r", encoding="utf8") as f:
    read_list = f.readlines()

sum = 0
count = 0
min = 1000
max = 0
for i in read_list:
    num = re.findall(r': (.*)ms', i)[0]
    sum += int(num)
    count += 1
    if min > int(num):
        min = int(num)
    if max < int(num):
        max = int(num)

print(f'总数{count}平均值{sum/count}最大值{max}最小值{min}')
