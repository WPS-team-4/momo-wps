# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20170417_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='is_visible',
        ),
    ]
