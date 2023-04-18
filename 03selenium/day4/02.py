# css 下篇 课外作业 保存股票前十页
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = webdriver.Chrome()

wd.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")
sleep(2)

eles = wd.find_elements(By.CSS_SELECTOR, "tbody > tr")

# 写入字符
total = "第一页：\n"

# * 读取的是10页
# ele 是每一行
for ele in eles:
    # tes 是每一行中的没一列
    tes = ele.find_elements(By.CSS_SELECTOR, "tbody >  tr > td")
    for te in tes:
        if te.get_attribute("class") == " listview-col-add":
            # 最后了可以跳出
            break
        else:
            total = total + te.text + " "
    total = total + "\n"
    print(total)

# 第二次到第十次
for page in range(2, 11):
    total = total + f"第{page}页\n"
    # 下一页按钮
    wd.find_element(By.CSS_SELECTOR, 'a[class="next paginate_button"]').click()
    sleep(5)
    eles = wd.find_elements(By.CSS_SELECTOR, "tbody > tr")
    # ele 是每一行
    for ele in eles:
        # tes 是每一行中的没一列
        tes = ele.find_elements(By.CSS_SELECTOR, "tbody >  tr > td")
        for te in tes:
            if te.get_attribute("class") == " listview-col-add":
                # 最后了可以跳出
                break
            else:
                total = total + te.text + " "
        total = total + "\n"

        print(total)

with open("03selenium/day4/02text.txt", 'w', encoding="utf8") as f:
    f.write(total)