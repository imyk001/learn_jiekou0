#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests
url = 'http://www.kuaidi.com/index-ajaxselectinfo-1202247993797.html'

header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
          }#get方法加user-agent就可以了

s = requests.session()
r = s.get(url,headers=header,verify=False)
result = r.json()
data = result['data']#获取data里面的内容
print(data)
print(data[0])
get_result = data[0]['context']#获取签收状态
print(get_result)