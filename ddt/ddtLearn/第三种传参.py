#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import unittest
from ddt import ddt,data,unpack,file_data

#调试ddt，传入json

@ddt
class MyTestCase3(unittest.TestCase):
    @file_data('F:\json.json')
    def test_file(self,value):
        print(value)

if __name__ == '__main__':
    unittest.main()