# 这是第七天找包的实验 设置环境变量 保证找到phone
import sys

# sys.path.append('D:/03CodeSpace23/learn-python/day7')
# set PYTHONPATH= D:/03CodeSpace23/learn-python/day7 #* 方法二

from phone.apple.iphone6 import askPrice as i6askpri
from phone.apple.iphone7 import askPrice as i7askpri
from phone.samsung.note.galaxy_note8 import askPrice as snoteaskpri
from phone.samsung.s.galaxy_s7 import askPrice as sgalaaskpri



i6askpri()
i7askpri()
snoteaskpri()
sgalaaskpri()