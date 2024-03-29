# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-27 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190521_2124'),
    ]

    operations = [
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
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='区域')),
            ],
            options={
                'verbose_name_plural': '区域表',
            },
        ),
    ]
