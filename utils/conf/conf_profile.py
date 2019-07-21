#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/10 9:11
# @Author : liaochao
# @File   : conf_profile.py

import os

BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#salt api地址，用于执行salt命令
salt_api="https://192.168.25.130:8001/"
# Agent模式保存服务器唯一ID的文件
cert_path=os.path.join(BASEDIR,"conf","cert")
# 错误日志
ERROR_LOG_FILE = os.path.join(BASEDIR, "log", 'error.log')
# 运行日志
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')
# 用于API认证的KEY
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'

#加载所有的类,采集硬件信息的插件
Host_func_dic={
    'disk':'utils.src.plugins.disk.Disk',
    'ip':'utils.src.plugins.ip.Ip',
    'base':'utils.src.plugins.get_message.Get_basic',
}
#控制需要展示的属性
host_li=['ip','disk','base']

#暂定模式为salt
#MODE ="Salt"
MODE ="other"
#传入django的接口
ASSET_API="127.0.0.1:8000/api/saltapi"