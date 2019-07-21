# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-27 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='名字')),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=64, null=True, verbose_name='挂载路径')),
                ('size', models.CharField(blank=True, max_length=16, null=True, verbose_name='磁盘大小/G')),
                ('remarks', models.CharField(blank=True, max_length=2048, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '磁盘',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=64, null=True, verbose_name='主机名')),
                ('ecsname', models.CharField(blank=True, max_length=64, null=True, verbose_name='实例名')),
                ('login_port', models.CharField(blank=True, default='22', max_length=16, null=True, verbose_name='登录端口')),
                ('cpu', models.CharField(blank=True, max_length=8, null=True, verbose_name='CPU')),
                ('mem', models.CharField(blank=True, max_length=8, null=True, verbose_name='内存')),
                ('speed', models.CharField(blank=True, default='5', max_length=8, null=True, verbose_name='带宽')),
                ('eth1_network', models.CharField(blank=True, max_length=32, null=True, verbose_name='公网IP')),
                ('eth0_network', models.CharField(max_length=32, verbose_name='私网IP')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='SN')),
                ('kernel', models.CharField(blank=True, max_length=64, null=True, verbose_name='内核版本')),
                ('remarks', models.CharField(blank=True, max_length=2048, null=True, verbose_name='备注')),
                ('createtime', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建时间')),
                ('expirytime', models.CharField(blank=True, max_length=32, null=True, verbose_name='到期时间')),
                ('state', models.SmallIntegerField(blank=True, choices=[(1, 'Running'), (2, '下线'), (3, '关机'), (4, '删除'), (5, '故障')], null=True, verbose_name='主机状态')),
                ('disks', models.ManyToManyField(default=1, to='apiAPP.Disk', verbose_name='磁盘')),
            ],
            options={
                'verbose_name_plural': '主机表',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(default='root', max_length=16, verbose_name='登录用户名')),
                ('login_pwd', models.CharField(blank=True, max_length=64, null=True, verbose_name='登录密码')),
                ('auth', models.CharField(blank=True, max_length=8, null=True, verbose_name='具有权限')),
            ],
            options={
                'verbose_name_plural': '主机用户表',
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='区域')),
            ],
            options={
                'verbose_name_plural': '区域表',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='名字')),
                ('address', models.URLField(blank=True, max_length=128, null=True, verbose_name='地址')),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='邮箱')),
                ('date', models.DateField(null=True, verbose_name='时间')),
                ('cla', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apiAPP.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, null=True, verbose_name='来源')),
            ],
            options={
                'verbose_name_plural': '主机来源表',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True, verbose_name='账户')),
                ('password', models.CharField(max_length=30, null=True, verbose_name='密码')),
                ('specialty', models.CharField(max_length=32, null=True, verbose_name='专业')),
                ('cla_name', models.ManyToManyField(to='apiAPP.Class')),
            ],
        ),
        migrations.AddField(
            model_name='number',
            name='num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apiAPP.Userinfo', verbose_name='学号'),
        ),
        migrations.AddField(
            model_name='host',
            name='logining',
            field=models.ManyToManyField(default=1, to='apiAPP.Login', verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='host',
            name='region',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiAPP.Region', verbose_name='地域'),
        ),
        migrations.AddField(
            model_name='host',
            name='source',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiAPP.Source', verbose_name='来源IP'),
        ),
        migrations.AddField(
            model_name='class',
            name='sch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apiAPP.School'),
        ),
        migrations.AddField(
            model_name='class',
            name='user',
            field=models.ManyToManyField(to='apiAPP.Userinfo'),
        ),
    ]
