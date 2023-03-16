# 用户输入章节课后练习

salaryTotal = int(input("请输入总收入："))
salaryWang = int(input("请输入会记小王薪资："))
salaryEat = int(input("请输入餐饮费："))
salaryCar = int(input("请输入交通费："))
earn = (salaryTotal-salaryWang-salaryEat-salaryCar)*0.8
print(f"公司本月利润为：{earn}")