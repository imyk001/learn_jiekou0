#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#导入模块的方法


# #1------导入目标模块
# import Testmodule
# #调用模块内部的方法
# Testmodule.fun1()
# Testmodule.fun2()

#2------使用from...impor导入全部方法，配合__all__用法，目标模块内部通过__all__控制导入的方法：
# __all__=['fun1']
#
# from Testmodule import *
# fun1()
# fun2()

# #3----使用from...import导入指定方法
# from Testmodule import fun1
# fun1()

# #4----导入包的方法
# #from xx包 import xx模块
# from Testpackage import Mymodule
# Mymodule.yk1()
# Mymodule.yk2()

#5-----导入包名.模块名
# import Testpackage.Mymodule
# Testpackage.Mymodule.yk1()
# Testpackage.Mymodule.yk2()

#6-----__name__的作用：一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块
                        # 不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

from Testpackage import name

name.wan1()
name.wan2()

