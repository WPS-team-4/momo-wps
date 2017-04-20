# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0005_auto_20170420_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_label',
            field=models.CharField(choices=[('0', 'place'), ('1', 'food'), ('2', 'cafe'), ('3', 'shop'), ('4', 'etc')], default=0, max_length=1),
        ),
    ]