#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/5/13 23:03
# @Author : liaochao
# @File   : my_tags.py

from django.template import Library

from django.utils.safestring import mark_safe
import datetime
#register的名字是固定的,不可改变
register = Library()
@register.filter
def filter_func(x,y):
    return x+y

#处理多个参数
@register.simple_tag
def simple_fun(a,b,c):
    d = datetime.datetime.now()
    date = d.strftime('%Y-%m-%d')
    return date