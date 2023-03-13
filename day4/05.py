# 10 字符串格式化

salaryTxt = '''
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
'''


def getList(salartStr):
    tmp = salartStr.splitlines()

    # 去除空格
    tList = []
    for t in tmp:
        t = t.strip()
        if t == '':
            continue
        tList.append(t)

    return tList


salartList = getList(salaryTxt)

for user in salartList:  # * 注意 user 已经是一个字符串 可以用str方法
    tname, tsalary = user.split(';')
    t1, name = tname.split(':')  # t1 是没用的 再切一次
    t2, salary = tsalary.split(':')  # 再切一次
    name = name.strip()
    salary = salary.strip()
    tax = int(salary)*0.1
    income = int(salary)-int(salary)*0.1
    print(f'name: {name:<6};{"salary":>10}:{salary:>10} ;{"tax:":>6}{tax:6.0f} ; {"income:":>6}{income:8.0f}') #* f外面用了' 里面就需要"
