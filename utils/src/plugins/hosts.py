#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/5/31 15:26
# @Author : liaochao
# @File   : src.py
#from utils.src import get_message
import importlib
Host_func_dic={
    'cpu':'utils.src.get_message.Cpu',
    'disk':'utils.src.get_message.Disk',
    'mem':'utils.src.get_message.Mem',
    'ip':'utils.src.get_message.Ip',
}
path = Host_func_dic.get('disk')
#字符串从右分割一次。
module_path,class_name=path.rsplit('.',maxsplit=1)
print(module_path,class_name)
module = importlib.import_module(module_path)
disk_class = getattr(module,class_name)
JG = disk_class()
JG.run()