# py练习 调用其他程序 打开notepad++并kill掉这个进程

import os
from time import sleep

#* 加上 r 表示无需转义 \ 就是 \ 不然需要用 \\
os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
sleep(10)
os.system("Taskkill /PID 6732 /F")