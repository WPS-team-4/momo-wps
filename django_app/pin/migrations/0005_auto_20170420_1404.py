# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0004_auto_20170414_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin',
            name='pin_color',
        ),
        migrations.AddField(
            model_name='pin',
            name='pin_label',
            field=models.CharField(choices=[(0, 'place'), (1, 'food'), (2, 'cafe'), (3, 'shop'), (4, 'travel')], default=0, max_length=1),
        ),
    ]
