# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20170417_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='map',
            table=None,
        ),
    ]
