# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 13:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170321_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 21, 13, 38, 20, 174756, tzinfo=utc)),
        ),
    ]