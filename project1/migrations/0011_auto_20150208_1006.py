# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0010_auto_20150208_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_id', models.IntegerField(default=1, max_length=100)),
                ('reciever_id', models.IntegerField(default=1, max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='user_message',
        ),
    ]
