# 调用其它程序例程

#! 该代码需在管理员权限

from subprocess import PIPE, Popen

# 返回的是 Popen 实例对象

proc = Popen(
    'fsutil volume diskfree c:',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True)

outinfo, errinfo = proc.communicate()

outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')
print(outinfo)
print('----------')
print(errinfo)

outputList = outinfo.splitlines()

# 剩余量
free = int(outputList[0].split(':')
           [1].replace(',', '').split('(')[0].strip())

# 总空间
total = int(outputList[1].split(':')
            [1].replace(',', '').split('(')[0].strip())

if (free/total < 0.1):
    print('!！剩余空间告急！！')
else:
    print('剩余空间足够')
