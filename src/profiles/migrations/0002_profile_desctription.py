# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desctription',
            field=models.TextField(default='description deafult text'),
        ),
    ]
