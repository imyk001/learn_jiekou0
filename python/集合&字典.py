#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:分别定义一个集合和一个字典
1-	为集合和字典分别插入元素：55（d：55）
2-	分别删除集合和字典内的一个元素
3-	取出字典内的所有值（value）和集合组合一个列表
'''
#1
s = {1,2,3}
d = {'a':1,'b':2,'c':3}
s.add(55)
d.update({'d':55})
print(s,d)
#2
s.remove(1)
del d['a']
print(s,d)
#3
d1=d.values()
l1= list(s)
l1.extend(d1)
print(l1)

