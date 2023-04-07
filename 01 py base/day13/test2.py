# 多个线程访问共享数据

from threading import Thread, Lock
from time import sleep

bank = {
    'byhy': 0
}

bankLock = Lock()

# todo theadidx 线程编号 amount 每次增加的余额
def deposit(theadidx, amount):
    bankLock.acquire()

    balance = bank['byhy']
    sleep(0.1)
    bank['byhy'] = balance+amount
    print(f'子线程 {theadidx} 结束')

    bankLock.release()


theadlist = []
for idx in range(10):
    thread = Thread(target=deposit, args=(idx, 1))
    thread.start()
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('main thread finish')
print(f'the balance is: {bank["byhy"]}')