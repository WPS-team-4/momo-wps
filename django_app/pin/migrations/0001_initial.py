# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_name', models.CharField(max_length=100)),
                ('pin_color', models.CharField(blank=True, default='0,0,0', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Map')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
        ),
        migrations.CreateModel(
            name='PinHashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('hash_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pin.HashTag')),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pin.Pin')),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pin.Pin'),
        ),
        migrations.AlterUniqueTogether(
            name='pinhashtag',
            unique_together=set([('hash_tag', 'pin')]),
        ),
    ]
