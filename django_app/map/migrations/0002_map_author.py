# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
