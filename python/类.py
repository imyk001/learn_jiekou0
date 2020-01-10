#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#用法:
# class 类名(object):
#     属性
#     方法
# pS:属性和方法可以为空，里面直接pass即可，表示一个空类
# class Person(object):
#     def eat(self,food):
#         print("吃",food)
#     def sleep(self):
#         print('睡觉')
# a = Person()
#
# a.eat('米饭')
# a.sleep()
#练习：
# a、定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
# class student(object):
#     def study(self,name,course):
#         print(name+'学习'+course)
# a = student()
# a.study('梨花','数学')

#b、定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，
                # 实现打印：学号为xx的学生，学习xx课程

class Student(object):
    def __init__(self,sno):
        self.sno = sno
        print('学号为'+sno+'的学生')
    def study(self,course):
        print('学习'+course+'课程')
stu = Student('12')
stu.study('数学')




