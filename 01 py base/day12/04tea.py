import os

targetDir = r'E:\learn-python\learn-python\day12\prac_re'

keyword = 'https://www.bilibili.com/video/av74106411/?p='

# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        if not fn.endswith('.md'):
            continue

        fpath = os.path.join(dirpath, fn)

        with open(fpath, encoding='utf8') as f:
            lines = f.readlines()

        # 新文件的内容
        newContent = ''
        isChanged = False
        # 一行行分析
        for line in lines:
            # pos1 是网址首位的下标
            pos1 = line.find(keyword)
            # 没有包含关键字
            if pos1 < 0:
                newContent += line
            else:
                isChanged = True
                # 计算出数字部分的起止 下标 
                startPos = pos1 + len(keyword)
                # 先让 尾标与首标一致 再慢慢移
                endPos = startPos
                while True:
                    # 尾标先加1 不是数字的话退出 后面再减去1
                    endPos += 1
                    if not line[startPos:endPos].isdigit():
                        break

                num = int(line[startPos:endPos-1]) + 3

                # 注意现在尾标还是向前了一位 记得减1
                newContent += line[:startPos] + str(num) + line[endPos-1:]

        # 判断文件是否改变
        if isChanged:
            print(f"{fpath} 改变")
            with open(fpath, "w", encoding='utf8') as f:
                f.write(newContent)
        else:
            print(f"{fpath} 没有改变")