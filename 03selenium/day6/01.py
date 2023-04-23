# frame `UI-0107` 新窗口练习
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

medeList = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
            ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
            ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']]

clientList = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
              ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
              ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']]

wd = webdriver.Chrome()
wd.get("http://127.0.0.1/mgr/sign.html")

ele = wd.find_element(By.CSS_SELECTOR, 'input[id="username"]').send_keys('byhy')
ele = wd.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('88888888')

wd.find_element(By.CSS_SELECTOR,
                'button[class="btn btn-primary btn-block btn-flat"]').click()
sleep(1)

# 创建药品或客户
def insertData(tList):
    for j in range(0,3):
        eles = wd.find_elements(By.CSS_SELECTOR,'div[style="margin-top: 1em;"] > :nth-child(1)')
        for i in range(0,len(eles)):
            eles[i].send_keys(f'{tList[j][i]}')
        wd.find_element(By.CSS_SELECTOR,'div[class="col-lg-12 col-md-12 col-sm-12"] > :nth-child(1)').click()
        sleep(1)

# 按下药品按钮
wd.find_element(By.CSS_SELECTOR,'i[class="fa fa-plus"]').click()
# 按下新增药品按钮
wd.find_element(By.CSS_SELECTOR,'button[class="btn btn-green btn-outlined btn-md"]').click()
insertData(medeList)

# 按下客户按钮 
wd.find_element(By.CSS_SELECTOR,'a[href="#/customers"]').click()
# 按下新增客户按钮 
wd.find_element(By.CSS_SELECTOR,'button[class="btn btn-green btn-outlined btn-md"').click()
insertData(clientList)

# 按下订单
wd.find_element(By.CSS_SELECTOR,'a[href="#/orders"]').click()
# 按下新建订单
wd.find_element(By.CSS_SELECTOR,'button[class="btn btn-green btn-outlined btn-md"]').click()

# 订单名字 
wd.find_element(By.CSS_SELECTOR,'div[class="col-lg-8 col-md-8 col-sm-8"] input:nth-child(1)').send_keys("ui107订单")

select = Select(wd.find_element(By.CSS_SELECTOR,'div[class="col-lg-8 col-md-8 col-sm-8"] > div:nth-child(2) > select'))
select.select_by_visible_text("南京中医院2")
select = Select(wd.find_element(By.CSS_SELECTOR,'div[class="col-lg-8 col-md-8 col-sm-8"] > div:nth-child(3) > select'))
select.select_by_visible_text("青霉素盒装1")
sleep(1)
# 数量 
wd.find_element(By.CSS_SELECTOR,'div[style="margin-top: 0.2em;"] input').send_keys("100")
# 按钮 
wd.find_element(By.CSS_SELECTOR,'div[class="col-lg-12 col-md-12 col-sm-12"] > :nth-child(1)').click()
input()


""" for i in range(0,len(medeList)):
    print(f'{medeList[i]}')
    if (i+1)%3==0:
        print("\n") """