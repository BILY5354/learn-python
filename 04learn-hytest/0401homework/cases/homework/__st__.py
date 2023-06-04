from lib.webui import *


# 套件初始化，只执行一次
def suite_setup():
    open_browser() # 打开浏览器

# 套件清除，只执行一次
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()
