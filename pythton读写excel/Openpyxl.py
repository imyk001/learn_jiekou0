#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
xlrd和xlwt处理的是xls文件，单个sheet最大行数是65535，
如果有更大需要的，建议使用openpyxl函数，最大行数达到1048576
如果数据量超过65535就会遇到：ValueError: row index was 65536, not allowed by .xls format
"""
import openpyxl


# def readExcel(self):
filename = r'F:\接口学习\pythton读写excel\data.xls'
inwb = openpyxl.load_workbook(filename)  # 读文件
print(inwb)
sheetname = inwb.get_sheet_names()  # 获取所有sheet
print(sheetname)
ws = inwb.get_sheet_by_name(sheetname[0])  # 获取第一个sheet内容
print(ws)
    # 获取sheet的最大行数和列数
    # rows =
    # cols =
    # for r in range(1,rows):
    #     for c in range(1,cols):
    #         print(ws.cell(r,c).value)
    #     if r ==10:
    #         break
