from lib.webui import *


# 全局初始化
def suite_setup():
    INFO('UI_010X suite_setup')
    mgr_login()  # 登陆


# 全局清除
def suite_teardown():
    INFO('UI_010X suite_teardown')


class UI_0101:

    def setup(self):
        pass

    def teststeps(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        #! 测试没问题后记得改
        wd = GSTORE['wd']
        eles = wd.find_elements(
            By.CSS_SELECTOR, ".sidebar-menu > li")[1:4]  # 第一个不是 拿3个
        INFO(f'前三项的分别是')
        for ele in eles:
            INFO(f'{ele}')


class UI_0102:

    def setup(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        wd = GSTORE['wd']
        # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留
        wd.refresh()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        delete_items('南京中医院1')  # 删除客户

    def teststeps(self):
        list1 = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501']]

        wd = GSTORE['wd']
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()
        sleep(1)

        insert_data(list1)


class UI_0103:

    def setup(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        wd = GSTORE['wd']
        # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留
        wd.refresh()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        delete_items('南京省中医院1')  # 删除客户

    def teststeps(self):
        list1 = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501']]

        wd = GSTORE['wd']
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()
        sleep(1)

        insert_data(list1)

        #点击编辑
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item label').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item .form-control').clear() # 清除输入框已有的字符串
        # 修改名称
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item .form-control').send_keys('南京省中医院1')
        wd.find_element(By.CSS_SELECTOR,'.content .search-result-item label').click()


class UI_0105:

    def setup(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        wd = GSTORE['wd']
        # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留
        wd.refresh()
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]').click()
        delete_items('青霉素盒装1')  # 删除客户

    def teststeps(self):
        list1  = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装']]

        wd = GSTORE['wd']
        wd.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR, '.add-one-area > button').click()

        insert_data(list1)


# * 这题退出登陆了 记得登陆回去
class UI_0106:

    def setup(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        mgr_login()

    def teststeps(self):
        wd = GSTORE['wd']
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
        sleep(1)
        # 点击右上角 管理员
        wd.find_element(By.CSS_SELECTOR, '.dropdown.user > a').click()
        sleep(1)
        wd.find_element(By.CSS_SELECTOR, '.pull-right > a').click()


# * 这题无需删除 因为 108 会做
class UI_0107:

    def setup(self):
        pass

    def teardown(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teststeps(self):
        wd = GSTORE['wd']
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
        insert_data(medeList)

        wd.find_element(By.CSS_SELECTOR,
                        'a[href="#/customers"]').click()  # 按下客户按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增客户按钮
        insert_data(clientList)

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

    # 清除用例7的手尾
    def setup(self):
        self.clear_order()
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留

    def teardown(self):
        wd = GSTORE['wd']
        wd.refresh() # 重新进入该页面 因为现在刚刚完成新增 页面元素有残留
        self.clear_order()

    def teststeps(self):
        wd = GSTORE['wd']
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
        insert_data(medeList)

        wd.find_element(By.CSS_SELECTOR,
                        'a[href="#/customers"]').click()  # 按下客户按钮
        wd.find_element(By.CSS_SELECTOR,
                        '.add-one-area .btn').click()  # 按下新增客户按钮
        insert_data(clientList)

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

    # 用例8会清除两次 所以写一个函数搞定
    def clear_order(self):
        wd = GSTORE['wd']
        wd.find_element(By.XPATH, '//*[@href="#/orders"]').click()  # 按下订单按钮
        delete_items("青霉素盒装 南京中医院")  # 删除订单

        wd.find_element(By.XPATH, '//*[@href="#/medicines"]').click()  # 按下药品按钮
        delete_items("青霉素盒装")

        wd.find_element(By.XPATH, '//*[@href="#/customers"]').click()  # 按下客户按钮
        delete_items('南京中医院')  # 删除客户
        sleep(1)
