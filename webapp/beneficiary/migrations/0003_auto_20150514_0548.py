# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0002_auto_20150514_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytimewindows',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 48, 38, 826250, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliverytimewindows',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 48, 48, 277346, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliverytimewindows',
            name='day_of_week',
            field=models.CharField(max_length=3, choices=[(b'Mon', 'Monday'), (b'Tue', 'Tuesday'), (b'Wed', 'Wednesday'), (b'Thu', 'Thursday'), (b'Fri', 'Friday'), (b'Sat', 'Saturday'), (b'Sun', 'Sunday')]),
            preserve_default=True,
        ),
    ]
