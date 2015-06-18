# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tel_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tel_2',
        ),
        migrations.AddField(
            model_name='profile',
            name='beneficiary',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='donor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
