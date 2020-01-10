#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#语法：继承谁就在括号中写谁的类名
"""
1.继承谁，类中的括号就写谁
2.继承后，子类具有父类全部属性和方法，但是父类不能具备子类的属性和方法
3.如果父类中没有子类需要的方法，可以在子类中自行定义
注意*：实例化和调用方法的时候要区分是否需要传参
"""
# # for example
# class Animal(object):
#     def eat(self):
#         print("-----吃")
#     def drink(self):
#         print('------喝')
# class dog(Animal):
#     def bark(self):
#         print("----旺旺叫")
# class cat(object):
#     def catch(self):
#         print("-----抓老鼠")
# a = Animal()
# a.eat()
# a.drink()
#
# b = dog()
# b.eat()
# b.drink()
# b.bark()

#练习-----------定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）

#类的定义
class Person(object):
    # name ='lihua'
    def __init__(self,name):
        self.name = name
class Teacher(Person):
    def __init__(self, gh, name):
        self.gh = gh
        self.name = name
    def teach(self,course):
        print('工号为%s的老师，教%s课'%(self.gh,course))
        print('名字是%s，工号为%s的老师，吃饭'%(self.name,self.gh))

a = Teacher('12','lihua')
a.teach('数学')





















