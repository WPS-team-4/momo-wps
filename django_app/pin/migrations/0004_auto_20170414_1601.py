# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0003_auto_20170413_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_color',
            field=models.CharField(blank=True, default='0,0,0', max_length=11),
        ),
    ]
