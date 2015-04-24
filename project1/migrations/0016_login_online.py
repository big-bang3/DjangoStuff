# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0015_user_message_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='online',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
