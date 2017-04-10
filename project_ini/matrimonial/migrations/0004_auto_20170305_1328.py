# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 13:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matrimonial', '0003_auto_20170305_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='mat_info',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mat_info',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 5, 13, 28, 36, 382168, tzinfo=utc)),
        ),
    ]