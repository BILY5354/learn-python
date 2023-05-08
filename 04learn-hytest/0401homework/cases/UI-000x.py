from lib.webui import *
from time import sleep


# * 自动化测试 UI-0001到UI-0005
class UI_000x:

    #! 无 setup 在 __st__.py 已经定义
    # def setup(self):
    #     open_browser() # 打开浏览器

    #* 定义
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

    def teststeps(self):
        wd = GSTORE['wd']

        wd.get('http://127.0.0.1/mgr/sign.html')

        #todo 分别对应 ddt_cases 中 para 中3个元素的列表 info 是错误信息
        username, password, info = self.para

        # 如果 username 不为空 便送过去
        if username is not None:
            wd.find_element_by_id('username').send_keys(username)

        if password is not None:
            wd.find_element_by_id('password').send_keys(password)

        wd.find_element_by_tag_name('button').click()

        sleep(2)

        notify = wd.switch_to.alert.text

        CHECK_POINT('弹出提示', notify == info)

        wd.switch_to.alert.accept()

    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element_by_id('username').clear()
        wd.find_element_by_id('password').clear()