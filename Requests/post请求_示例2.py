#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests,json
#发送post请求
urlstr = 'http://httpbin.org/post'
#参数
payload = {'qq群名':'seleni+jmeter+loadrunner','qq群号':'106014970'}
#发送请求,接口请求为json数据，通过json自动将python对象转化为json类型
r = requests.post(url=urlstr,json=payload)
#获取结果
print(r.text)
#返回json类型，既可以通过r.json方法来查看结果
print(r.json())
