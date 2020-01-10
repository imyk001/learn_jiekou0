#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#1-----------try.....except 已知异常类型
# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print('除数不能为0')
# a = int(input('输入a:',))
# b = int(input('输入b:',))
# calc(a,b)
# 2----------获取异常信息：用as result接受 print（result）
# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError as result:
#         print(result)
# a = int(input('输入a:',))
# b = int(input('输入b:',))
# calc(a,b)
# #3----------多个错误信息：用except后跟多个错误类型 (ZeroDivisionError,NameError) as result
# def calc(a,b):
#     try:
#         print(a/b)
#     except (ZeroDivisionError, NameError) as result:
#         print(result)
#
# a = int(input('输入a:',))
# b = int(input('输入b:',))
# calc(a,b)
#4-----------未知异常,BaseException和Exception
# def calc(a,b):
#     try:
#         print(a/b)
#     except BaseException:
#         print('出错啦')
#
# a = int(input('输入a:',))
# b = int(input('输入b:',))
# calc(a,b)
#5------多重异常：挨个匹配Exception后的异常类型、finally
# def calc(a,b):
#     try:
#         print(a/b)
#     except NameError:
#         print('该对象未声明')
#     except ZeroDivisionError:
#         print('除数不能为0')
#     finally:
#         print('程序执行完毕')
# a = int(input('输入a:',))
# b = int(input('输入b:',))
# calc(a,b)
#6-------else：在程序没有抛出异常的时候，继续执行else语句/raise抛出异
def calc(a,b):
    try:
        print(a/b)
    except NameError:
        print('该对象未声明')
        #查看异常后不做处理继续抛出异常
        raise
    except TypeError as msg:
        print(msg)
    else:
        print('程序执行完毕')
a = int(input('输入a:',))
b = int(input('输入b:',))
calc(a,b)

