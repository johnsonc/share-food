# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0023_auto_20150612_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 11, 9, 13, 960694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 11, 9, 13, 960728, tzinfo=utc)),
        ),
    ]
