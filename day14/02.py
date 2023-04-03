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


# todo theadidx 线程序号  task 下载任务的网址 getText 下载后的字典
def downloadwz(theadidx, task,getText):
    
    res = requests.get(task)
    getText[task] = res.text


    fileLock.acquire()  # 获取锁
    with open(txtpath, 'a+', encoding="utf8") as f:
        f.write(getText[task])
        f.write("\n")
    fileLock.release()


theadlist = []
getText = {}  # 键是下载的链接 值是返回的数据
for idx in range(len(taskList)):  # 循环次数是 tasklist的长度
    thread = Thread(target=downloadwz, args=(idx, taskList[idx], getText))
    thread.start()
    theadlist.append(thread)  # 加入线程列表 后面按顺序停止

for thread in theadlist:
    thread.join()

print("all task finish")
