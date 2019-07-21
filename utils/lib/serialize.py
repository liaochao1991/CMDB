#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/14 11:25
# @Author : liaochao
# @File   : serialize.py

from datetime import datetime
from datetime import date

import json as default_json
from .response import BaseRespone
from json.encoder import JSONEncoder


class JsonEncoder(JSONEncoder):
    '''
        json只能序列化列表、元组、字典、布尔值、字符串
        不能序列化时间、内存地址等等。所以需要定制json
    '''
    def default(self, filed):
        if isinstance(filed,datetime):
            return filed.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(filed,date):
            return filed.strftime('%Y-%m-%d')
        #指定序列化BaseRespone 这个类
        elif isinstance(filed,BaseRespone):
            #默认存为字典
            return filed.__dict__
        else:
            #不是上述格式就用默认的json方法
            return JSONEncoder.default(self,filed)

class Json(object):

    @staticmethod
    def dumps(response, ensure_ascii=True):

        return default_json.dumps(response, ensure_ascii=ensure_ascii, cls=JsonEncoder)


# #测试用的类
# class BaseRespone(object):
#     def __init__(self):
#         self.status=True,
#         self.data="test message"
#  #测试用的字典
# data = {
#     'k1':'123',
#     'k2': datetime.now(),  #时间类型
#     'k3': BaseRespone()  #对象类型
#
# }
#
# ds = Json.dumps(data)
# print(ds)