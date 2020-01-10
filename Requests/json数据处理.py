#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests,json
#python的字典
payload = {'yoyo':True,
           'json':False,
           'pyhton':'226296743',
           }
print(type(payload))
#转换成json格式
data_json = json.dumps(payload)
print(type(data_json))
print(data_json)