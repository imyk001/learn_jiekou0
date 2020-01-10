#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests

#发送get请求
urlstr = 'https://blog.csdn.net/rainshine1190'

#发送请求
r = requests.get(url = urlstr)

print(r.text)
