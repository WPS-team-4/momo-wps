# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0002_auto_20170331_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place_id',
            new_name='google_place_id',
        ),
    ]