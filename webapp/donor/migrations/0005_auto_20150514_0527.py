# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_auto_20150514_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 27, 32, 50779, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 27, 38, 434444, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
