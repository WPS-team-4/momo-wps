# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_remove_momouser_facebook_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='momouser',
            name='hash_username',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='momouser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]