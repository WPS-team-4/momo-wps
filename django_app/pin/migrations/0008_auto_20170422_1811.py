# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0007_pin_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
