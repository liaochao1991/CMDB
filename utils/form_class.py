#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/5/27 9:49
# @Author : liaochao
# @File   : form_class.py

from django.forms  import  Form
from django.forms  import  fields
from django.forms  import  widgets
from apiAPP import models

class HostForm(Form):
    hostname = fields.CharField(
        #required=True, #是否允许为空
        error_messages={'required':'主机名不能为空'},
        # 加样式是 通过 form-control 修改
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    cpu = fields.CharField(
        required=True,
        error_messages={'required':'核心数不能为空'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    mem = fields.CharField(
        required=True,
        error_messages={'required':'内存大小不能为空'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    speed  = fields.CharField(
        required=True,
        #error_messages={'required':'不能为空'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    eth0_network = fields.CharField(
        required=True,
        error_messages={'required':'网卡信息不能为空'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    source_id = fields.ChoiceField(
        required=True,
        #error_messages={'required':'不能为空'},
        choices=[],
        #下拉框
        widget = widgets.Select(attrs={'class': 'form-control'}),
    )
    region_id = fields.ChoiceField(
        required=True,
        choices=[],
       # error_messages={'required':'不能为空'},
        widget = widgets.Select(attrs={'class': 'form-control'}),
    )
    state = fields.CharField(
        required=True,
        #choices=[],
        error_messages={'required': '不能为空'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}),
    )
    messages = "温馨提示,这里请填写正确的数字, (1, 'Running'),(2, '下线'), (3, '关机'),(4, '删除'), (5, '故障'),"

    def __init__(self,*args,**kwargs):
        '每次都默认执行初始化，保证在数据库拿到的数据是最新的'
        super(HostForm,self).__init__(*args,**kwargs)
        self.fields['source_id'].choices=models.Source.objects.values_list('id','name')
        self.fields['region_id'].choices=models.Region.objects.values_list('id','name')
        #messages = '温馨提示'
        #self.fields['state_id'].choices=models.Host.objects.values_list()
        #print('看看',self.fields['region_id'].choices)

