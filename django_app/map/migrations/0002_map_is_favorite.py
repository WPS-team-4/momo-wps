# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
