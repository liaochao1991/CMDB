#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/11 17:22
# @Author : liaochao
# @File   : __init__.py

import importlib
from utils.src.plugins.get_message import Get_basic
from utils.conf.conf_profile import Host_func_dic,host_li

def get_server_info(hostname=None):
    """
    获取服务器基本信息
    :param hostname: agent模式时，hostname为空；salt或ssh模式时，hostname表示要连接的远程服务器
    :return:
    """
    response =Get_basic(hostname).linux()
    #print("respone-->",response)
    if not response.status:
        return response
    #result_li = []
    for host in host_li:
        '''
        利用importlib反射来加载类
        '''
        path = Host_func_dic.get(host)
        # 字符串从右分割一次。
        module_path, class_name = path.rsplit(".", maxsplit=1)
        module = importlib.import_module(module_path)
        print(class_name)
        dis_class = getattr(module, class_name)
        JG = dis_class(hostname).linux()
        print("JG--》",JG)
        response.data[host]=JG
        print("aa->",response.data)
        #result_li.append(JG)
    return response

if __name__ =='__main__':
    ret = get_server_info()
    print(ret.__dict__)

#合并key值相同的字典用
#
# def Merge_dic():
#     dic = {}
#     salt_id = {}
#
#     #将key值相同的字典，放在同一个列表中
#     for i in result_li:
#         for k, v in i.items():
#             dic.setdefault(k, []).append(v)
#     for k1, v1 in dic.items():  # 遍历出每个salt_id对应的字典
#         tmp_dic = {}
#         for m in v1:  # 将每个salt_id里面的字典合并
#             tmp_dic.update(m)
#         salt_id[k1] = tmp_dic
#     return salt_id

