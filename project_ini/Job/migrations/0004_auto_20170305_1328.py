# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 13:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0003_auto_20170305_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_database',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 5, 13, 28, 36, 379231, tzinfo=utc)),
        ),
    ]
