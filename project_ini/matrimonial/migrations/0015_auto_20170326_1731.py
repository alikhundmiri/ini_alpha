# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0014_auto_20170321_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mat_info',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 26, 17, 31, 22, 296098, tzinfo=utc)),
        ),
    ]
