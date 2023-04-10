# 装饰器代码
import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper(*args,**kargs):
        curTime = func(*args,**kargs)
        return f'当地时间： {curTime}'
    return wrapper

def getXXXTimeFormat1(name):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} '


def getXXXTimeFormat2(name,place):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} , 采集地：{place}'


# 装饰 
# getXXXTime = sayLocal(getXXXTime)

print(getXXXTimeFormat1('aaa'))
print(getXXXTimeFormat2('aaa',place='bbb'))