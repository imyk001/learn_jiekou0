#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
查看帮助文档
import requests
help(requests.session())
"""
import requests
#发送post请求
urlstr = 'https://account.kmf.com/api/login/user'
data = {'username':'yk4659136','password':'qqqqqq'}
#初始化seesion对象
s = requests.session()
#通过session对象发送请求，服务器设置在本地的cookie会保存在本地
r = s.post(url=urlstr,data=data)
#通过session继续发送post请求，自动携带上一个请求返回的cookie
r2 = s.get('https://toefl.kmf.com/record')


print('r2:',r2.text)
print('r1:',r.text)