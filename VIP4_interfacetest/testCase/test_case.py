#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
# 1-导入目标模块和包
import unittest
from common.readExcel import *
from common.configHttp import *
from ddt import ddt,unpack,data
from common.wrieteExcel import *
"""
6-将接口执行状态写入excel
"""
# 2 - 调用readExcel模块，获取测试数据
data1 = getExcelData()
test_data = data1.assmbleData()
print('test_data的值',test_data)

#实例化configHttp
result = configHttp()

#实例化writeExcel
we = writeExcel()
@ddt
class testCase(unittest.TestCase):

    @ddt
    @data(*test_data)
    @unpack
    def test_request(self,id,url,name,method,param,expect):
        global status
        print(id,url,name,method,param,expect)
        #处理数据格式param和expect
        param = param[0]
        expect =expect[0]
        # 3-根据测试数据调用请求方法
        if method == 'get' or method =='GET':
            #请求get方法
            #4-获取实际结果
            recv_data = result.get(url,param)
            # 5 - 将实际结果和预期结果进行比对
            #使用try--except接收异常，来判断断言是否成功
            try:
                self.assertEqual(str(recv_data),str(expect))
                status = 'success'
            except AssertionError as msg:
                print(msg)
                status = 'fail'
            #将接口执行状态写入Excel
            real = recv_data
            we.write(int(id),int(real),status)

        elif method == 'post'or method =='POST':
            #请求post方法
            #4-获取实际结果
            recv_data = result.post(url,param)
            #5-将实际结果和预期结果进行比对
            #使用try--except接收异常，来判断断言是否成功
            try:
                self.assertEqual(str(recv_data),str(expect))
                status = 'success'
            except AssertionError as msg:
                print(msg)
                status = 'fail'
            # 将接口执行状态写入Excel
            real = recv_data
            we.write(int(id),int(real),status)
if __name__ == '__main__':
    unittest.main()















