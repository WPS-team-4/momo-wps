# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0002_auto_20170407_0226'),
        ('post', '0002_auto_20170407_0226'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PinComment',
        ),
        migrations.DeleteModel(
            name='PinPhoto',
        ),
    ]
