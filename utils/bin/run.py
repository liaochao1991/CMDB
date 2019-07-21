#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/4 21:36
# @Author : liaochao
# @File   : run.py

from utils.src.script import client
##导入一个包的时候，会自动导入其中的__init__.py
'''
此时我们已经将一整套采集数据方法封装在plugins中
'''

if __name__ == '__main__':
    client()