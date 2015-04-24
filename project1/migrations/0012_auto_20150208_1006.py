# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0011_auto_20150208_1006'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_messages',
            new_name='user_message',
        ),
    ]
