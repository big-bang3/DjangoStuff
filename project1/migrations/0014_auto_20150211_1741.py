# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project1', '0013_auto_20150211_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='logged_in_users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user_message',
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
        migrations.RemoveField(
            model_name='logged_in_userss',
            name='user',
        ),
        migrations.DeleteModel(
            name='logged_in_userss',
        ),
        migrations.RemoveField(
            model_name='logins',
            name='user',
        ),
        migrations.DeleteModel(
            name='Logins',
        ),
        migrations.DeleteModel(
            name='user_messagse',
        ),
    ]
