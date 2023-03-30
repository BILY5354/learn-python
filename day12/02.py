# 读取可能包含不是utf字符的文件

# * 既然文件包含不同字符 那么就用二进制方式读
with open('day12/0019.txt', "rb") as f:
    bytesLines = f.read().splitlines()  # 以换行符作切割

lineIdx = 1
for bytesLine in bytesLines:
    try:
        toStr = bytesLine.decode("utf8")
        print(f'第{lineIdx:04}行，有{len(toStr)}个字符')
    except UnicodeDecodeError:
        print(f'第{lineIdx:04}行，有非UTF8编码字符！！！')

    lineIdx += 1
