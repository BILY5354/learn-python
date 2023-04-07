#tList = [["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]]
tList = [["布", "石头"], ["石头", "剪刀"], ["石头", "剪刀"]]

def gameRes(gy, zf):  # 关羽 张飞
    if gy == zf:  # 平局
        return 0
    elif gy == "布":
        if zf == "剪刀":
            return -1
        else:
            return 1
    elif gy == "石头":
        if zf == "剪刀":
            return 1
        else:
            return -1
    elif gy == "剪刀":
        if zf == "布":
            return 1
        else:
            return -1


result = 0  # 如果为1 说明关羽赢 -1 张飞赢
# 想列表去掉外面的括号 拿里面的内容 可通过for循环
for huihe in tList:
    # print(type(n))
    result += gameRes(huihe[0], huihe[1])

if result>0:
    print(f"关羽3局赢了{result}局，平手{3-result}，关羽胜出")
elif result<0:
    print(f"张飞3局赢了{-result}局，平手{3-(-result)}，张飞胜出")
elif result==0:
    print("三局平好耶")
else:
    print("你确定？")
