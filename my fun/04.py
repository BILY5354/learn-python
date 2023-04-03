# 用 python 执行控制台命令并返回结果
from subprocess import PIPE, Popen

# 返回的是 Popen 实例对象
proc = Popen(
    'reg query HKEY_CURRENT_USER\Environment /v Path',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True)

# communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# 标准输出设备和 标准错误设备 当前都是本终端设备
outinfo, errinfo = proc.communicate()

print(outinfo)