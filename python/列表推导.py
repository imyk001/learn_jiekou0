#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:列出100以内偶数中能整除3的所有数字
'''
l = [i for i in range(1,101)if i%2==0 if i%3 ==0]
print(l)