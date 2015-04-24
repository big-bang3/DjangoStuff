# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0014_auto_20150211_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 18, 19, 59, 988019, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
