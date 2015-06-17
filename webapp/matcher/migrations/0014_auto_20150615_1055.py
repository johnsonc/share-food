# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0013_auto_20150612_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matched',
            options={'verbose_name': 'Delivery schedule (Match)', 'verbose_name_plural': 'Delivery schedules (Matches)', 'permissions': (('readonly', 'Can read matches'),)},
        ),
        migrations.AlterModelOptions(
            name='visitpoint',
            options={'ordering': ['seq_num'], 'verbose_name': 'Visit point', 'verbose_name_plural': 'Visit points'},
        ),
        migrations.AlterField(
            model_name='visitpoint',
            name='donor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visitpoint',
            name='status',
            field=models.CharField(default=b'p', max_length=1, choices=[(b'p', 'Pending'), (b'c', 'Confirmed')]),
        ),
    ]
