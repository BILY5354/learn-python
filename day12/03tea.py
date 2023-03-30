# 统计出现的字符 tea ver

def equals(*nums):
    # 定义统计表
    stats = {}
    for num in nums:
        # 已经在统计表中
        if num in stats:
            stats[num] += 1
        # 不在统计表中
        else:
            stats[num] = 1

    for num,times in stats.items():
        print(f'数字{num}出现了{times}次')

equals(3, 4, 3, 4, 1, 6, 2) 