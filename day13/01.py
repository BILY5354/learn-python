# 线程进程课后作业 py程序

from threading import Thread, Lock
import os

# 定义 wget 位置
wgetpath = r'E:\01codeenvirment\wget\wget.exe'


def downloadTask(url):
    # -P 参数 指定下载存放目录
    os.system(f'{wgetpath} {url} -P F:\\9999else')

# 循环让用户输入下载任务
while True:
    url = input('请输入下载网址：')

    # 返回的是删除空格后的字符串副本 
    if url.strip()=='':
        continue # 如果为空则跳过

    # 创建一个新线程 执行下载操作
    thread = Thread(target=downloadTask, args=(url,))

    thread.start()