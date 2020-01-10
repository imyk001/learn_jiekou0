"""
ddt使用步骤：
1.导入ddt包
2.用装饰器装饰@ddt
3.传入参数，执行
"""
#1-------第一种传参方式:调试ddt，单个传参
import unittest
from ddt import ddt,data,unpack

@ddt
class MytestCase(unittest.TestCase):

    @data(1)#1传入value
    def test_normal(self,value):
        print(value)
        self.assertEqual(value,2)

    @data(2,3,4)#2,3,4会分别按照执行次数传入，比如第一次执行方法传入2，第二次执行方法传入3
    def test_normal(self,value):
        print(value)
        self.assertEqual(value,2)

if __name__ == '__main__':
    unittest.main()
