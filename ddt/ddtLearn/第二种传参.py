#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import unittest
from ddt import ddt,data,unpack

#第二种传参方式
@ddt
class MyTestCase2(unittest.TestCase):
    #会依次按照执行次数传入，比如第一次执行该方法传入（1,2），第二次执行传入（2,3）
    @data((1,2),(2,3))
    @unpack#只有需要进行分发参数的时候才需要添加，1分发给value1,2分发给value2
    def test_tuple(self,value1,value2):
        print('--1',value1,value2)
        self.assertEqual(value2,value1+1)

    @data([1,2],[2,3])
    @unpack
    def test_list(self,value1,value2):
        print('--2',value1,value2)
        self.assertEqual(value2,value1+1)

    @data({'value1':1,'value2':2},{'value1':2,'value2':3})
    @unpack
    def test_dict(self,value1,value2):
        print('--3',value1,value2)
        self.assertEqual(value2,value1+1)


if __name__ == '__main__':
    unittest.main()



