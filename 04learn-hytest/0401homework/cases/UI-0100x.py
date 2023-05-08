from lib.webui import *


# 全局初始化
def suite_setup():
    INFO('suite_setup')
    mgr_login()  # 登陆


# 全局清除
def suite_teardown():
    INFO('suite_teardown')
    wd = GSTORE['wd']
    wd.quit()


class UI_0101:

    def setup(self):
        pass

    def teardown(self):
        #! 测试没问题后记得改
        # wd = GSTORE['wd']
        wd = webdriver.Chrome()
        eles = wd.find_elements(
            By.CSS_SELECTOR, ".sidebar-menu > li")[1:4]  # 第一个不是 拿3个
        INFO(f'前三项的分别是')
        for ele in eles:
            INFO(f'{ele}')

    def teststeps(self):
        pass


class UI_0102:

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        list1 = ['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装']
        
        wd = webdriver.Chrome()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()
        sleep(2)

        insertData(list1)


class UI_0103:

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        list1 = ['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装']
        
        wd = webdriver.Chrome()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()
        sleep(2)

        insertData(list1)

        #点击编辑
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item label').click()
        # 修改名称 
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item .form-control').send_keys('南京省中医院1')
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item label').click()


class UI_0105:

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        wd = webdriver.Chrome()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()

        # * 用css 下篇的内容找元素
        sleep(2)
        eles = wd.find_elements(
            By.CSS_SELECTOR, ".col-lg-8  input:nth-child(1)")
        eles[0].send_keys('新的药')
        sleep(2)
        eles[1].send_keys('新的编号')
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()


# * 这题退出登陆了 记得登陆回去
class UI_0106:

    def setup(self):
        pass

    def teardown(self):
        mgr_login()

    def teststeps(self):
        wd = webdriver.Chrome()
        # 保存旧窗口句柄
        oldWin = wd.current_window_handle

        wd.find_element(By.CSS_SELECTOR, '.pull-right.hidden-xs > a').click()
        sleep(2)

        for handle in wd.window_handles:
            # 先切换到该窗口
            wd.switch_to.window(handle)
            # 判断是否是需要操作的窗口
            if '白月黑羽' in wd.title:
                # 使窗口最大化
                wd.maximize_window()
                eles = wd.find_elements(
                    By.CSS_SELECTOR, 'ul[class="navbar-nav d-md-inline-flex"] > li')
                for ele in eles:
                    print(ele.find_element(By.CSS_SELECTOR, 'span').text)
                break

        # 切换会一开始的窗口
        wd.switch_to.window(oldWin)
        sleep(2)
        # 点击右上角 管理员
        wd.find_element(By.CSS_SELECTOR, '.dropdown.user > a').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.pull-right > a').click()
        wd.quit()


# * 这题无需删除 因为 108 会做
class UI_0107:

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        wd = webdriver.Chrome()
        medeList = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
                    ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
                    ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']]

        clientList = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
                      ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
                      ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']]

        wd.find_element(By.CSS_SELECTOR,
                        'i[class="fa fa-plus"]').click()  # 按下药品按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增药品按钮
        insertData(medeList)

        wd.find_element(By.CSS_SELECTOR,
                        'a[href="#/customers"]').click()  # 按下客户按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增客户按钮
        insertData(clientList)

        wd.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]').click()  # 按下订单
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新建订单

        # 订单名字
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area  .form-control').send_keys("ui107订单")

        # 两个 select
        selectEles = wd.find_elements(By.CSS_SELECTOR, ".add-one-area select")
        # 客户
        Select(selectEles[0]).select_by_visible_text("南京中医院2")
        Select(selectEles[1]).select_by_visible_text("青霉素盒装1")

        sleep(1)
        # 数量
        wd.find_element(By.CSS_SELECTOR,
                        'input[type="number"]').send_keys("100")
        # 按钮
        wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()


class UI_0108:

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        wd = webdriver.Chrome()
        medeList = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
                    ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
                    ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']]

        clientList = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
                      ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
                      ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']]

       

        wd.find_element(By.XPATH, '//*[@href="#/orders"]').click()  # 按下订单按钮
        deleteItems("青霉素盒装 南京中医院")  # 删除订单

        wd.find_element(By.XPATH, '//*[@href="#/medicines"]').click()  # 按下药品按钮
        deleteItems("青霉素盒装")

        wd.find_element(By.XPATH, '//*[@href="#/customers"]').click()  # 按下客户按钮
        deleteItems('南京中医院')  # 删除客户
        sleep(1)

        wd.find_element(By.CSS_SELECTOR,
                        'i[class="fa fa-plus"]').click()  # 按下药品按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增药品按钮
        insertData(medeList)

        wd.find_element(By.CSS_SELECTOR,
                        'a[href="#/customers"]').click()  # 按下客户按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增客户按钮
        insertData(clientList)

        wd.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]').click()  # 按下订单
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新建订单

        # 订单名字
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area  .form-control').send_keys("ui107订单")

        # 两个 select
        selectEles = wd.find_elements(By.CSS_SELECTOR, ".add-one-area select")
        # 客户
        Select(selectEles[0]).select_by_visible_text("南京中医院2")
        Select(selectEles[1]).select_by_visible_text("青霉素盒装1")

        sleep(1)
        # 数量
        wd.find_element(By.CSS_SELECTOR,
                        'input[type="number"]').send_keys("100")
        # 按钮
        wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()
