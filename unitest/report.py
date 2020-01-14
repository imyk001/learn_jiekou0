#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#导入HTMLTestRunner包
import HTMLTestRunner,unittest
import testmeFun

#1------定义报告存放路径
report = 'F:\result'
#2------定义文件名，以写方打开
rp1 = open(report,'wb')
#3------定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream= rp,title=u'Test测试报告',description=u'用例执行情况：')
#4------运行测试用例
runner.run()
#5------关闭报告文件
rp1.close()