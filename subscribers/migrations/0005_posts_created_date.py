# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0004_auto_20170902_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
