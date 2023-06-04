from time import sleep
from lib.webui import *


# 套件初始化，只执行一次
def suite_setup():
    pass


# 套件清除，只执行一次
def suite_teardown():
    pass


# * 自动化测试 UI-0001到UI-0005
class UI_0001:

    # name = "UI_0001"

    # * 定义
    ddt_cases = [
        {
            'name': '登录 UI_0001',
            'para': [None, '88888888', '请输入用户名']
        },
        {
            'name': '登录 UI_0002',
            'para': ['byhy', None, '请输入密码']
        },
        {
            'name': '登录 UI_0003',
            'para': ['byh', '88888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录 UI_0004',
            'para': ['byhy', '888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录 UI_0005',
            'para': ['byhy', '8888888888', '登录失败 : 用户名或者密码错误']
        },
    ]

    def setup(self):
        print("UI_0001 setup")

    def teardown(self):
        print("UI_0001 teardown")

    def teststeps(self):
        print(f'UI_0001{GSTORE["wd"]}')
        wd = GSTORE['wd']
        wd.get('http://127.0.0.1/mgr/sign.html')

        # todo 分别对应 ddt_cases 中 para 中3个元素的列表 info 是错误信息
        username, password, info = self.para

        # 如果 username 不为空 便送过去
        if username is not None:
            wd.find_element(By.ID, 'username').send_keys(username)

        if password is not None:
            wd.find_element(By.ID, 'password').send_keys(password)

        wd.find_element(By.TAG_NAME, 'button').click()

        sleep(1)

        notify = wd.switch_to.alert.text

        CHECK_POINT('弹出提示', notify == info)

        wd.switch_to.alert.accept()
