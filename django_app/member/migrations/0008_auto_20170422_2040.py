# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20170422_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='momouser',
            name='userid',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]