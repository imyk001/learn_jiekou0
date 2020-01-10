#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests
#请求百度首页
r = requests.get('https://www.baidu.com/')

print(r.url)
print(r.encoding) #编码
print(r.content)  #获取返回内容（自动解码gzip）
print(r.headers)
print(r.cookies)
