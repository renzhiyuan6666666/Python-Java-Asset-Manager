# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-27 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0002_remove_user_passwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
