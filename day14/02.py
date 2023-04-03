# 多线程课后作业
import requests
from threading import Thread, Lock
from time import sleep

taskList = [
    'http://httpbin.org/ip',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
]

""" 
我的思路：
将这些网站准备开始线程
加锁
打开文件时候是在最后追加
"""

fileLock = Lock()  # 定义文件锁
txtpath = "day14/taskList.txt"


def downloadwz(theadidx, txtpath,task):
    fileLock.acquire()  # 获取锁

    with open(txtpath, 'a+', encoding="utf8") as f:
        # print(task)
        res = requests.get(task)
        # print(res.text)
        f.write(res.text)
        f.write("\n")

    fileLock.release()


theadlist = []
for idx in range(len(taskList)):  # 循环次数是 tasklist的长度
    thread = Thread(target=downloadwz, args=(idx, txtpath, taskList[idx]))
    thread.start()
    theadlist.append(thread)  # 加入线程列表 后面按顺序停止

for thread in theadlist:
    thread.join()

print("all task finish")
