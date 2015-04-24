# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0021_auto_20150306_2354'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_message',
        ),
    ]
