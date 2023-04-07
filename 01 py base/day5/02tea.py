# 因为文件是utf8编码
with open('day5/0013_a1.txt', encoding='utf-8') as f:
    lines = f.read().splitlines()

oldPeople = []
for line in lines:
    # 去掉行中的空格
    line = line.replace(' ', '')

    # 如果是空行 跳过
    if not line:
        continue

    name, age = line.split(':')
    if int(age) > 50:
        oldPeople.append(name)

oldPeople=','.join(oldPeople)
appendText=f'\n\n大于50岁的人有：{oldPeople}'
print(appendText)