# 熟悉线程
print("main thread")

from threading import Thread
from time import sleep

# 定义一个函数 作为新线程执行的入口函数
def threadFunc(arg1,arg2):
    print('sub thread start')
    print(f'the arg of sub thread: {arg1}, {arg2}')
    sleep(5)
    print("sub thread finish")

thread = Thread(
    target=threadFunc,args=("参数1","参数2")
)

thread.start()

thread.join()
print('main thread finish')