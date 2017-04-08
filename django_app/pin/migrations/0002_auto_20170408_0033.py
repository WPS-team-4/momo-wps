# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pin',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
