#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/5/31 14:52
# @Author : liaochao
# @File   : get_message.py

from utils.src.plugins.base import BasePlugin
from utils.lib.response import BaseRespone

import traceback

class Get_basic(BasePlugin):
    '''
    获取cpu,系统版本，内存大小
'''
    def linux(self):
        base_dic={}
        try:
            response = BaseRespone()
            mess_neizhi = BasePlugin().salt()
            mess_dic={}
            for slat_id,mess in mess_neizhi.items():
                mess_dic["cpu"]=mess['num_cpus']
                mess_dic["os"]=mess["os"]+mess["osrelease"]
                mem_total = mess['mem_total'] / 1024+1
                mess_dic["mem"] = int(mem_total)
                mess_dic["hostname"] = mess["host"]
                #设定一个状态默认值表示机器是运行状态。
                mess_dic["state"]=1
                     #base_dic[slat_id] = mess_dic
            response.data=mess_dic
        except Exception as e:
            msg = "%s BasicPlugin Error:%s"
            self.logger.log(msg % (self.hostname,traceback.format_exc()),False)
            response.status=False
            response.error = msg %(self.hostname,traceback.format_exc())
        return response
'''
{'cpu': 2, 'os': 'CentOS7.5.1804', 'mem': 8, 'hostname': 'bes-test', 'state': 1}
'''

#Get_basic().execute().data


