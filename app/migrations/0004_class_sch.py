# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-20 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190520_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='sch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
    ]
