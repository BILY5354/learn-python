# py基础 *课后作业记录*
- 有补充字样代表补充练习
## 1.安装与运行
- [课后练习](http://v3.byhy.net/prac/pub/py/0001/)
## 2.对象及数字对象
- [课后练习](http://v3.byhy.net/prac/pub/py/0002/)
## 3.变量 和 注释
- [课后练习](http://v3.byhy.net/prac/pub/py/0003/)
## 4.字符串
- [课后练习](http://v3.byhy.net/prac/pub/py/0004/)
## 5.初学函数
- [课后练习](http://v3.byhy.net/prac/pub/py/0005/)
## 6.让用户输入信息
- [课后练习](http://v3.byhy.net/prac/pub/py/0006/)
- [补充练习](http://v3.byhy.net/prac/pri546/py/002a01/)
## 7.列表、元组
- [课后练习](http://v3.byhy.net/prac/pub/py/0007/)
- [补充练习](http://v3.byhy.net/prac/pri546/py/002c21/)
## 8.判断语句
- [课后练习](http://v3.byhy.net/prac/pub/py/0008/)
## 9.对象的方法
- [课后练习]()
- [补充练习](http://v3.byhy.net/prac/pri546/py/004a2d/)
  - [答案](http://v3.byhy.net/prac/pri546/py/ref/_0006e/)
## 10.格式化字符串
## 11.循环
## 12.字符编码
## 13.文件读写
## 14.模块和库
## 15.使用IDE
## 16.调试程序
## 17.字典
## 18.自定义类
## 19.异常
## 20.再学函数
## 通过搜索解决问题

- [课后练习]()
- [补充练习]()

# py高级 *课后作业记录*
## 21.文件和目录操作
- 文件目录课后练习 `day12/04.py`
  - 遍历文件夹下所有的目录与文件
  - 需要遍历目录下的所有文件 用 `walk`
  - `walk` 返回的是列表对象 可以通过 `+` 完成两个列表的合并  实现目录的拼接
## 22.日期和时间
## 23.调用其他程序
- [课后练习](http://v3.byhy.net/prac/pub/py/1001/)
  - 找到notepad++进程并杀死它 `day13/02tea.py`
- [补充练习](http://v3.byhy.net/prac/pri546/py/051a00/)
## 24.多线程 和 多进程
- Python练习：多线程 `day13/01.py`
## 25.JSON
## 26.正则表达式
- 正则表达式练习 `day16/01.py`
  - 进入网站解析音频地址（用正则解）并用wget下载到本地
  - 网址有空格 在os.system("{变量}")中 变量需要加上双引号
  - 正则表达式 匹配了一大串 很可能是因为 **贪婪模式** 
- 正则表达式课后练习 `day16/02.py`
  - 遍历目录下所有文件并将规定部分进行替换
  - 替换不需要用 `for` 循环一个一个匹配 而是直接使用 `sub`
  - `re.sub(pattern, my_replace, content)` 即在 content 中所有的pattern 被 my_replace 替换
## 27.读写Excel
## 28.装饰器

# 小技巧
- 字符串格式化
  - `r` 不使用转义
  - `f` 格式化 让`{变量}`
- 列表 `+` 与 `append`
  - `+` 是将两个列表合并
  - `append` 是加入 比如列表
  - 例子可以看练习 文件目录