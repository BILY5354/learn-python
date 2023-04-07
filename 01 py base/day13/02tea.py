# 老师代码
import os
import sys
import time
from subprocess import Popen, PIPE

# 应用程序的地址
notepadexepath = r'C:\Program Files\Notepad++\notepad++.exe'

# 直接用 cmd 打开命令
cmd = f'{notepadexepath}'

# 注意，不能用os.system 因为 我们的程序不能等notepad++退出
p = Popen(args=cmd, shell=True)

time.sleep(1)

# 返回的是 Popen 实例对象
p = Popen(
    'tasklist',
    stdin=None,
    stdout=PIPE,
    stderr=None,
    shell=True
)

# communicate 方法返回 输出信息
outinfo, errinfo = p.communicate()

# 注意返回的内容是bytes 不是 str ，
# 我的是中文windows，所以用gbk解码
outinfo = outinfo.decode('gbk')
# print (outinfo)


# 在输出中，寻找 notepad++ 的 进程ID
pid = None
proclist = outinfo.splitlines()
for pinfo in proclist:
    if 'notepad++.exe' in pinfo:
        print(pinfo)

        #* 只要有空格就切 两个连续空格变1个 三个连续空格变2个
        infolist = pinfo.split(' ')
        print(infolist)

        # 去掉其中的空字符串元素 列表推导式 不需要加冒号
        infolist = [info for info in infolist if info]
        print(infolist)

        # 去掉其中的空字符串元素
        pid = infolist[1]
        print(f'notepad++的进程号是{pid}')
        break

if pid is None:
    print("没有发现notepad++的进程id")
    sys.exit(2)

# 杀掉进程
os.system(f'taskkill /PID {pid} /F')