# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 15:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0004_auto_20170305_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mat_info',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 8, 15, 0, 18, 479253, tzinfo=utc)),
        ),
    ]
