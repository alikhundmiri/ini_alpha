# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0019_auto_20170326_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_database',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 26, 17, 32, 50, 988252, tzinfo=utc)),
        ),
    ]
