# 课内练习

wendu=float(input("请输入今天气温（单位 摄氏度）:"))
qiya=float(input("请输入今天气压（单位 帕）:"))

if(wendu>30 or wendu<-8 or qiya>300 or qiya<20):
    print("不舒适")
elif((wendu>25 and wendu<= 30)and(qiya>200 and qiya<=300)):
    print("比较舒适")
elif((wendu>10 and wendu<= 25)and(qiya>100 and qiya<=200)):
    print("特别舒适")
elif((wendu>=-8 and wendu<= 10)and(qiya>20 and qiya<=100)):
    print("比较舒适")
else:
    print("本程序不能判断")
