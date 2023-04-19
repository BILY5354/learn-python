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
## css表达式-上篇
- 课后练习 `day3/02.py` `UI-0103`
- [补充练习](http://v3.byhy.net/prac/pri546/selenium/0032f3/) `day3/01.py`
  - 在招聘网站上获取对应的职位信息 用`CSS Selector`
    - **找元素的关键是**选择一个唯一能表示这个空间的方式，可用开发者模式中的判断是否选中
    - 如果`CSS Selector`选择元素没有效果，可用*debug*方式查看
## css表达式-下篇
- 课后练习 `day4/01.py` `UI-0105`
  - 完成登陆后会出现代码执行得比服务器响应快的情况，这时候会出现找元素找不到的情况，两种解决方式
    - 用 `sleep` `time.sleep(10)`
    - 用 `implicitly_wait` `webdriver.Chrome().implicitly_wait(10)`
    - 用 `.` **是不能找多个class的** 比如 `<div class="a b c">`
      - 这里有三个类名，不同类间用空格隔开
      - 错误例子的css选择器： `."a b c"` 是不能找到的，正确只能找一个 `.a`
      - **不要过分纠结 找不到就换一种思路 实现就好** 当有多个 class 名时：
        - 用点法 `.a.b`
        - 直接复制法： `[class=""]`
- [补充练习-股票网站](http://quote.eastmoney.com/center/gridlist.html#hs_a_board)
  - 获取前10页的股票 名称和代码，并且保存到文件中 `day4/02.py`
## frame
- 课后练习 `day5/01.py` `UI-0106`
  - 完成：跳转新页面
    - 窗口最大化 `webdriver.Chrome().maximize_window()`
- [补充练习-股票网站](http://quote.eastmoney.com/center/gridlist.html#hs_a_board)
  - 获取前 10条的股票 名称和代码 `day5/02.py`
    点开10个股票公司的 数据 链接 获取公司简介相关信息 以csv格式存储在文件中
  - 当需要获取一个表格内的多种元素的 *显示在屏幕上的值* 时 **可用列表推导式**
  - 想要将列表中的元素拼接成一个大的字符串可以使用 `join()` 
    - **注意 使用方式： 字符串.join([列表])** 
## 选择框
- 课后练习 `day？？？/01.py` `UI-0107`
  - 完成：添加3中药品 3个客户及相关操作