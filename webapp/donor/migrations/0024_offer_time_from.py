# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0023_auto_20150519_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 29, 45, 134172)),
            preserve_default=True,
        ),
    ]
