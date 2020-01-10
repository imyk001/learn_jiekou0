#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@projec：
'''
# #求1-100的和
# sum = 1
# for i in range(1,101):
#     sum = sum +i
#     i +=1
# print(sum)
# #求10的阶乘
# s=1
# for i in range(1,11):
#     s  = s * i
#     i +=1
# print(s)
#求100以内能被3整除的数，并将作为列表输出
# l = []
# for i in range(1,101):
#     if i%3 ==0:
#         l.append(i)
# print(l)
#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# l = [1,2,3,4,3,4,2,5,5,8,9,7]
# # l1 =[]
# # for i in l:
# #     if i not in l1:
# #         l1.append(i)
# #         l1.sort()
# # print(l1)
# l1 =[]
# for i in l:
#     l1.append(i)
#     if l1.count(i)>1:
#         l1.remove(i)
# print(l1)
#求斐波那契数列 1 1 2 3 5 8 13 ……
fibs =[]
for i in range(0,20):
    if i == 0 :
        fibs.append(1)
    elif i ==1 :
        fibs.append(1)
    else:
        fibs.append(fibs[i-2]+fibs[i-1])
print(fibs)




