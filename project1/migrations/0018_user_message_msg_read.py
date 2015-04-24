# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0017_auto_20150217_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_message',
            name='msg_read',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
