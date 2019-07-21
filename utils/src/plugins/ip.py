#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/4 21:33
# @Author : liaochao
# @File   : ip.py

from utils.src.plugins.base import BasePlugin
from utils.lib.response import BaseRespone
import traceback

mess_neizhi=BasePlugin().salt()

class Ip(BasePlugin):
    def linux(self):
        getIp_dic={}
        response = BaseRespone()
        try:
            for slat_id,ip_mess in mess_neizhi.items():
                ip_parse=ip_mess['ip4_interfaces']
                #print(ip_parse)
                #排除掉lo网络和docker网络
                for eth,ip_list in ip_parse.items():
                    if eth != "lo" and eth != "docker0":
                        for ip in ip_list:
                            ip_dic = {}
                            is_ip=ip.split(".")[0]
                            #经过冒号分割后,为整数的可以判断为ip
                            if is_ip.isdigit():
                                ip_dic["ip"]=ip
                                #getIp_dic[slat_id]=ip_dic
                                response.data=ip_dic
        except Exception as e:
            msg = "%s linux ip plugin error: %s"
            self.logger.log(msg % (self.hostname, traceback.format_exc()), False)
            response.status = False
            response.error = msg % (self.hostname, traceback.format_exc())

        return response

# print(Ip().linux().data)