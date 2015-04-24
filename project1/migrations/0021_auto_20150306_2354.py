# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0020_auto_20150223_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logged_in_users',
            name='user',
        ),
        migrations.DeleteModel(
            name='logged_in_users',
        ),
        migrations.AddField(
            model_name='login',
            name='last_log_in',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 23, 54, 22, 686448), auto_now=True),
            preserve_default=False,
        ),
    ]
