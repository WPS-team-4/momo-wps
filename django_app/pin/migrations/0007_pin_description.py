# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0006_auto_20170420_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
