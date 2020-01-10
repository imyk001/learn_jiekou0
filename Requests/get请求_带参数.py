#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests

#发送get请求
urlstr = 'https://www.wanandroid.com/article/query?k=Android'
#参数
payload = {'k':'Android'}
#发送请求
r = requests.get(url = urlstr,params= payload)
#获取结果
print(r.text)
print(r.status_code)

