# 目录
## 选择元素的基本方法练习
- 课后练习 `day1/01.py` 完成UI-0001 输入密码并登陆
   -  找 button 可以用 `wd.find_element(By.CSS_SELECTOR,'button[type=submit]')`
- 补充练习 `day1/02.py` 查询天气网站
  - 找一个控件用 `find_element` 找一堆用 `find_elements`
  - 三种方式找控件
    - 用 id `By.ID`
    - 用 class `By.CLASS_NAME`
    - 用 tag `By.TAG_NAME`