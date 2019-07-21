#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/21 10:26
# @Author : liaochao
# @File   : auth.py

import json
import hashlib
import time
from CMDB.settings import ASSET_AUTH_HEADER_NAME,ASSET_AUTH_KEY,ASSET_AUTH_TIME
from django.http import JsonResponse
'''
    用于api认证时的认证具体实现方法
'''
#存放认证信息
ENCRYPT_LIST=[
    # {'encrypt': encrypt, 'time': timestamp}
]
def api_auth_method(request):
    auth_key = request.META['HTTP_AUTH_KEY']
    # 拿到的数据进行分割
    if not auth_key:
        return False
    sp = auth_key.split('|')
    if len(sp) != 2:
        print("认证超时")
        return False
    encrypt,timestamp = sp
    timestamp=float(timestamp)
    #服务端时间减去我们设置的时间间隔得到的时间
    limit_timestamp = time.time() - ASSET_AUTH_TIME
    if limit_timestamp > timestamp:
        print("认证超时")
        return False
    ha = hashlib.md5(ASSET_AUTH_KEY.encode('utf-8'))
    #拼接字符串与客户端带来的时间戳
    ha.update(bytes("%s|%f" %(ASSET_AUTH_KEY,timestamp),encoding="utf-8"))
    result = ha.hexdigest()
    print(result,encrypt)
    if result != encrypt:
        print("认证值不一致")
        return False
    #检查元素是否存在，对已经失效的元素进行清除
    exist = False
    del_keys = []
    for k,v  in enumerate(ENCRYPT_LIST):
        m=k['time']
        n = v['encrypt']
        if m < limit_timestamp:
            del_keys.append(k)
            continue
        #如果访问过的认证列表还有一样的值存在
        if n == encrypt:
            exist = True
    for k in del_keys:
        del ENCRYPT_LIST[k]

    if exist:
        return False
    #访问过后的认证信息加到列表中
    ENCRYPT_LIST.append({'encrypt': encrypt, 'time': timestamp})
    return True

def api_auth(func):
    def inner(request, *args, **kwargs):
        if not api_auth_method(request):
            return JsonResponse({'code': 1001, 'message': 'API授权失败'}, json_dumps_params={'ensure_ascii': False})
        return func(request, *args, **kwargs)

    return inner

