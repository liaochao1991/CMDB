#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/12 16:57
# @Author : liaochao
# @File   : response.py

class BaseRespone:
    def __init__(self):
        self.status=True
        self.message=None
        self.data=None
        self.error=None