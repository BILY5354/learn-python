# 正则表达式 老师代码
import os
import re
biliVideoNo = 'av74106411'
addNo = 3
pattern = biliVideoNo + '\/\?p=(\d+)'
targetDir = r'day16/prac_re'


# 自定义修改规则函数
def my_replace(match):
    sourceStr = match.group(0)
    pageNo = match.group(1)
    parts = sourceStr.split('=')
    targetStr = f'{parts[0]}={int(pageNo)+addNo}'
    
    print(f'{sourceStr} 改为 {targetStr}')

    return targetStr


# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        if not fn.endswith('.md'):
            continue

        fpath = os.path.join(dirpath, fn)
        with open(fpath, encoding='utf8') as f:
            content = f.read()

        if biliVideoNo not in content:
            content
        print(fpath)

        # content 是一个 md 文件的全部内容
        # 执行完 sub 后，指定的字符会被替换 
        # 该替换 是不需要 for 循环的 而是直接将匹配的字符全部替换
        # pattern 是匹配字符 my_repalce 是修改后的字符
        # 即在 content 中所有的pattern 被 my_replace 替换
        newContent = re.sub(pattern, my_replace, content)

        if newContent != content:
            with open(fpath, 'w', encoding="utf8") as f:
                f.write(newContent)
