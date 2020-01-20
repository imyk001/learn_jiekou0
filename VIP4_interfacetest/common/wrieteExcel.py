#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
2--打开目标excel
3--确定需要写入的数据
4--保存
"""
# 1--导入包
import xlrd,xlwt
from xlutils.copy import copy

class writeExcel(object):
    def __init__(self):
        print('将实际结果与执行状态写入excel')
        try:
            #打开excel
            mybook = xlrd.open_workbook(r'../testData/data.xls')
            #复制目标对象
            self.wb = copy(mybook)
            #获取目标sheet页
            self.ws = self.wb.get_sheet(2)
        except FileNotFoundError as msg:
            print(msg)
    def write(self,id,real,status):
        #写入目标单元格（此处我们写入data.xls中的第三个sheet页中的第三列-real和第四列-status）
        #此处的id代表行，id为1代表第一行，2代表列，代表第二列
        self.ws.write(id,2,real)
        self.ws.write(id,3,status)
        #保存
        self.wb.save(r'../testData/data.xls')

