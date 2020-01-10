#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:1：定义一个1-9的元组，1、输出倒数第3个元素；2、输出值468:
         2：定义1-999的元组
         3:定义1-99的列表
         4：给定列表[11,13,5,7,0,56,23,34,72]
'''
#1
tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[2])
print(tuple[3:8:2])
#2
print(tuple(range(1,99)))
#3:1-99的list
print(list(range(1,99)))
#4.1求该列表中的最大值，最小值及列表中一共有几个元素
l = [11,13,5,7,0,56,23,34,72]
print(max(l))
print(min(l))
print(len(l))
#4.2获取56元素在列表的位置
print(l.index(56))
# 追加元素7
l.append(7)
print(l)
# 删除元素0
l.remove(0)
print(l)
# 排序列表（由大到小）
l1 = sorted(l)
l1.reverse()
print(l1)
# 将列表[66,67,68]与原列表组合
l2 = [66,67,68]
l.extend(l2)
print(l)
