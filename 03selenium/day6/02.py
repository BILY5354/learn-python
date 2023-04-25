from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

medeList = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
            ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
            ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']]

clientList = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
              ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
              ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']]

# 用 xpath选择器
wd = webdriver.Chrome()
wd.get("http://127.0.0.1/mgr/sign.html")
ele = wd.find_element(By.ID, 'username').send_keys('byhy')
ele = wd.find_element(By.ID, 'password').send_keys('88888888')

wd.find_element(By.XPATH, '//button').click()
sleep(1)


def deleteItems(name):
    # 判断 是否还有元素 有的话一直删删删
    while wd.find_elements(By.CSS_SELECTOR, '.content .search-result-item'):
        results = wd.find_elements(
            By.CSS_SELECTOR, '.content .search-result-item')

        for res in results:
            # res 是每一个框
            eles = res.find_elements(
                By.CSS_SELECTOR, '.search-result-item-field')

            eleStr = ""
            # 将 每一个框里的文字遍历 添加到字符串中 再根据是否包含来删除
            for ele in eles:
                eleStr += ele.text

            # * 两种情况 name 包含空格即删除订单 不包含即删除药品或客户
            if " " in name:
                if name.split(" ")[0] in eleStr and name.split(" ")[1] in eleStr:
                    #! 订单只有一个按钮即删除 所以下标为0
                    wd.find_elements(
                        By.CSS_SELECTOR, '.content .btn-xs')[0].click()
                    wd.switch_to.alert.accept()  # 点击确认按钮
                    sleep(1)
                    continue  # 继续下一个框
            else:
                if name in eleStr:
                    # 如果存在该名字 则删除 并跳出循环 删除为第二个
                    wd.find_elements(
                        By.CSS_SELECTOR, '.content .btn-xs')[1].click()
                    wd.switch_to.alert.accept()  # 点击确认按钮
                    sleep(1)
                    continue  # 继续下一个框

        # 找不到 name 跳出循环
        break


wd.find_element(By.XPATH, '//*[@href="#/orders"]').click()  # 按下订单按钮
deleteItems("青霉素盒装 南京中医院") # 删除订单

wd.find_element(By.XPATH, '//*[@href="#/medicines"]').click()  # 按下药品按钮
deleteItems("青霉素盒装")

wd.find_element(By.XPATH, '//*[@href="#/customers"]').click()  # 按下客户按钮
deleteItems('南京中医院')  # 删除客户

sleep(1)

#* ui107的代码直接复制
# 创建药品或客户
def insertData(tList):
    for j in range(0, 3):
        # input
        eles = wd.find_elements(By.CSS_SELECTOR, '.add-one-area .form-control')
        for i in range(0, len(eles)):
            eles[i].send_keys(f'{tList[j][i]}')
        # * 不需要唯一 此处的选择器能找到两个元素
        wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()
        sleep(1)

wd.find_element(By.CSS_SELECTOR, 'i[class="fa fa-plus"]').click()  # 按下药品按钮
wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn').click()  # 按下新增药品按钮
insertData(medeList)

wd.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]').click()  # 按下客户按钮
wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn').click()  # 按下新增客户按钮
insertData(clientList)

wd.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]').click()  # 按下订单
wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn').click()  # 按下新建订单

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
wd.find_element(By.CSS_SELECTOR, 'input[type="number"]').send_keys("100")
# 按钮
wd.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()

input()