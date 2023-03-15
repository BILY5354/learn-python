# f = open('day5/tmp.txt')
f = open('D:/03CodeSpace23/learn-python\day5/tmp.txt') #* 绝对路径也是反斜杠
#!相对路径错误写法： f = open('tmp.txt')
linelist = f.readlines() 
f.close()  
for line in linelist:
    print(line)