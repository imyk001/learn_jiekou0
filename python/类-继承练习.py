#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#1、打印小猫爱吃鱼，小猫要喝水
# class cat(object):
#     def eat(self):
#         print('小猫爱吃鱼')
#     def drink(self):
#         print('小猫爱喝水')
# cat = cat()
# cat.eat()
# cat.drink()


#2、小明爱跑步，爱吃东西  1）小明体重75.0公斤
                        # 2）每次跑步会减肥0.5公斤
                        # 3）每次吃东西体重会增加1公斤
                        # 4）小美的体重是45.0公斤
# class Person(object):
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#     def __str__(self):
#         return '%s的体重是%.1f'%(self.name,self.weight)
#     def run(self):
#         print('%s每次跑步会减肥0.5公斤'%(self.name))
#         self.weight -= 0.5
#     def eat(self):
#         print('%s每次吃东西体重增加1公斤'%(self.name))
#         self.weight += 1
# xiaoming = Person('小明',75.0)
# xiaomei = Person('小美',45.0)
# print(xiaoming.__str__())
# print(xiaomei)
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)


#3摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
# 餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
#分析一下：
"""
房子类：
属性：户型，总面积
方法：放入家具
家具类：
属性：户型，占地面积
方法：
"""
# class Funiture(object):
#     def __init__(self,name,area):
#         self.name = name
#         self.area = area
#     def __str__(self):
#         return '家具%s的面积是%.1f'%(self.name,self.area)
# class house(object):
#     def __init__(self,type,area):
#         self.type = type
#         self.area = area
#         #剩余面积
#         self.free_area = area
#         #家具列表
#         self.Funiture_name = []
#     def add_Funiture(self,funiture):
#         print('要添加的%s家具'%(funiture))
#         self.free_area -= funiture.area
#         if funiture.area > self.free_area:
#             print('家具太大了，放不下')
#             return
#         self.Funiture_name.append(funiture.name)
#     def __str__(self):
#         return '房子是%s,总面积是%.1f，剩余面积是%.1f，家具名称是%s'%(self.type,self.area,self.free_area,self.Funiture_name)
# #创建家具对象
# bed = Funiture('床',120)
# wardrobe = Funiture('衣柜',2)
# desk = Funiture('桌子',1.5)
# print(bed)
# print(wardrobe)
# print(desk)
# #创建房子对象
# house = house('三室一厅',120)
# house.add_Funiture(bed)
# house.add_Funiture(wardrobe)
# house.add_Funiture(desk)
# print(house)

"""
士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
分析;
士兵
属性：name，
方法：开火（减少子弹数量），装填子弹（增加子弹数量）
枪
属性：name
"""


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None      #####这里先设为None  等枪示例化后再给
    def __str__(self):
        return '士兵%s有一把%s,%s。' % (self.name, self.gun.model, self.gun)
            # 这里gun.model为枪名字 gun为gun类的str

    def fire(self):
        if self.gun == None:
            print("没有武器！")
            return False
        self.gun.add_bullet(10)
        self.gun.shoot()
        return True
class gun:
    def __init__(self, model, bullet_count=0):
        self.model = model
        self.bullet_count = bullet_count

    def __str__(self):
        return '这把%s剩余%d子弹' % (self.model, self.bullet_count)

    def shoot(self):
        if self.bullet_count == 0:
            return False
        self.bullet_count -= 1
        print('发射一颗子弹')
        return True

    def add_bullet(self, count):
        self.bullet_count += count
        print('填充%d颗子弹' % count)
        return True

B = gun('AK-47')  # 填充30颗子弹
B.add_bullet(30)  # 发射一颗子弹
B.shoot()  # 射击
A = Soldier('瑞恩')  # 发射一颗子弹
A.gun = B  # 将实例化的枪给士兵
A.fire()  # 士兵开火
print(A)  ##士兵瑞恩有一把AK-47,这把AK-47剩余38子弹。







