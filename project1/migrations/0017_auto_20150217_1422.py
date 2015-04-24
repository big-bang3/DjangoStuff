# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0016_login_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
