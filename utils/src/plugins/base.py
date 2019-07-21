#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/13 16:47
# @Author : liaochao
# @File   : base.py

from utils.lib.log import Logger
from utils.conf import conf_profile
from utils.saltapi import SaltApi
class BasePlugin(object):
    '''
        执行salt模块
    '''
    def __init__(self,hostname=''):
        self.logger=Logger()
        self.mode_list=['agent','salt','ssh']
        self.hostname=hostname

    def salt(self,cmd=None):
        #print("执行同步命令")
        salt = SaltApi()
        #print('token-->>', salt.token)
        #salt_client = "*"
        salt_client='cmdb_master'
        salt_cmd = "grains.items"
        salt_method = "cmd.run"
        #salt_params = "free -m"
        if not cmd:
            #print("无参数")
            result = salt.salt_command(salt_client, salt_cmd)
            return result
        else:
            #print("有参数")
            result = salt.salt_command(salt_client, salt_method, cmd)
            return result

    def execute(self):
        #print("出现在父类次数")
        return self.linux()
    def linux(self):
        '''表示必须要有linux方法'''
        raise Exception('You must implement linux method.')
