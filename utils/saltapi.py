#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/5/31 10:30
# @Author : liaochao
# @File   : saltapi.py

import requests
import json
from utils.conf.conf_profile import salt_api

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import ssl
context = ssl._create_unverified_context()

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()



class SaltApi:
    """
    定义salt api接口的类
    初始化获得token
    """
    def __init__(self):
        self.url = salt_api
        self.username = "saltapi"
        self.password = "saltapi"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Content-type": "application/json"
            # "Content-type": "application/x-yaml"
        }
        self.params = {'client': 'local', 'fun': '', 'tgt': ''}
        self.login_url = salt_api + "login"
        self.login_params = {'username': self.username, 'password': self.password, 'eauth': 'pam'}
       #获取token
        self.token = self.get_data(self.login_url, self.login_params).get('token')
        self.headers['X-Auth-Token'] = self.token

    def get_data(self, url, params):
        send_data = json.dumps(params)
        request = requests.post(url, data=send_data, headers=self.headers, verify=False)
        response = request.json()
        # print('----->>>>',response)
        result = dict(response)
        # print('result集合--->', result['return'][0])
        return result['return'][0]

    def salt_command(self, tgt, method, arg=None):
        """远程执行命令，相当于salt 'client1' cmd.run 'free -m'"""
        if arg:
            # salt内置key
            params = {'client':'local', 'fun': method, 'tgt': tgt, 'arg': arg}

        else:
            #salt内置key，定义params参数
            params = {'client':'local', 'fun': method, 'tgt': tgt}
        # print ('命令参数: ', params)
        result = self.get_data(self.url, params)
        # print ('result--->',result)
        return result

# def salt_result(salt_params=None):
#     #print("执行同步命令")
#     salt = SaltApi()
#     ('token-->>',salt.token)
#     salt_client="*"
#     #salt_client='cmdb_master'
#     salt_cmd="grains.items"
#     salt_method="cmd.run"
#     #salt_params="free -m"
#     if not salt_params:
#         #print("无参数")
#         result=salt.salt_command(salt_client,salt_cmd)
#         return result
#     else:
#         #print("有参数")
#         result=salt.salt_command(salt_client,salt_method,salt_params)
#         return result
#

