#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
7-return给需要数据的地方
"""
# 1-导入读取excel的包
import xlrd
class getExcelData(object):
    def __init__(self):
    # 2-打开目标文件
        readbook = xlrd.open_workbook('F:\VIP4_interfacetest\\testData\data.xls')
    #3-定位sheet页
        self.urlSheet = readbook.sheet_by_name('urlSheet')
        self.urlNum = self.urlSheet.nrows
        self.paramSheet = readbook.sheet_by_name('paramSheet')
        self.paramNum = self.paramSheet.nrows
        self.assertSheet = readbook.sheet_by_name('assertSheet')
        self.assertNum = self.assertSheet.nrows
    # 4-定位行和列（从哪一行哪一列开始读）
    # 5-读取数据
    def getSheetData(self,Num,sheetName):
        data = []
        for i in range(1,Num):
            sheetData = sheetName.row_values(i)
            data.append(sheetData)
        return data
        # urlSheetData = getSheetData(urlNum,urlSheet)
        # paramSheetData = getSheetData(paramNum,paramSheet)
        # assertSheetData = getSheetData(assertNum,assertSheet)
        # print('urlSheetData数据为：',urlSheetData)
        # print('paramSheetData数据为：',paramSheetData)
        # print('assertSheetData数据为：',assertSheetData)
    # 6-组装数据，分别取sheet页第一行数据进行组装
    def assmbleData(self):
        urlList = self.getSheetData(self.urlNum,self.urlSheet)
        paramList = self.getSheetData(self.paramNum,self.paramSheet)
        assertList = self.getSheetData(self.assertNum,self.assertSheet)
        dataList = []

        for i in range(len(urlList)):
            new_urlList = urlList[i]
            new_paramList = paramList[i][1:]
            new_assertList = assertList[i][1:]
            new_urlList.append(new_paramList)
            new_urlList.append(new_assertList)
            print('singleList',new_urlList)
            dataList.append(new_urlList)
        return dataList

if __name__ == '__main__':
    a = getExcelData()
    a.assmbleData()