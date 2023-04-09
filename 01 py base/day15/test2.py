# 测试正则

""" content = '''苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的'''

import re
p = re.compile(r'.*.')
for one in  p.findall(content):
    print(one) """

content = '''张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901'''

import re
p = re.compile(r'^(.+)，.+(\d{11})', re.MULTILINE)
for one in  p.findall(content):
    print(one)