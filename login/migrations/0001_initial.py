# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-31 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=False, max_length=20)),
                ('user_pw', models.CharField(default=False, max_length=20)),
            ],
            options={
                'db_table': 'login_user',
                'verbose_name': '\ub85c\uadf8\uc778 \ud14c\uc2a4\ud2b8 \ud14c\uc774\ube14',
            },
        ),
    ]
