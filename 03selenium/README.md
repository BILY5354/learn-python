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
  - 注意 想要取字典第一个元素 `list(cityWeatherDict.keys())[0]`
    - 其中 `keys` 返回的是 dict_keys 故需要强转
## 操控元素的基本方法
- 课后练习 `UI-0102`
  -  
- 课后练习 `UI-0103`