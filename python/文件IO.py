#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#————————————读取——————
#打卡文件open，两个常用参数：文件路径和打开模式
#路径支持绝对路径和相对路径
#模式：r:读 r+:读写 w：写（覆盖/新建）w+:读写（覆盖/新建）a:追加（存在的时候追加，没有的时候新建 ）
# f = open('F:\code\data.txt','w+')

 #写入
# # f.write('hello world')
# #
# # m = ['hello\n','world']
# # f.writelines(m)
# # f.seek(0)
# # print(f.read())
# # f.close()
# #-----------------------------简单写入
# f = open('F:\code\data.txt','w+')
# m = ['11\n','2\n','22\n','13\n','2\n','13']
# f.writelines(m)
# f.seek(0)
# l = f.readlines()
# l1 =[]
# for i in l:
#     i.rstrip('\n')
#     l1.append(int(i))
#     l1.sort()
# for j in l1:
#     if l1.count(j)>1:
#         l1.remove(j)
# print(l1)
# f.close()
# f1 = open('F:\code\data1.txt','w+')
# l2 =[]
# for i1 in l1:
#     i2 = str(i1)
#     l2.append(i2)
# print(l2)
# f1.close()
# f2 = open('F:\code\data2.txt','w+')
# for j1 in l2:
#     f2.write(j1+'\n')
# print(f2.read())
# f2.close()
#---------------------复杂写入
with open('F:\code\haha.txt','w+') as f:
    l = ['11,10,18\n','2,23,24\n','22,1,0\n','13,7\n','5\n','29,19\n','10,1,3,5,9']
    l1 =[]
    l2 = []
    f.writelines(l)
    f.seek(0)
    # print(f.readlines())
    for i in l:
        j = i.rstrip('\n').split(',')
        l1.extend(j)
    for i1 in l1:
        l2.append(int(i1))
        for i2 in l2:
            if l2.count(i2)>1:
                l2.remove(i2)
    print(sorted(l2))
with open('F:\code\haha1.txt','w+') as f1:
    l3 = []
    for i3 in sorted(l2):
        l3.append(str(i3))
    print(l3)
    for i4 in l3:
       f1.write(i4+'\n')
    f1.seek(0)
    print(f1.read())























