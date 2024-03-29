# 用框架完成自动化测试

## 文件目录
- `cases` 文件夹：
  - **所有测试用例必须放在根目录下的** `cases` **目录下**
    - 用 `hytest --new autotest` `autotest` 会包含 `cases` 
    - 所以 `autotest` 创建的是一个项目目录
  - 每个 `cases` 是包含许多套件的文件夹 每一个套件下又可以包含许多用例 `class UI_0101:`
  - `__st__.py` 目录文件初始化
    - 比如 大家都有的步骤 打开网页
    - 关闭 `webdriver` 
- `lib` 文件夹：
  - `webui.py` 将共通的操作放在里面
    - 打开网页，登陆

## 用例内的函数说明
- `STEP` 函数
  - 用来声明每个测试步骤，这样日志报告更清晰
- `INFO` 函数
  - 用来打印一些信息在日志和报告中，方便出现问题时定位。
- `CHECK_POINT` 函数
- 用来声明测试过程中的每个检查点，*任何一个检查点不通过，整个测试用例就被认为不通过*

## 过程记录
- 每次执行一个用例完成后 执行一次 `webdriver.Chrome().refresh()` 会避免很多麻烦
  - 因为这样会重新进入首页 就像是第一次进入首页一样 不会有上一次操作留下的干扰

### 数据驱动
- 数据驱动 创建 `ddt_cases`
### 初始化 清除 共享 数据
- 遵循：**谁做的初始化 操作对环境产生了 什么改变 谁 就应该在 清除 操作里面做什么样的 还原**
- 规则：
  - 单个用例 *在该用例对应的类中*
    - `setup` 初始化 
      - 如果 setup 执行失败（有异常）， 就不会再执行 `teststeps` 和 `teardown` 
    - `teststeps` 用例内容
      - 如果 `teststeps` 执行失败， 仍然会执行 `teardown` 确保环境被清除
    - `teardown` 清除
  - 单个文件 在该文件中添加全局函数  `suite_setup` `suite_teardown`
  - 整个目录 在该目录下添加文件 `__st__.py`
    - 然后执行 `suite_setup` `suite_teardown`
- `setup` `teststeps` `teardown` 放在 `__st__.py` *是不起初始化作用的*
  

## hytest 操作
- debug： 右键点击一个用例的 `name`
  - 或者 右键点击 一个文件
  - 或者 右键点击 一个文件夹
- 快速添加初始化：直接在文件中右键 选择对应操作
