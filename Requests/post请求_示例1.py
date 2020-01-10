#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
查看官方文档
help(requests)
发送post请求（json形式）
1.post的body是json类型，有两种方法来传递json数据。
2.第一种：先导入json模块，用dumps方法转化成json格式。
3.第二种：使用json参数默认处理成json格式进行传递。
4.返回结果，传到data里
"""
import requests,json
#发送post请求
urlstr = 'http://httpbin.org/post'

payload = {'qq群名':'seleni+jmeter+loadrunner','qq群号':'106014970'}
#通过json.dumps方法将Python字符串转换成json类型
payload = json.dumps(payload)
#发送请求
r = requests.post(url=urlstr,data=payload)
#获取结果
print(r.text)
#返回为json类型，既可以通过r.json方法来查看结果
print(r.json())
