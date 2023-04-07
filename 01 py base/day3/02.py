# 判断语句 题目1

height=float(input("请输入你的身高(单位米):"))
weight=float(input("请输入你的体重(单位公斤):"))
age=int(input("请输入你的年龄:"))

if(age<10):
    print("10岁以下儿童不参与健康评估")
elif(age>=10 and age<60):
    if(weight/(height**2)>24):
        print("超重")
    elif(weight/(height**2)<18):
        print("超轻")
    else:
        print("正常")
elif(age>=60):
    print("60岁以上老人不参与健康评估")