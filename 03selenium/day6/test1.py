# 导入 select 类
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

wd= webdriver.Chrome()

select = Select(wd.find_element(By.ID,""))

select.deselect_all()

# 选择
select.select_by_visible_text('')
select.select_by_visible_text('')