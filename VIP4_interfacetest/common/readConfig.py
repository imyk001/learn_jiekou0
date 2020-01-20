#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
# 1-导入包
import configparser
"""


4-关闭
"""
class readConfig(object):
    def __init__(self):
        # 2 - 创建对象
        self.conf = configparser.ConfigParser()
        # 3 - 读取文件
        self.conf.read(r'../config.ini',encoding='utf-8-sig')

    def get_emain(self,name):
        #-获取文件内容
        return self.conf.get('EMAIL',name)

if __name__ == '__main__':
    re = readConfig()
    print(re.get_emain('mail_user'))


