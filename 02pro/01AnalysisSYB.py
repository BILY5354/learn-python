# 分析事业编

from openpyxl import load_workbook

wb = load_workbook(filename = "02pro/4138028.xlsx") # 获取表格文件对象

sheet_ranges = wb['岗位表1']
print(sheet_ranges['考区'].value)
