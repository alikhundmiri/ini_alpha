# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0007_auto_20170308_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_database',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 8, 15, 1, 43, 624420, tzinfo=utc)),
        ),
    ]
