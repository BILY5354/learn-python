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
- 课后练习 `day2/01.py` `UI-0102`
- 课后练习 `day2/02.py` `UI-0103`
- [补充练习](http://v3.byhy.net/prac/pri546/selenium/0010a1/) `day2/03.py` 在qq音乐中找出对应列表
  - 很多时候标签是重复的，怎么办，**限制范围**
    - `t = webdriver.Chrome().find_element(By.什么什么)`
    - `要找的东西 = t.find_element(By.什么什么)`
    - 获取页面上显示内容 <a>显示内容</a> 用 `text` 方法
      - 但很多时候是这样 <a title='想获取内容'>显示内容</a> 想拿 `title` 怎么办
      - 用 `get_attribute` `get_attribute("title")`