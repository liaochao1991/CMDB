#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/11 15:05
# @Author : liaochao
# @File   : pool_test.py

from concurrent.futures import ThreadPoolExecutor
import time
# def task(arg):
#     print(arg)
#     time.sleep(1)
# #最大线程数为5个，也就是线程池只存放5个线程
# pool = ThreadPoolExecutor(5)
# for i in range(50):
#     #执行线程的时候一个参数只需要写函数名,第二个传入函数参数
#     pool.submit(task,i)
# import os
# BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# cert_path=os.path.join(BASE_PATH,"conf","cert")
# print(BASE_PATH)
# print(cert_path)

# from utils.lib.log import Logger
# logger = Logger()
#
# logger.log("错误",False)
# logger.log("正确",True)
from datetime import datetime
from datetime import date
import json
class JsonCustomEncoder(json.JSONEncoder):
    '''
        json只能序列化列表、元组、字典、布尔值、字符串
        不能序列化时间、内存地址等等。所以需要定制json
    '''
#     def default(self, filed):
#         if isinstance(filed,datetime):
#             return filed.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(filed,date):
#             return filed.strftime('%Y-%m-%d')
#         elif isinstance(filed,Response):
#             #默认存为字典
#             return filed.__dict__
#         else:
#             #不是上述格式就用默认的json方法
#             return json.JSONEncoder.default(self,filed)
#
# class Response(object):
#     def __init__(self):
#         self.status=True,
#         self.data="test message"
# data = {
#     'k1':'123',
#     'k2': datetime.now(),  #时间类型
#     'k3': Response()  #对象类型
#
# }
# #指定用我们定义的JsonCustomEncoder类来序列化
# ds = json.dumps(data,cls=JsonCustomEncoder)
# print(ds)
