wz = "https://www.bilibili.com/video/av74106411/?p"

with open("day6/prac_filerw.txt", encoding="utf8") as f:
    lines = f.readlines()   # 按一行一行读


val = int(input("你想加入的数是"))
# val = 3 测试用
nText = ''

for line in lines:  # line 为读到的每一行
    nuStr = ''  # 用作存粗数字
    if wz in line:  # 如果有网址 则处理 + val
        slitWz = line.split('?p=')    # 将 wz 分成 内容1 与 （数字（要处理的部分） 内容2）
        for tt in slitWz[1]:    # slitWz[1] 即 数字 内容2 slitWz[0] 即 内容1
            if tt.isdigit():
                nuStr = nuStr+tt
            else:  # 如果不是数字了 跳出循环
                break

        slitWz2 = slitWz[1].split(nuStr, 1)  # 将 数字（要处理的部分） 内容2 分割 且只分割一次
        nNu = str(int(nuStr)+val)  # 将数字内容加上
        nWz = slitWz[0] + '?p=' + nNu + slitWz2[1]  # 内容1 + ?p= + 新数字 + 内容2
        print(nWz)
        nText = nText + nWz

    else:   # 没有网址 直接塞入大字符串
        nText = nText + line

# print(nText)
with open("day6/prac_filerw.txt", "w", encoding="utf8") as f:
    f.write(nText)
