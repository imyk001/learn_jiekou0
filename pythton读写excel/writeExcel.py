#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import xlrd

from xlutils.copy import copy

#1-----读取源excel中的所有数据
rb = xlrd.open_workbook('F:\接口学习\pythton读写excel\data.xls')

#2-----复制读取的源excel对象
wb = copy(rb)

#3----通过get_sheet()获取复制对象的sheet页
ws = wb.get_sheet(2)

#4----对sheet页进行写入（传入X和Y的坐标，和具体写入的value）
self.ws.write(id,2,real)
self.ws.write(id,2,status)

#5----保存excel（具体的excel路径+名称）
self.wb.save(self.excel_dir+'\\'+'data.xls')

