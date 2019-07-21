#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/6/11 15:31
# @Author : liaochao
# @File   : client.py
from concurrent.futures import ThreadPoolExecutor
from utils.conf import conf_profile
import logging
import json
import requests
from utils.src import plugins
from utils.lib.log import Logger
from utils.lib.serialize import Json
import time
import hashlib
'''
    根据获取数据的方式，可以分为三类，将数据发送到api
    agent形式：1 采集资产、2 将资产数据发送到API(POST)
    SSH形式：1 获取今日未采集的主机列表、 2 采集资产、3 将资产数据发送到API(POST)
    salt形式：1 获取今日未采集的主机列表、 2 采集资产、3 将资产数据发送到API(POST)
'''
class AutoBase(object):
    def __init__(self):
        self.asset_api=conf_profile.ASSET_API
        self.key=conf_profile.KEY
        self.key_name=conf_profile.AUTH_KEY_NAME
    def auth_key(self):
        """
            接口认证,得到一个认证信息字典
        :return:
        """
        ha =hashlib.md5(self.key.encode('utf-8'))
        time_span=time.time()
        #将key和时间戳拼接
        ha.update(bytes("%s|%f" %(self.key,time_span),encoding='utf-8'))
        encryption=ha.hexdigest()
        result = "%s|%f" %(encryption,time_span)
        #返回一个认证信息字典
        #获取大概的格式：{'auth-key':6dfb804972fba0ea35e8767b9947985f|1561081938.810807}
        return {self.key_name:result}
    def get_asset(self):
        """
        get方式向获取未采集的资产
        :return: {"data": [{"hostname": "c1.com"}, {"hostname": "c2.com"}], "error": null, "message": null, "status": true}
        """
        try:
            headers={}
            headers.update(self.auth_key())
            response = requests.get(
                    url=self.asset_api,
                headers=headers
            )
        except Exception as e:
            return response.json()
    def post_asset(self,msg,callback=None):
        """
        post方式向接口提交资产信息，利用callback回调函数记录失败日志
        :param msg:
        :param callback:
        :return:
        """
        try:
            headers={}
            #header从auth_key()中获取
            headers.update(self.auth_key())
            response = requests.post(
                    url=self.asset_api,
                #请求头最好不要用下划线(_),最好用-
                    headers=headers,
                    json=msg
            )
        except Exception as e:
            response = e
            status=False
        if callback:
            callback(status,response)
    def process(self):
        """
        派生类需要继承此方法，意思就是子类必须要有自己的process（）方法，
        用于处理请求的入口
        :return:
        """
        raise NotImplementedError('you must implement process method')
    def callback(self,status,response):
        """
        提交资产后的回调函数,(会出错的地方的日志，我们需要记录下来)
        :param status: 是否请求成功
        :param response: 请求成功，则是响应内容对象；请求错误，则是异常对象
        :return:
        """
        if not status:
            Logger().log(str(response),False)
            return
        ret =json.loads(response.text)
        if ret['code'] == 1000:
            #此处True代表记录的正确的日志
            Logger().log(ret['message'], True)
        else:
            #此处False代表记录的错误的日志
            Logger().log(ret['message'], False)

class BaseClient(object):
    #发送数据api方法
    def send_data(self):
        pass
class SbaseClient(BaseClient):
    #获取主机列表
    def get_host(self):
        pass
class Agent(BaseClient):
    '''
       agent模式，获取主机名，判断机器是否更新，我们需要将主机名做成唯一标识，因为sn号有虚拟机会有重复现象，
        mac地址也会重复，ip会变，所以我们设定主机名为唯一
    '''
    def file_host(self):
        f = open("nid")
        data = f.read()
        f.close()
        if data:
            return data
    def process(self):
        #采集资产
        from .plugins import base
        data_dic=base().BasePlugin()
        #先从文件中取主机名,没有再从服务器上取
        hostname = self.file_host()
        if hostname:
            data_dic['hostname']=hostname
        else:
            #获取当前主机名
            #写入nid文件
            data_dic['hostname'] = "tmp_hostname"
        #将数据发送到api(POST)
        self.send_data(data_dic)
class SSH(SbaseClient):
    def process(self):
        #1、获取今日未采集的主机列表
        host_list = self.get_host()
        for host in host_list:
            #2、采集资产
            data_dic={}
            #3、将数据发送到api
            self.send_data(data_dic)
class Salt(AutoBase):
    def process(self):
        """
         根据主机名获取资产信息，将其发送到API
         :return:
         {
             "data": [ {"hostname": "c1.com"}, {"hostname": "c2.com"}],
            "error": null,
            "message": null,
            "status": true
         }
         """
        #1、获取今日未采集的主机列表
        task = self.get_asset()
        if not task['status']:
            #False表示日志打印在error中
            Logger().log(task['message'],False)
        #创建线程池，最大线程为5
        pool=ThreadPoolExecutor(5)
        for item in task['message']:
            hostname = item['hostname']
            #用5个线程调用run方法，参数为hostname
            pool.submit(self.run,hostname)
        pool.shutdown(wait=True)

    def run(self,hostname):
        '''
        获取指定主机名的资产信息
        {'status': True,
        'message': None, 'error': None,
         'data': {'disk': <lib.response.BaseResponse object at 0x00000000014686A0>,
          'main_board': <lib.response.BaseResponse object at 0x00000000014689B0>,
          'nic': <lib.response.BaseResponse object at 0x0000000001478278>,
          'memory': <lib.response.BaseResponse oat 0x0000000001468F98>bject ,
          'os_platform': 'linux', 'os_version': 'CentOS release 6.6 (Final)',
           'hostname': 'c1.com',
           'cpu': <lib.response.BaseResponse object at 0x0000000001468E10>}}
        :param hostname:
        :return:
        '''

        server_info = plugins.get_server_info(hostname)
        #序列化成字符串
        server_json = Json.dumps(server_info.data)
        #发送到api
        self.post_asset(server_json,self.callback)


# class AutoSalt(object):
#     def post_asset(self):
#         '''发送api接口的方法'''
#         pass
#     def process(self):
#         '''
#         根据主机名获取资产信息，将其发送api
#         :return:
#         '''
#         '''
#          task接受到的数据格式为：
#          {
#             "data":
#               [{"hostname":"c1.com"},{"hostname":"c2.com"},
#               "error":null,"message":null,"status":true]
#          }
#         '''
#         task = result
#         if not task['status']:
#             Logger().log(task['message'],False)
#         #创建线程池，最大可用线程5个
#         pool =ThreadPoolExecutor(5)
#         for item in task['data']:
#             hostname = item["hostname"]
#             #取线程执行run()方法,传入的参数是hostname
#             pool.submit(self.run,hostname)
#         pool.shutdown(wait=True)
#
#     def run(self,hostname):
#         #获取指定主机名的资产信息
#         server_info = plugins.get_server_info(hostname)
#         #序列化
#         server_json = json.dumps(server_info.data)
#         #发送到api
#         self.post_asset(server_json,self.callback)

