keyword = 'https://www.bilibili.com/video/av74106411/?p='

inputnum = 3

with open('day6/prac_filerw.txt', encoding='utf8') as f:
    lines = f.readlines()

print(lines)

# 新文件的内容
newContent = ''

#* 老师代码的思想是准确计算出数字在字符串中的下标进行准确定位 然后加上inputnum
for line in lines:
    pos1 = line.find(keyword)   # 找到 h开头的下标 
    # 没有包含关键字
    if pos1 < 0:
        newContent += line
    else:
        # 计算出数字部分的起止 下标
        startPos = pos1+len(keyword)
        endPos = startPos

        while True:     # 一直找到数字结束
            endPos += 1
            if not line[startPos:endPos].isdigit():
                break

        # endPos 已经到了非数字的地方 所以回退一个字符位置
        endPos -= 1
        num = int(line[startPos:endPos])+inputnum #* 注意 startPos endPos 不是 line 字符串的下标 只是用来切割数字的索引
        newContent += line[:startPos]+str(num)+line[endPos:]

print(newContent)
