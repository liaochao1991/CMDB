#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/4 21:34
# @Author : liaochao
# @File   : disk.py


#from utils import saltapi
from utils.src.plugins.base import BasePlugin
from  utils.lib.response import BaseRespone
import traceback

class Disk(BasePlugin):
    # def run(self):
    #     dis_mess = saltapi.salt_result("df -h")
    #     disk_dic = {}
    #     for slat_id,v in dis_mess.items():
    #         dis_dic = {}
    #         disk=v.split()
    #         dis_dic["disk"]=disk[11]
    #         disk_dic[slat_id]=dis_dic
    #     return disk_dic
    def linux(self):
        dis_dic={}
        response = BaseRespone()
        try:
            #通salt调用linux命令
            dis_mess = BasePlugin().salt("df -h")
            #print("获取到的磁盘信息：",dis_mess)
            for slat_id, v in dis_mess.items():
                disk = v.split()
                #print(disk)
                dis_dic["disk"] = disk[11]
            response.data=dis_dic
        except Exception as e:
            msg = "%s linux disk plugin error: %s"
            self.logger.log(msg % (self.hostname, traceback.format_exc()), False)
            response.status = False
            response.error = msg % (self.hostname, traceback.format_exc())
        return response

