#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/11 18:08
# @Author : liaochao
# @File   : script.py
from utils.conf import conf_profile
from .import client

def client():
    if conf_profile.MODE == "Agent":
        client.Agent().process()
    elif conf_profile.MODE == "SSH":
        client.SSH().process()
    elif conf_profile.MODE == "Salt":
        client.Salt().process()
    else:
        raise Exception("配置文件模式错误，请选择Agent|SSH|Salt")
