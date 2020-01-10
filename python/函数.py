#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:设计一个计算器，输入两个数，自动实现加减乘除（进阶：根据用户输入的计算符号计算结果）
'''
#1:位置参数
# def sum(a,b):
#     print(a+b)
# sum(1,2)
# #2:默认参数
# def sum1(a,b=1):
#     print(a+b)
# sum1(1,2)
#可变参数
# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for i in numbers:
#         sum +=i
#     return sum
# print(calc(1,2))
#关键字参数
def person(name,age,**kwargs):
    print('name',name,'age',age,kwargs)
person('xiaoming',15,sex='male')









# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
#
# # a = int(input("输入a："))
# # b = int(input("输入b："))
# a,b = input('输入a,b，并用逗号隔开：').split(',')
# c =input("请输入符号c:")
# if  c== '+':
#     add(int(a),int(b))
# elif c =='-':
#     sub(int(a),int(b))
# elif c =='*':
#     mul(int(a),int(b))
# elif c =='/':
#     div(int(a),int(b))
# else:
#     print('请输入正确的符号')









