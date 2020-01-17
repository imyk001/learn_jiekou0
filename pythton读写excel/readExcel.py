#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import xlrd
#1------打开excel文件
readbook = xlrd.open_workbook(r'F:\接口学习\pythton读写excel\data.xls')
#2----获取读入文件的sheet
sheet = readbook.sheet_by_index(0)#索引的方式，从0开始
sheet1 = readbook.sheet_by_name('urlSheet')#通过名字定位sheet页
allsheetnames = readbook.sheet_names()#返回所有的sheet页名字组成的列表
print(sheet,sheet1,allsheetnames)

#3-----获取sheet最大的行数和列数
nrows = sheet.nrows #行
ncols = sheet.ncols #列
print(nrows,ncols)

#4-----获取某个单元格的值
lng = sheet.cell(0,0).value #获取1行1列的表格值，从0开始计数
lat = sheet.cell(1,2).value #获取2行3列的表格值，从0开始计数
print(lng,lat)

#5-----获取某行/某列的值
row_value = sheet.row_values(x) #获取x行的值，从0开始计数
col_value = sheet.col_values(y) #获取y列的值，从0开始计数


