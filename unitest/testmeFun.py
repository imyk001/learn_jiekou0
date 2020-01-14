#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import unittest
from meFun import *
import HTMLTestRunner

class testMyfun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('执行所有用例前的准备工作')
    @classmethod
    def tearDownClass(cls):
        print('执行完所有用例后的清理工作')
    def setUp(self):
        print('执行单个用例前的准备工作')
    def tearDown(self):
        print('执行完单个用例后的清理工作')


    @unittest.skip('跳过这条用例')
    def test_add(self):
        self.assertEqual(3,add(1, 2))
        self.assertNotEqual(3,add(2,2))
    def test_minus(self):
        self.skipTest('跳过这个用例')
        self.assertNotEqual(1,minus(2,1))
    def test_multi(self):
        self.assertEqual(6,multi(2,3))
    def test_divide(self):
        self.assertEqual(2,divide(2,1))
        self.assertNotEqual(1,divide(2,1))
discover = unittest.defaultTestLoader.discover(start_dir=testMyfun,pattern='test*.py',top_level_dir=None)
#1------定义报告存放路径
report = '..\result'
#2------定义文件名，以写方打开
rp = open(report,'wb')
#3------定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream= rp,title=u'Test测试报告',description=u'用例执行情况：')
#4------运行测试用例
runner.run(discover)
#5------关闭报告文件
rp.close()

if __name__ == '__main__':
# 单元测试的执行方法一共有3种
# 1--------通过unittest。main（）加载全部test开头的用例并自动执行
# unittest.main(verbosity=1)

#2------通过添加测试套件的方法addTest，然后运行添加好的测试套件
    # suite =unittest.TestSuite()  #实例化Testsuite
    # suite.addTest(testMyfun('test_add'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

#3------通过testloader来加载指定目录下的test开头的用例，运行添加好的discover
    discover = unittest.defaultTestLoader.discover(start_dir=testMyfun,pattern='test*.py',top_level_dir=None)
    runner = unittest.TextTestRunner()
    runner.run(discover)