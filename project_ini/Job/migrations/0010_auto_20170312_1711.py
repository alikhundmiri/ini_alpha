# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 17:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0009_auto_20170312_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_database',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 17, 11, 29, 961318, tzinfo=utc)),
        ),
    ]
