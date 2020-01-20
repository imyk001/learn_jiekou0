#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests
import json
class configHttp(object):

    def __init__(self):
        print('开始请求接口')
        print('请求接口完成')

    def get(self,url,param):
        result = requests.get(url = url,params=param)
        print('get请求完成')
        print('接口返回数据',result.text)
        #将result.text转化为字典格式
        dict1 = json.loads(result.text)
        errorcode = dict1['errorCode']
        print(errorcode)
        return errorcode

    def post(self,url,param):
        result = requests.post(url=url, data=eval(param))
        print('post请求完成')
        print('接口返回的结果',result.text)
        #将result.text转换为字典格式
        dict1 = json.loads(result.text)
        errorcode = dict1['errorCode']
        print('errorcode:',errorcode)
        return errorcode

if __name__ == '__main__':
    #实例化
    send = configHttp()
    #使用实例对象调用类中的方法
    payload = {'username':'liangchao','password':'123456'}
    send.post('https://www.wanandroid.com/user/login',payload)
