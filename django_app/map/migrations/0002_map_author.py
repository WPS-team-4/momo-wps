# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.10.6 on 2017-04-11 11:07
=======
# Generated by Django 1.10.6 on 2017-04-12 11:37
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
