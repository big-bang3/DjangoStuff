# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_link_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='url',
        ),
        migrations.AddField(
            model_name='link',
            name='password',
            field=models.CharField(default='abcd', max_length=100),
            preserve_default=False,
        ),
    ]
