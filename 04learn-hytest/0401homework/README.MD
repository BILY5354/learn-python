# 用框架完成自动化测试

## 文件目录
- `cases` 文件夹：
  - `__st__.py` 目录文件初始化
    - 大家都有的步骤 打开网页
    - 关闭 `webdriver` 
- `lib` 文件夹：
  - `webui.py` 将共通的操作放在里面
    - 打开网页，登陆


## 过程记录
- 数据驱动 创建 `ddt_cases`
- 初始化：
  - 单个用例 **在该用例的类中** 
    - `setup` 初始化 
    - `teardown` 清除
    - `teststeps` 用例内容
  - 单个文件 **在该文件中添加全局函数**  `suite_setup` `suite_teardown`
  - 整个目录 **在该目录下添加文件** `__st__.py`
  

## 模板
```python
class UI_01xx:

    def setup(self):
        pass

    def teardown(self):
       pass

    def teststeps(self):
       pass
```