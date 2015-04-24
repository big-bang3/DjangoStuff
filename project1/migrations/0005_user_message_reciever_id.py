# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0004_user_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_message',
            name='reciever_id',
            field=models.IntegerField(default=1, max_length=100),
            preserve_default=True,
        ),
    ]
